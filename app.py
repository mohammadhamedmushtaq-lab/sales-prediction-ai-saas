import os
import streamlit as st
import joblib
import pandas as pd
from auth import register, login

# ================= MODEL =================
model = joblib.load("model.pkl")

st.set_page_config(page_title="AI Sales Decision System", layout="centered")

# ================= SESSION =================
if "user" not in st.session_state:
    st.session_state.user = None

# ================= INIT =================
# ❌ IMPORTANT: koi register() yaha mat call karna
# sirf DB init agar hai to yaha rakho (optional)

# ================= LOGIN SYSTEM =================
if st.session_state.user is None:

    st.title("🔐 AI Sales Decision SaaS")

    option = st.radio("Choose Option", ["Login", "Register"])

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    # ================= REGISTER =================
    if option == "Register":
        if st.button("Register"):
            if username and password:
                result = register(username, password)
                if result == "SUCCESS":
                    st.success("Account created! 🚀")
                elif result == "USER_ALREADY_EXISTS":
                    st.error("User already exists!")
                else:
                    st.error("Registration failed!")
            else:
                st.warning("Fill username & password")

    # ================= LOGIN =================
    if option == "Login":
        if st.button("Login"):
            if username and password:
                user = login(username, password)
                if user:
                    st.session_state.user = username
                    st.success("Login successful 🚀")
                    st.rerun()
                else:
                    st.error("Invalid login")
            else:
                st.warning("Fill username & password")

# ================= MAIN APP =================
else:

    st.title(f"💰 Welcome {st.session_state.user}")

    if st.button("Logout"):
        st.session_state.user = None
        st.rerun()

    st.divider()

    tab1, tab2 = st.tabs(["📊 Single Prediction", "📁 CSV Upload"])

    # ================= TAB 1 =================
    with tab1:

        st.subheader("AI Sales Decision Support")

        price = st.number_input("💵 Price", 10)
        marketing = st.number_input("📢 Marketing", 200)
        discount = st.selectbox("🏷 Discount", [0, 1])
        category = st.selectbox("📦 Category", [1, 2, 3])
        customer_type = st.selectbox("👥 Customer Type", [0, 1])
        month = st.slider("🕒 Month", 1, 12)
        competition_price = st.number_input("📊 Competition Price", 10)

        if st.button("🚀 Predict Sales Probability"):

            data = pd.DataFrame([[
                price,
                marketing,
                discount,
                category,
                customer_type,
                month,
                competition_price
            ]], columns=[
                "price",
                "marketing",
                "discount",
                "category",
                "customer_type",
                "month",
                "competition_price"
            ])

            prob = model.predict_proba(data)[0][1]
            confidence = round(prob * 100, 1)

            st.divider()
            st.subheader("📊 Business Insight")

            st.write(f"📊 Sales Probability Score: **{confidence}%**")

            if confidence >= 75:
                st.success("🟢 Strong Market Fit (High Potential)")
            elif confidence >= 50:
                st.warning("🟡 Moderate Market Fit (Needs Optimization)")
            else:
                st.error("🔴 Low Market Fit (Risky Product)")

            st.divider()
            st.info("📊 Model: Random Forest Classifier")
            st.info("⚡ Output: Probability-based decision system")

    # ================= TAB 2 =================
    with tab2:

        st.subheader("📁 Bulk Sales Analysis")

        uploaded = st.file_uploader("Upload CSV File", type=["csv"])

        if uploaded:
            df = pd.read_csv(uploaded)

            required_cols = [
                "price",
                "marketing",
                "discount",
                "category",
                "customer_type",
                "month",
                "competition_price"
            ]

            df = df[required_cols]

            df["Prediction"] = model.predict(df)

            st.dataframe(df)

            csv = df.to_csv(index=False).encode("utf-8")

            st.download_button(
                "📥 Download Report",
                csv,
                "sales_report.csv",
                "text/csv"
            )

    # ================= CHARTS =================
    st.divider()
    st.subheader("📊 Dataset Insights")

    if os.path.exists("data.csv"):
        df_chart = pd.read_csv("data.csv")
        if "target" in df_chart.columns:
            st.bar_chart(df_chart["target"].value_counts())
        else:
            st.warning("target column missing")
    else:
        st.warning("No dataset found")

    # ================= FOOTER =================
    st.divider()
    st.caption("⚡ AI Sales Decision SaaS | Built by You")

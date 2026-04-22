import os

print("\n🔥 AI SALES SAAS PIPELINE STARTED\n")

# ================= STEP 1: DATA GENERATION =================
print("📊 Generating dataset...")

os.system("python generate_data.py")

print("✅ Dataset ready (data.csv)\n")

# ================= STEP 2: TRAIN MODEL =================
print("🧠 Training ML model...")

os.system("python train.py")

print("✅ Model trained (model.pkl)\n")

# ================= STEP 3: TEST PREDICTION =================
print("🔍 Running sample prediction...")

os.system("python predict.py")

print("\n🚀 PIPELINE COMPLETED SUCCESSFULLY")
print("💰 System is ready for SaaS deployment\n")

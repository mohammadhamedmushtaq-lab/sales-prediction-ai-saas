import pandas as pd
import random

data = []

for i in range(500):  # 🔥 500 rows (PRO level)
    price = random.randint(5, 50)
    marketing = random.randint(50, 500)
    discount = random.randint(0, 1)
    category = random.randint(1, 3)
    customer_type = random.randint(0, 1)
    month = random.randint(1, 12)
    competition_price = random.randint(5, 60)

    # 🔥 REALISTIC BUSINESS LOGIC (IMPORTANT)
    score = (
        marketing * 0.4 +
        (50 - price) * 2 +
        discount * 10 +
        (customer_type * 5) -
        abs(price - competition_price)
    )

    target = 1 if score > 80 else 0

    data.append([
        price,
        marketing,
        discount,
        category,
        customer_type,
        month,
        competition_price,
        target
    ])

df = pd.DataFrame(data, columns=[
    "price",
    "marketing",
    "discount",
    "category",
    "customer_type",
    "month",
    "competition_price",
    "target"
])

df.to_csv("data.csv", index=False)

print("✅ 500 ROWS REALISTIC DATA GENERATED")

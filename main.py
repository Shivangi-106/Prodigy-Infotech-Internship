import joblib
import pandas as pd
import random

# Load model and encoders
model = joblib.load("bank_model.pkl")
encoders = joblib.load("encoders.pkl")

# Define valid input options
input_options = {
    "age": lambda: random.randint(18, 95),
    "job": lambda: random.choice(['admin.', 'blue-collar', 'entrepreneur', 'housemaid', 'management', 'retired', 'self-employed', 'services', 'student', 'technician', 'unemployed', 'unknown']),
    "marital": lambda: random.choice(['married', 'single', 'divorced', 'unknown']),
    "education": lambda: random.choice(['basic.4y', 'basic.6y', 'basic.9y', 'high.school', 'illiterate', 'professional.course', 'university.degree', 'unknown']),
    "default": lambda: random.choice(['yes', 'no', 'unknown']),
    "housing": lambda: random.choice(['yes', 'no', 'unknown']),
    "loan": lambda: random.choice(['yes', 'no', 'unknown']),
    "contact": lambda: random.choice(['cellular', 'telephone']),
    "month": lambda: random.choice(['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']),
    "day_of_week": lambda: random.choice(['mon', 'tue', 'wed', 'thu', 'fri']),
    "duration": lambda: random.randint(30, 3000),
    "campaign": lambda: random.randint(1, 10),
    "pdays": lambda: random.choice([999] + list(range(1, 999))),
    "previous": lambda: random.randint(0, 5),
    "poutcome": lambda: random.choice(['success', 'failure', 'nonexistent']),
    "emp.var.rate": lambda: round(random.choice([-3.4, -1.8, -0.1, 1.1, 1.4]), 1),
    "cons.price.idx": lambda: round(random.uniform(92, 94.5), 3),
    "cons.conf.idx": lambda: round(random.uniform(-50, -26), 1),
    "euribor3m": lambda: round(random.uniform(0.5, 5.0), 3),
    "nr.employed": lambda: round(random.choice([4963.6, 5099.1, 5191.0, 5228.1]), 1)
}

# Generate random input
input_data = {key: generator() for key, generator in input_options.items()}

# Create DataFrame
df_input = pd.DataFrame([input_data])

# Encode categorical features
for col in df_input.select_dtypes(include='object').columns:
    if col in encoders:
        df_input[col] = encoders[col].transform(df_input[col])

# Make prediction
prediction = model.predict(df_input)[0]

# ---------------- Output ----------------
print("\n📊 Input Used for Prediction:\n")
for key, val in input_data.items():
    print(f"{key:>18}: {val}")

print("\n🔍 Prediction Result:")
print("✅  Customer is highly likely to open a term deposit.." if prediction == 1 else "❌ Customer is unlikely to proceed with the offer.")

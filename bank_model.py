import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
import joblib

# Load your dataset
df = pd.read_csv("bank-additional-full.csv", sep=';')

# Encode target
df['y'] = df['y'].map({'yes': 1, 'no': 0})

# Encode categorical features and save encoders
categorical_cols = df.select_dtypes(include='object').columns
encoders = {}

for col in categorical_cols:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    encoders[col] = le

# Split
X = df.drop("y", axis=1)
y = df["y"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = DecisionTreeClassifier(max_depth=5, random_state=42)
model.fit(X_train, y_train)

# Save model and encoders
joblib.dump(model, "bank_model.pkl")
joblib.dump(encoders, "encoders.pkl")

print("✅ Model and encoders saved.")

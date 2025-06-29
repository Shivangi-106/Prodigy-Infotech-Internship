import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set styling
sns.set(style="whitegrid")
plt.rcParams['figure.figsize'] = (10, 6)

# Load Titanic dataset (assumed locally saved as train.csv)
df = pd.read_csv("train.csv")

# ------------------ CLEANING ------------------ #
# Initial shape
print(f"Initial dataset shape: {df.shape}")

# 1. Check missing values
missing_summary = df.isnull().sum()

# 2. Fill 'Age' with median
df['Age'].fillna(df['Age'].median(), inplace=True)

# 3. Fill 'Embarked' with mode
df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)

# 4. Drop 'Cabin' (too many missing values)
df.drop(columns=['Cabin'], inplace=True)

# 5. Drop duplicates if any
df.drop_duplicates(inplace=True)

# ------------------ EDA ------------------ #

# 1. Survival count
survival_count = df['Survived'].value_counts()

# 2. Survival rate by gender
survival_by_sex = df.groupby('Sex')['Survived'].mean()

# 3. Survival rate by class
survival_by_class = df.groupby('Pclass')['Survived'].mean()

# 4. Age distribution
plt.figure()
sns.histplot(df['Age'], kde=True, bins=30)
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Count")
plt.savefig("eda_age_distribution.png")

# 5. Survival by gender (bar plot)
plt.figure()
sns.countplot(data=df, x='Sex', hue='Survived')
plt.title("Survival Count by Gender")
plt.savefig("eda_survival_gender.png")

# 6. Survival by class
plt.figure()
sns.countplot(data=df, x='Pclass', hue='Survived')
plt.title("Survival Count by Passenger Class")
plt.savefig("eda_survival_class.png")

# 7. Age vs. Fare scatter with survival
plt.figure()
sns.scatterplot(data=df, x='Age', y='Fare', hue='Survived')
plt.title("Age vs Fare (colored by Survival)")
plt.savefig("eda_age_fare_survival.png")

# 8. Correlation heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Correlation Matrix")
plt.savefig("eda_correlation_matrix.png")

# ------------------ SUMMARY ------------------ #
summary_report = {
    "Initial Shape": df.shape,
    "Missing Values (after cleaning)": df.isnull().sum().to_dict(),
    "Survival Count": survival_count.to_dict(),
    "Survival Rate by Gender": survival_by_sex.to_dict(),
    "Survival Rate by Class": survival_by_class.to_dict(),
}
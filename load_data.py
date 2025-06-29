'''
# load_data.py
import pandas as pd

def load_and_clean_data(filepath):
    # Try to load file normally
    df = pd.read_csv(filepath)

    # Print the column names found
    print("\n🧾 Columns found in the CSV file:")
    print(df.columns.tolist())

    # Clean column headers
    df.columns = df.columns.str.strip().str.lower()

    # Check if expected columns are there
    if "entity" not in df.columns or "sentiment" not in df.columns:
        raise ValueError("❌ ERROR: 'entity' and 'sentiment' columns not found in the file.")

    # Proceed with cleaning
    df.dropna(subset=["entity", "sentiment"], inplace=True)
    df['entity'] = df['entity'].str.title().str.strip()
    df['sentiment'] = df['sentiment'].str.lower()
    df = df[df['sentiment'].isin(['positive', 'neutral', 'negative'])]

    return df
'''


# load_data.py
import pandas as pd

def load_and_clean_data(filepath):
    df = pd.read_csv(filepath)

    print(f"🧾 Columns found in the CSV file:\n{list(df.columns)}")

    df.columns = [col.strip().lower() for col in df.columns]

    if "entity" not in df.columns or "sentiment" not in df.columns:
        raise ValueError("❌ ERROR: 'entity' and 'sentiment' columns not found in the file.")

    df['entity'] = df['entity'].str.title().str.strip()
    df['sentiment'] = df['sentiment'].str.lower().str.strip()

    df = df[df['sentiment'].isin(['positive', 'neutral', 'negative'])]

    return df[['sentence_id', 'entity', 'sentiment', 'tweet']]

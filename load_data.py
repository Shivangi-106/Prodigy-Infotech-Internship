import pandas as pd

def load_and_clean_data(data):
    print("📄 Loading data from:", data)
    df = pd.read_csv(data, low_memory=False, parse_dates=['Start_Time'])

    # Drop rows with missing critical values
    df.dropna(subset=['Start_Time', 'Start_Lat', 'Start_Lng', 'Weather_Condition'], inplace=True)

    # Extract useful time features
    df['Hour'] = df['Start_Time'].dt.hour
    df['DayOfWeek'] = df['Start_Time'].dt.day_name()
    df['Month'] = df['Start_Time'].dt.month_name()

    return df

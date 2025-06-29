def analyze_hourly(df):
    return df['Hour'].value_counts().sort_index()

def analyze_weather(df):
    return df['Weather_Condition'].value_counts().nlargest(10)

def analyze_road_features(df):
    features = ['Crossing', 'Traffic_Signal', 'Bump']
    result = {}
    for feature in features:
        if feature in df.columns:
            result[feature] = df[feature].value_counts(normalize=True) * 100
    return result

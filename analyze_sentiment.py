# analyze_sentiment.py
import pandas as pd

def overall_sentiment_counts(df):
    return df['sentiment'].value_counts()

def sentiment_by_entity(df):
    return df.groupby(['entity', 'sentiment']).size().unstack(fill_value=0)

def top_entities_by_mentions(df, top_n=10):
    return df['entity'].value_counts().head(top_n)

def sentiment_distribution_top_entities(df, top_n=5):
    top_entities = df['entity'].value_counts().head(top_n).index.tolist()
    filtered_df = df[df['entity'].isin(top_entities)]
    return filtered_df.groupby(['entity', 'sentiment']).size().unstack(fill_value=0)

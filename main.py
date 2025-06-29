# main.py
import os
from load_data import load_and_clean_data
from analyze_sentiment import (
    overall_sentiment_counts,
    sentiment_by_entity,
    top_entities_by_mentions,
    sentiment_distribution_top_entities
)
from visualize_sentiment import (
    plot_overall_sentiment,
    plot_sentiment_by_entity,
    plot_top_entities,
    heatmap_sentiment_distribution
)

FILE_PATH = "twitter_training.csv"
OUTPUT_FOLDER = "output"

def main():
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)

    already_saved = all([
        os.path.exists(os.path.join(OUTPUT_FOLDER, "overall_sentiment.png")),
        os.path.exists(os.path.join(OUTPUT_FOLDER, "sentiment_by_entity.png")),
        os.path.exists(os.path.join(OUTPUT_FOLDER, "top_entities.png")),
        os.path.exists(os.path.join(OUTPUT_FOLDER, "sentiment_heatmap.png"))
    ])

    df = load_and_clean_data(FILE_PATH)

    overall_counts = overall_sentiment_counts(df)
    by_entity = sentiment_by_entity(df)
    top_entities = top_entities_by_mentions(df)
    dist_top = sentiment_distribution_top_entities(df)

    plot_overall_sentiment(overall_counts, save=not already_saved)
    plot_sentiment_by_entity(by_entity, save=not already_saved)
    plot_top_entities(top_entities, save=not already_saved)
    heatmap_sentiment_distribution(dist_top, save=not already_saved)

if __name__ == "__main__":
    main()

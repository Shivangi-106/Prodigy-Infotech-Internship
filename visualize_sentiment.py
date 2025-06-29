# visualize_sentiment.py
import matplotlib.pyplot as plt
import seaborn as sns
import os

def plot_overall_sentiment(overall_counts, save=False):
    plt.figure(figsize=(6, 6))
    overall_counts.plot.pie(autopct='%1.1f%%', colors=['red', 'green', 'gray'])
    plt.title("Sentiment Distribution")
    plt.ylabel("")
    if save:
        plt.savefig("output/overall_sentiment.png", bbox_inches='tight')
    plt.show()

def plot_sentiment_by_entity(df_grouped, save=False):
    import matplotlib.pyplot as plt
    import os

    sentiment_colors = {
        'negative': '#E74C3C',   # red
        'neutral': '#95A5A6',    # gray
        'positive': '#2ECC71'    # green
    }

    # Ensure the correct order
    color_order = [sentiment_colors.get(col, '#cccccc') for col in df_grouped.columns]

    ax = df_grouped.plot(
        kind="bar",
        stacked=True,
        color=color_order,
        figsize=(16, 8),
        width=0.8
    )

    ax.set_title("Sentiment by Entity", fontsize=16)
    ax.set_xlabel("Entity", fontsize=12)
    ax.set_ylabel("Count", fontsize=12)
    ax.tick_params(axis='x', labelrotation=30)

    plt.legend(title="Sentiment", title_fontsize=12, fontsize=10, loc="upper left")
    plt.tight_layout()

    if save:
        os.makedirs("output", exist_ok=True)
        ax.get_figure().savefig("output/sentiment_by_entity.png", bbox_inches='tight')

    plt.show()


def plot_top_entities(df_grouped, save=False):
    plt.figure(figsize=(10, 6))
    df_grouped.plot(kind="bar", colormap="tab10")
    plt.title("Top Entities by Mentions")
    plt.xlabel("Entity")
    plt.ylabel("Mentions")
    plt.xticks(rotation=45)
    plt.tight_layout()
    if save:
        plt.savefig("output/top_entities.png", bbox_inches='tight')
    plt.show()

def heatmap_sentiment_distribution(pivot_table, save=False):
    plt.figure(figsize=(12, 6))
    sns.heatmap(pivot_table, annot=True, fmt="d", cmap="YlGnBu")
    plt.title("Sentiment Distribution (Top Entities)")
    plt.xlabel("Sentiment")
    plt.ylabel("Entity")
    if save:
        plt.savefig("output/sentiment_heatmap.png", bbox_inches='tight')
    plt.show()

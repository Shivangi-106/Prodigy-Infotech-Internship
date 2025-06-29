import matplotlib.pyplot as plt
import seaborn as sns

def plot_hourly_accidents(hourly_counts):
    plt.figure(figsize=(10, 6))
    sns.lineplot(x=hourly_counts.index, y=hourly_counts.values, marker='o')
    plt.title('Accidents by Hour of Day')
    plt.xlabel('Hour')
    plt.ylabel('Number of Accidents')
    plt.grid(True)
    plt.savefig('output/charts/hourly_accidents.png')
    plt.close()

def plot_weather_conditions(weather_counts):
    plt.figure(figsize=(10, 6))
    sns.barplot(x=weather_counts.values, y=weather_counts.index, palette='coolwarm')
    plt.title('Top 10 Weather Conditions for Accidents')
    plt.xlabel('Number of Accidents')
    plt.ylabel('Weather Condition')
    plt.tight_layout()
    plt.savefig('output/charts/weather_conditions.png')
    plt.close()

def plot_road_features(feature_dict):
    for feature, stats in feature_dict.items():
        plt.figure(figsize=(5, 5))
        stats.plot(kind='pie', autopct='%1.1f%%', startangle=90, title=f'{feature} Presence')
        plt.ylabel('')
        plt.tight_layout()
        plt.savefig(f'output/charts/{feature.lower()}_distribution.png')
        plt.close()

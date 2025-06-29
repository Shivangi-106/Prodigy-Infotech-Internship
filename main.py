from analysis.load_data import load_and_clean_data
from analysis.analyze_patterns import analyze_hourly, analyze_weather, analyze_road_features
from analysis.visualize_patterns import plot_hourly_accidents, plot_weather_conditions, plot_road_features
from analysis.map_hotspots import generate_accident_map
from utils.helper import ensure_directories

def main():
    # Ensure output folders exist
    ensure_directories()

    # Load dataset
    data_path = "data/data.csv"
    df = load_and_clean_data(data_path)

    # Analysis
    hourly_counts = analyze_hourly(df)
    weather_counts = analyze_weather(df)
    road_feature_stats = analyze_road_features(df)

    # Visualizations
    plot_hourly_accidents(hourly_counts)
    plot_weather_conditions(weather_counts)
    plot_road_features(road_feature_stats)

    # Map Hotspots
    generate_accident_map(df)

if __name__ == "__main__":
    main()

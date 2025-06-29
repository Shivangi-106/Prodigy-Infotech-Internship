import folium

def generate_accident_map(df):
    m = folium.Map(location=[df['Start_Lat'].mean(), df['Start_Lng'].mean()], zoom_start=5)

    for _, row in df.sample(1000).iterrows():
        folium.CircleMarker(
            location=(row['Start_Lat'], row['Start_Lng']),
            radius=2,
            color='red',
            fill=True,
            fill_opacity=0.5
        ).add_to(m)

    m.save('output/maps/accident_hotspots.html')

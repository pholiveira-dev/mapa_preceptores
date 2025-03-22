import folium

# Coordenadas do centro do Distrito Federal
mapa_df = folium.Map(location=[-15.7801, -47.9292], zoom_start=11)

# Lista de coordenadas dos funcionários (latitude, longitude) com nomes
coordenadas_funcionarios = [
    ("Pedro Henrique", -15.8751, -48.0817),  # Samambaia Norte
    ("Lucas", -15.641994898394096, -47.797991007838036),  # Sobradinho
    ("Itamara", -16.0204, -48.0665),  # Gama
    ("Emilaine", -15.83819625405043, -48.02766793312688)  # Águas Claras
]

# Adiciona os marcadores ao mapa
for nome, lat, lon in coordenadas_funcionarios:
    folium.Marker(
        location=[lat, lon],
        popup=f'{nome}',
        icon=folium.Icon(color='blue', icon='user')
    ).add_to(mapa_df)

# Salvar o mapa em um arquivo HTML
mapa_df.save("mapa_colaboradores.html")

print("Mapa gerado e salvo como mapa_colaboradores.html")

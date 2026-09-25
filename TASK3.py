locations = [         
("Tbilisi", 41.71, 44.82),
("Batumi", 41.64, 41.63),
("Kutaisi", 42.26, 42.71)
]

for city, lat, lon in locations:
    print(f"city: {city}, latitude: {lat}, longitude: {lon}")



city_names = [city for city, lat, lon, in locations]
print(city_names)
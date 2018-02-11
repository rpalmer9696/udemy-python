import folium
import pandas


def get_popup_string(name, typ, elev):
    return "Name: {} <br /> Type: {} <br /> Elevation: {}".format(name.replace("'", "\\'"), typ, str(elev) + " m")


def get_elevation_colour(elevation):
    if  elevation < 1000:
        return "green"
    elif 1000 <= elevation < 3000:
        return "orange"
    else:
        return "red"


def create_marker(lat, lon, name, typ, elev):
    popup_string = get_popup_string(name, typ, elev)
    colour = get_elevation_colour(elev)

    return folium.Marker(location=[lat, lon], popup=folium.Popup(popup_string), icon=folium.Icon(color=colour))


def create_circle_marker(lat, lon, name, typ, elev):
    popup_string = get_popup_string(name, typ, elev)
    colour = get_elevation_colour(elev)

    return folium.CircleMarker(
        location=[lat, lon], radius=6, popup=folium.Popup(popup_string), color=colour, fill=True, fill_opacity=0.6
    )


def append_map_group(marker_type):
    if marker_type is "marker":
        volcanoMarkerGroup.add_child(create_marker(lat, lon, name, typ, elev))
    else:
        volcanoMarkerGroup.add_child(create_circle_marker(lat, lon, name, typ, elev))



volcanoData = pandas.read_csv("data/Volcanoes_USA.txt")
foliumMap = folium.Map(location=[38.58, -99.09], zoom_start=5)
volcanoMarkerGroup = folium.FeatureGroup(name="Volcanoes")
populationGroup = folium.FeatureGroup(name="Population")

with open("data/world.json", "r", encoding="utf-8-sig") as file:
    populationGroup.add_child(
        folium.GeoJson(
            file.read(),
            style_function=lambda x: {
                'fillColor': 'green' if x['properties']['POP2005'] < 10000000 else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else "red"
            }
        )
    )

for lat, lon, name, typ, elev in zip(volcanoData["LAT"], volcanoData["LON"], volcanoData["NAME"], volcanoData["TYPE"], volcanoData["ELEV"]):
    append_map_group("circle_marker")



foliumMap.add_child(populationGroup)
foliumMap.add_child(volcanoMarkerGroup)

foliumMap.add_child(folium.LayerControl())

foliumMap.save("data/map1.html")

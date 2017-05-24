import folium
from itertools import cycle


def draw_paths(center, paths, file_name):
    """
    :param center: list[lat, lng]
    :param paths: list of Paths, where path is a list like this:
        [(52.529, 13.407, 'TItle 1'), (52.529, 13.407, 'TItle 2')]
    :param file_name: where to save the map, e.g. 'map.html'
    :return: 
    """
    colors = cycle(['red', 'blue', 'green', 'purple', 'orange', 'darkred',
                    'lightred', 'beige', 'darkblue', 'darkgreen', 'cadetblue',
                    'darkpurple', 'white', 'pink', 'lightblue', 'lightgreen',
                    'gray', 'black', 'lightgray'])

    def _draw_path(map, path):
        color = colors.next()
        coords = [[p[0], [p[1]]] for p in path]
        folium.PolyLine(
            locations=coords,
            color=color
        ).add_to(map)

        for point in path:
            coord = [point[0], point[1]]
            title = point[2]
            folium.Marker(
                coord,
                popup=title,
                icon=folium.Icon(color=color),
            ).add_to(map)

    map = folium.Map(
        location=center,
        zoom_start=15,
        tiles='Stamen Toner',
    )
    for path in paths:
        _draw_path(map, path)

    map.save(file_name)
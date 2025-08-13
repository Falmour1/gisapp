import geemap.foliumap as geemap

def create_map():
    m = geemap.Map(center=[0, 37], zoom=6)
    m.add_basemap("SATELLITE")
    return m

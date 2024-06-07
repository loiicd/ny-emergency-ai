import folium

from layers.boroughs import createBoroughsLayer
from layers.boroughsScore import createBoroughsScoreLayer
from layers.fireBattalions import createFireBattalionsLayer
from layers.firehouses import createFirehousesLayer
from layers.firehousesRadius import createFirehousesRadiusLayer
from layers.communityDistricts import createCommunityDistrictsLayer


map = folium.Map(location=[40.71552394800378, -74.01878975440212], zoom_start=11, tiles='CartoDB positron')

borough_layer = createBoroughsLayer()
boroughs_score_layer = createBoroughsScoreLayer()
community_districts_layer= createCommunityDistrictsLayer()
fire_battalions_layer = createFireBattalionsLayer()
firehouses_layer = createFirehousesLayer()
firehouses_radius_layer = createFirehousesRadiusLayer()

map.add_child(borough_layer)
map.add_child(boroughs_score_layer)
map.add_child(community_districts_layer)
map.add_child(fire_battalions_layer)
map.add_child(firehouses_layer)
map.add_child(firehouses_radius_layer)

folium.LayerControl().add_to(map)

map.save('./newYorkMap.html')
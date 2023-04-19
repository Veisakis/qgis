from qgis.core import *
import qgis.utils

import re
import sys
sys.path.append('C:/Users/mohstud82/OneDrive - MOH/Desktop/QGIS/scripts')

all_layers = [] 
for layer in QgsProject.instance().mapLayers().values():
    all_layers.append(layer.name())

base_name = QInputDialog().getItem(None, "Choose Base Layer", "Layer", all_layers, 0, False)[0]
base_layer = QgsProject.instance().mapLayersByName(base_name)[0]

filename = QInputDialog().getText(None, "CSV filename in EGSA87", "Name")[0]

with open('C:/Users/mohstud82/OneDrive - MOH/Desktop/' + filename) as f:
    lines = f.readlines()

pattern_coords = "^\d+\.\d+,\d+\.\d+"
pattern_id = "^\d+\\n"

i = 0
in_coords = False
error = False
for line in lines:
    i += 1
    found_pattern = bool(re.findall(pattern_coords, line))
    
    if found_pattern and not in_coords:
        file_coords = []
        file_coords.append(line)
        in_coords = True
        continue
    
    if found_pattern and in_coords:
        file_coords.append(line)
    
    if line == '\n' or i == len(lines):
        if file_coords:
            polygon_coords = []
            for set in file_coords:
                x,y = set.replace("\n", "").split(",")
                polygon_coords.append((float(x), float(y)))
            polygon = QgsGeometry.fromPolygonXY( [[ QgsPointXY(x,y) for x,y in polygon_coords ]] )

            fet = QgsFeature()
            fet.setGeometry(polygon)

            base_layer.startEditing()
            base_layer.dataProvider().addFeatures([fet])
            status = base_layer.commitChanges()
            
            if not status:
                error = True
        in_coords = False
        continue
print(polygon)
if error:
    iface.messageBar().pushMessage("Error", "Couldn't draw polygons.", level=Qgis.Critical, duration=3)
else:
    iface.messageBar().pushMessage("Polygons have been inserted.", level=Qgis.Success, duration=3)
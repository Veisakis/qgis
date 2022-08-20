from qgis.core import *
import qgis.utils

all_layers = [] 
for layer in QgsProject.instance().mapLayers().values():
    all_layers.append(layer.name())

x_layers = []
while True:
    selected_layer = QInputDialog().getItem(None, "Layer not to include", "Choose Layer", all_layers, 0, False)
    if selected_layer[1] == False:
        break
    x_layers.append(selected_layer[0])
    
crs = QInputDialog().getInt(None, "CRS", "Choose CRS")

for layer in QgsProject.instance().mapLayers().values():
    if (layer.name() in x_layers):
        continue
    layer.setCrs(QgsCoordinateReferenceSystem(crs[0],QgsCoordinateReferenceSystem.EpsgCrsId))
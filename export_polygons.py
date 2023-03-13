from qgis.core import *
import qgis.utils

all_layers = [] 
for layer in QgsProject.instance().mapLayers().values():
    all_layers.append(layer.name())

layer_name = QInputDialog().getItem(None, "Choose the layer where the polygon is", "Layer", all_layers, 0, False)[0]
layer = QgsProject.instance().mapLayersByName(layer_name)[0]

iface.setActiveLayer(layer)
active_layer = iface.activeLayer()
provider = active_layer.dataProvider()

features = active_layer.getFeatures()
for feat in features:
    coords = feat.geometry().asMultiPolygon()
    n_points = len(coords[0][0])
    with open("C:/Users/mohstud82/OneDrive - MOH/Desktop/coords.csv", "a") as f:
        f.write(str(feat.id()+1)+"\n")
        for i in range(n_points):
            f.write(str(coords[0][0][i][0])+","+str(coords[0][0][i][1])+"\n")
        f.write("\n")
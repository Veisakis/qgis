from qgis.core import *
import qgis.utils

all_layers = [layer.name() for layer in QgsProject.instance().mapLayers().values()]

base_name = QInputDialog().getItem(
    None, 
    "Choose Base Layer", 
    "Layer", 
    all_layers, 0, False
    )[0]
base_layer = QgsProject.instance().mapLayersByName(base_name)[0]
qgis.utils.iface.setActiveLayer(base_layer)
base = qgis.utils.iface.activeLayer()

fields = base.fields().names()
field_name = QInputDialog().getItem(
    None, 
    "Choose Field to compare", 
    "Fields", 
    fields, 0, False
    )[0]

filename = QInputDialog().getText(None, "txt filename", "Name")[0]
with open("C:/Users/mveis/Desktop/" + filename) as f:
    lines = f.readlines()

for line in lines:
    am = line.strip("\n")
    base.selectByExpression('"' + field_name + "\"='" + am + "'", QgsVectorLayer.AddToSelection)

features = []
selected = base.selectedFeatures()
for feat in selected:
    features.append(feat[field_name])

count = 0
for line in lines:
    am = line.strip("\n")
    if am not in features:
        print(am)
        count += 1

print("Selected Features: " + str(base.selectedFeatureCount()))
print("Not found: " + str(count))

from qgis.core import *
import qgis.utils

import csv
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
    
error = False

for line in lines:
    x,y = line.split(',')
    print(x,y)
    fet = QgsFeature()
    fet.setGeometry(QgsGeometry.fromPointXY( QgsPointXY(float(x),float(y)) ))

    base_layer.startEditing()
    base_layer.dataProvider().addFeatures([fet])
    status = base_layer.commitChanges()
            
    if not status:
        error = True
    in_coords = False
    continue

if error:
    iface.messageBar().pushMessage("Error", "Couldn't draw points.", level=Qgis.Critical, duration=3)
else:
    iface.messageBar().pushMessage("Points have been inserted.", level=Qgis.Success, duration=3)
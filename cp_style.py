from qgis.core import *
import qgis.utils

all_layers = [] 
for layer in QgsProject.instance().mapLayers().values():
    all_layers.append(layer.name())
    
prototype_name = QInputDialog().getItem(None, "Choose Prototype Layer", "Layer", all_layers, 0, False)[0]
prototype = QgsProject.instance().mapLayersByName(prototype_name)[0]
prototype_style = prototype.renderer().symbol().symbolLayers()[0].properties()

all_layers.remove(prototype_name)

layers = []
while True:
    selected_layer = QInputDialog().getItem(None, "Layer to apply changes to", "Layer", all_layers, 0, False)
    if selected_layer[1] == False:
        break
    layers.append(selected_layer[0])

for layer_name in layers:
    layer = QgsProject.instance().mapLayersByName(layer_name)[0]
    symbol = QgsMarkerSymbol.createSimple(prototype_style)
    layer.renderer().setSymbol(symbol)
    layer.triggerRepaint()



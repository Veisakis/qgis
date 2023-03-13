import time

from qgis.utils import iface

def peek():
    fieldname = layer.fields().names()[1]
    for feature in layer.getFeatures():
        print(feature[fieldname], layer.dataProvider().encoding())
        break

encodings = QgsVectorDataProvider.availableEncodings()

layer = iface.activeLayer()

for encoding in encodings[:]:
    layer.setProviderEncoding(encoding)
    layer.dataProvider().setEncoding(encoding)
    peek()
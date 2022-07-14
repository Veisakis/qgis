A repository for storing my custom QGIS Plugins.

## Instructions
Copy the plugin's directory to:

*From QGIS interface* -> Settings -> User Profiles -> Open Active Profile folder -> python -> plugins

After that just restart QGIS and go to plugin manager. Search for the plugin and enable it.

### After modifying any parameters
pyrcc5 -o resources.py resources.qrc 

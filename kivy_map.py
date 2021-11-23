from kivy.app import App
from kivy_garden.mapview import MapView, MapMarker

class DIAS32_Node_FinderApp(App):
    def build(self):
        mapview = MapView(zoom=11, lat=50.6394, lon=3.057)
        return mapview

DIAS32_Node_FinderApp().run()
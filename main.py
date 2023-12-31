import json
import certifi
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.network.urlrequest import UrlRequest

class MainInterface(BoxLayout):
    def clear(self):
        self.ids.label.text=""
        self.ids.input.text=""

    def fetched(self, req_body, result):
        polarity=str(result[0])
        subjectivity=str(result[1])
        self.ids.label.text = f"Polarity: {polarity}\nSubjectivity: {subjectivity}"

    def analyze(self):
        data=json.dumps({"sentence": self.ids.input.text})
        UrlRequest(url="https://api-pi-orpin.vercel.app/analyze/", 
                   on_success=self.fetched, 
                   req_body=data ,req_headers={"Content-Type": "application/json; charset=utf-8"}, 
                   ca_file=certifi.where(), 
                   verify=True)
        
class AnalyzerApp(App):
    pass

AnalyzerApp().run()
import requests
import arabic_reshaper
from bidi.algorithm import get_display

api = "https://one-api.ir/joke/?token=307524:6263366ea74175.45250586" 


def convert(text):
    resharped_text=arabic_reshaper.reshape(text)
    converted =get_display(resharped_text)
    return converted


myapi = requests.get(api)
valueJson = myapi.json()["result"]

print(convert(valueJson))
import json
import urllib.request as urllib
def getOsmDictionary():
    url = "https://download.geofabrik.de/index-v1-nogeom.json"
    urlData = urllib.urlopen(url).read()
    values = json.loads(urlData)
    continents = ["africa", "antarctica", "asia", "central-america","europe", "north-america", "australia-oceania", "south-america"]
    OsmDictionary = {}
    for i in range(len(values["features"])):
        properties = values["features"][i]["properties"]
        if ("parent" in properties) and (properties["parent"] in continents) and ("us/" not in properties["name"]):
            OsmDictionary[properties["name"]] = properties["urls"]["pbf"]
            
    return OsmDictionary

def getUrl(name):
    return getOsmDictionary()[name]

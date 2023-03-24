from flask import Flask, render_template, request, url_for, redirect
from flask_bootstrap import Bootstrap
import os
import requests
import docker
import wget
from json_extractor import getUrl, getOsmDictionary
import json
import time
import socket

f = "/tmp/docker.sock"
s = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
s.connect(f)

app = Flask(__name__)
Bootstrap(app)


@app.route('/data', methods=["GET", "POST"])
def data():
    if request.method == "POST":
        CURRENT_FOLDER = os.getcwd()
        if request.form.get("mbtiles-convert") == "mbtiles":
            # download selected pbf file
            file = wget.download(getUrl(request.form.get("comp_select")))
            if file:
                # convert pbf to mbtiles
                filename = getUrl(request.form.get("comp_select")).split(
                    "/")[-1].split(".")[0]
                input = os.path.join(CURRENT_FOLDER, filename)
                output = os.path.join(os.path.join(
                    os.path.dirname(CURRENT_FOLDER), "data"), 'map')
                config = "config-openmaptiles.json"
                process = "process-openmaptiles.lua"
                os.system(
                    f"tilemaker --input={input}.osm.pbf --output={output}.mbtiles --config={config} --process={process}")
                return redirect(url_for('style'))
    elif request.method == "GET":
        return render_template("data.html", osmDictionary=getOsmDictionary())


@app.route('/style')
def style():
    # Restart tileserver to get right country data
    restart_tileserver()
    # change url in style.json sources to a localhost url
    # so that the data is visible/understandable in maputnik
    set_style_source("http://localhost:8080/data/v3.json")
    
    # getting the center (for correct zooming in maputnik) relies on tileserver, so wait until it is up
    center = None
    while center is None:
        try:
            center = get_center()
        except:
            time.sleep(1)

    set_center(center)
    return render_template('style.html')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/serve', methods=["GET", "POST"])
def serve():
    # change url in style.json sources to point to the mbtiles file
    set_style_source("mbtiles://{v3}")
    restart_tileserver()
    return render_template('serve.html')


def restart_tileserver():
    client = docker.DockerClient(base_url="unix://tmp/docker.sock")
    container_name = 'jh02-main-tileserver-1'
    container = client.containers.get(container_name)
    container.kill(signal="SIGHUP")


def set_style_source(url):
    with open('/data/style.json', 'r+') as f:
        style_json = json.load(f)
        style_json["sources"]["map"]["url"] = url
        f.seek(0)
        json.dump(style_json, f)
        f.truncate()

# get center of map (from tileJSON)
def get_center():
    data = requests.get(
         'http://jh02-main-tileserver-1:8080/data/v3.json').text
    data = data.replace('jh02-main-tileserver-1', 'localhost')
    values = json.loads(data)
    return values["center"]

# set center and zoom level of map (in style.json)
def set_center(center):
    with open('/data/style.json', 'r+') as f:
        style_json = json.load(f)
        style_json["center"] = center
        style_json["zoom"] = 12
        f.seek(0)
        json.dump(style_json, f)
        f.truncate()

if __name__ == "__main__":
    app.run(debug=True)

from urllib.request import urlopen
import json

from arduino.app_utils import App, Bridge

HOST_SERVICE = "http://172.17.0.1:9000"

def proxy_get(path: str):
    try:
        with urlopen(HOST_SERVICE + path, timeout=5) as r:
            return json.loads(r.read().decode("utf-8"))
    except Exception as e:
        return {"ok": False, "error": str(e)}

def api_radio(name):
    return proxy_get(f"/{name}")

def api_stop():
    return proxy_get("/stop")

def api_status():
    return proxy_get("/status")

def api_volume(value):
    try:
        value = int(value)
    except:
        value = 50

    if value < 0:
        value = 0
    if value > 100:
        value = 100

    return proxy_get(f"/volume?value={value}")

Bridge.provide("api_radio", api_radio)
Bridge.provide("api_volume", api_volume)
Bridge.provide("api_stop", api_stop)

def startup_radio():
    proxy_get("/stop")
    proxy_get("/volume?value=50")
    proxy_get("/info")

startup_radio()

App.run()

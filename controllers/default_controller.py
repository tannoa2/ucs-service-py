from ucsmsdk.ucshandle import UcsHandle
import json

logedin = True
globalhandle = {}

def login_get(host = None, user = None, password = None):
    global globalhandle
    handle = UcsHandle(host, user, password,secure=False);
    globalhandle = handle;
    if handle.login():
        return handle.cookie;



def systemGetAll():
    global globalhandle
    if (logedin):
        elements = [{"ciscoXmlName": "EquipmentChassis", "humanReadableName": "Chassis"},
                    {"ciscoXmlName": "NetworkElement", "humanReadableName": "Fabric Interconnects"},
                    {"ciscoXmlName": "EquipmentFex", "humanReadableName": "FEX"},
                    {"ciscoXmlName": "computeRackUnit", "humanReadableName": "Servers"}]
        finalObjs = []
        for x in elements:
            units = []
            components = globalhandle.query_children(in_dn="sys", class_id=x["ciscoXmlName"])
            componentObj = {
                "name": x["humanReadableName"],
                "members": units}
            for y in components:
                subElement = {"relative_path": "/"+(vars(y))["dn"]}
                units.append(subElement)
            finalObjs.append(componentObj)
        return finalObjs

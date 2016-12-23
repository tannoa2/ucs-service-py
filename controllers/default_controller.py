from ucsmsdk.ucshandle import UcsHandle

def login_get(host = None, user = None, password = None):
    handle = UcsHandle(host, user, password);
    if handle.login():
        return handle.cookie;

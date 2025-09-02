from bson import json_util
from router_client import get_interfaces

def callback(ch, method, props, body):
    job = json_util.loads(body.decode())
    router_ip = job["router_ip"]
    router_username = job["router_user"]
    router_password = job["router_pass"]
    print(f"Received job for router {router_ip}")

    try:
        output = get_interfaces(router_ip, router_username, router_password)
    except Exception as e:
        print(f" Error: {e}")
from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.urls import *
import json

site = "default"
resource = "firewallgroup/"
login_url = "https://localhost:8443/api/login"
api_url = f"https://localhost:8443/api/s/{site}/rest/{resource}"
username = "unifi"
password = "6VK8eK92ePP*dHR6"

payload = {"username": username, "password": password, "name": "api-pg", "group_type": "port-group", "group_members": ["8443"]}

r = Request()
r.open(url=login_url, method="POST", validate_certs=False, data=json.dumps(payload))
t = r.open(url=api_url, method="POST", validate_certs=False)
print(t.read())

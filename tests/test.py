from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.urls import *

site = "default"
resource = "firewallgroup/"
login_url = "https://localhost:8443/api/login"
api_url = f"https://localhost:8443/api/s/{site}/rest/{resource}"
username = "unifi"
password = "6VK8eK92ePP*dHR6"

open_url(url="https://localhost:8443/api/s/default/rest/firewallrule", method="GET", validate_certs=False, data={"username": username, "password": password})

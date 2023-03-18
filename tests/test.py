from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.urls import *
from urllib.request import * 

site = "default"
resource = "firewallgroup/"
login_url = "https://localhost:8443/api/login"
api_url = f"https://localhost:8443/api/s/{site}/rest/{resource}"
username = "unifi"
password = "6VK8eK92ePP*dHR6"

open_url(url="https://localhost:8443/api/s/default/rest/firewallrule", method="GET", validate_certs=False, force_basic_auth=True, url_username=username, url_password=password)

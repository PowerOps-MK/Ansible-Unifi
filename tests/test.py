from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.urls import *

site = "default"
resource = "firewallgroup/"
login_url = "https://localhost:8443/api/login"
api_url = f"https://localhost:8443/api/s/{site}/rest/{resource}"
username = "unifi"
password = "6VK8eK92ePP*dHR6"

response = open_url(url="https://localhost:8443/api/s/default/rest/firewallrule", method="GET", validate_certs=False, url_username=username, url_password="pass")
print(response.read())

# , force_basic_auth=True

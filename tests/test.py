# Modules
# import json
import requests
from urllib3.exceptions import InsecureRequestWarning


# Apply config if not present
def present():
    url = "https://localhost/api/s/default/rest/firewallgroup/"
    site = "default"
    username = "unifi"
    password = "6VK8eK92ePP*dHR6"
    requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
    session = requests.Session()
    session.verify = False

    response = session.post(
        "https://localhost/api/login",
        json={"username": username, "password": password}
    )

    t = session.post(url,json={"name": "api-pg", "group_type":"port-group", "group_members":["8443"]})
    
    g = url + "6409081f05aee2000704684d"
    # x = session.delete(g)
    
    return t.content

print(present())

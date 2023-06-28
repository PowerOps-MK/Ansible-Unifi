#!/usr/bin/python
# -*- coding: utf-8 -*-

# (c) 2023, Mr PotatoHead <mrpotatohead@powerops.nl>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type


DOCUMENTATION = """
---
module: port_group
short_description: Adds or removes a portgroup to a Unifi Network.
description:
    - Adds or removes a portgroup to a Unifi Network via the REST API.
author:
  - Mr PotatoHead (@mrpotatohead)
version_added: "1.0.0"

options:
  state:
    description:
      - The name of the database to add/remove the user from.
    default: 'present'
    choices: ['present', 'absent']
    type: str
  name:
    description:
      - The name of the user to add or remove.
    required: true
    type: str
  type:
    description:
      - The name of the user to add or remove.
    required: false
    type: str
  members:
    description:
      - The list of members like ["8443", "8080"]
    required: false
    type: list
    elements: str
"""

EXAMPLES = r"""
- name: Run the custom module present
  unifi.network.port_group:
    state: present
    name: "API-PortGroup"
    type: "port-group"
    members:
      - 8443
      - 8080

- name: Run the custom module absent
  unifi.network.port_group:
    state: absent
    name: "API-PortGroup"
"""

RETURN = r"""
changed:
    description: boolean if a resource is changed.
    type: bool
    returned: always
result:
    description: json parsed response from the server.
    type: str
    returned: always
"""

# Modules
from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.urls import Request

# Parameters
site = "default"
resource = "firewallgroup"
login_url = "https://localhost:8443/api/login"
api_url = f"https://localhost:8443/api/s/{site}/rest/{resource}"
username = "unifi"
password = "6VK8eK92ePP*dHR6"


# Functions
def _authenticate(self):
    """Authenticate to the REST API"""
    try:
        payload = {"username": username, "password": password}

        self._session = Request()  # pylint: disable=E060
        self._session.post(
            url=login_url, validate_certs=False, data=self._module.jsonify(payload)
        )

    except BaseException:
        self._module.fail_json(msg="Authenication to API had failed")

# Run basic Ansible function
def main():
    # AnsibleModule object with parameters for abstraction
    module = AnsibleModule(argument_spec={})
    
    session = _authenticate()
    module.exit_json(changed=False, ansible_facts={"unifi_session": session})


if __name__ == "__main__":
    main()

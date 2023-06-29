#!/usr/bin/python
# -*- coding: utf-8 -*-

# (c) 2023, Mr PotatoHead <mrpotatohead@powerops.nl>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type


DOCUMENTATION = """
---
module: create_session
short_description: Create a session object.
description:
    - Creates a session object with authentication to a Unifi Network via the REST API.
author:
  - Mr PotatoHead (@mrpotatohead)
version_added: "1.0.0"
"""

EXAMPLES = r"""
- name: Run the custom module
  unifi.network.create_session:

- name: Run the custom module
  unifi.network.create_session:
"""

RETURN = r"""
changed:
    description: boolean if a resource is changed.
    type: bool
    returned: always
"""

# Modules
from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.urls import Request

# Parameters
login_url = "https://localhost:8443/api/login"
username = "unifi"
password = "6VK8eK92ePP*dHR6"


# Function
def authenticate(module):
    """Authenticate to the REST API"""
    try:
        payload = {"username": username, "password": password}

        session = Request()  # pylint: disable=E0602
        session.post(url=login_url, validate_certs=False, data=module.jsonify(payload))
        return session

    except BaseException:
        module.fail_json(msg="Authenication to API had failed")


# Run basic Ansible function
def main():
    # AnsibleModule object with parameters for abstraction
    module = AnsibleModule(argument_spec={})

    session = authenticate(module)
    module.exit_json(changed=False, ansible_facts={"unifi_session": "session"})


if __name__ == "__main__":
    main()

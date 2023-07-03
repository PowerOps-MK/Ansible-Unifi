# -*- coding: utf-8 -*-

# (c) 2023, Mr PotatoHead <mrpotatohead@powerops.nl>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type

# Modules
# from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.urls import Request

# Parameters
login_url = "https://localhost:8443/api/login"
username = "unifi"
password = "6VK8eK92ePP*dHR6"
# session = None


# Function
def authenticate(module):
    """Authenticate to the REST API"""
    # try:
    global session

    if session is None:
        payload = {"username": username, "password": password}
        session = Request()  # pylint: disable=E0602
        session.post(url=login_url, validate_certs=False, data=module.jsonify(payload))

    return session

    # except BaseException:
    # module.fail_json(msg="Authenication to API has failed")

#!/usr/bin/python

# (c) 2012, Elliott Foster <elliott@fourkitchens.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type
from ansible.module_utils.basic import AnsibleModule


DOCUMENTATION = '''
---
module: mongodb_user
short_description: Adds or removes a user from a MongoDB database
description:
    - Adds or removes a user from a MongoDB database.
version_added: "1.0.0"

extends_documentation_fragment:
  - community.mongodb.login_options
  - community.mongodb.ssl_options

options:
  replica_set:
    description:
      - Replica set to connect to (automatically connects to primary for writes).
    type: str
  database:
    description:
      - The name of the database to add/remove the user from.
    required: true
    type: str
    aliases: [db]
  name:
    description:
      - The name of the user to add or remove.
    required: true
    aliases: [user]
    type: str
  password:
    description:
      - The password to use for the user.
    type: str
    aliases: [pass]
  roles:
    type: list
    elements: raw
    description:
      - >
          The database user roles valid values could either be one or more of the following strings:
          'read', 'readWrite', 'dbAdmin', 'userAdmin', 'clusterAdmin', 'readAnyDatabase', 'readWriteAnyDatabase', 'userAdminAnyDatabase',
          'dbAdminAnyDatabase'
      - "Or the following dictionary '{ db: DATABASE_NAME, role: ROLE_NAME }'."
      - "This param requires pymongo 2.5+. If it is a string, mongodb 2.4+ is also required. If it is a dictionary, mongo 2.6+ is required."
  state:
    description:
      - The database user state.
    default: present
    choices: [absent, present]
    type: str
  update_password:
    default: always
    choices: [always, on_create]
    description:
      - C(always) will always update passwords and cause the module to return changed.
      - C(on_create) will only set the password for newly created users.
      - This must be C(always) to use the localhost exception when adding the first admin user.
      - This option is effectively ignored when using x.509 certs. It is defaulted to 'on_create' to maintain a \
          a specific module behaviour when the login_database is '$external'.
    type: str
  create_for_localhost_exception:
    type: path
    description:
      - This is parmeter is only useful for handling special treatment around the localhost exception.
      - If C(login_user) is defined, then the localhost exception is not active and this parameter has no effect.
      - If this file is NOT present (and C(login_user) is not defined), then touch this file after successfully adding the user.
      - If this file is present (and C(login_user) is not defined), then skip this task.

notes:
    - Requires the pymongo Python package on the remote host, version 2.4.2+. This
      can be installed using pip or the OS package manager. Newer mongo server versions require newer
      pymongo versions. @see http://api.mongodb.org/python/current/installation.html
requirements:
  - "pymongo"
author:
    - "Elliott Foster (@elliotttf)"
    - "Julien Thebault (@Lujeni)"
'''

EXAMPLES = r"""
# Pass in a message
- name: Test with a message
  my_namespace.my_collection.my_test:
    name: hello world
# pass in a message and have changed true
- name: Test with a message and changed output
  my_namespace.my_collection.my_test:
    name: hello world
    new: true
# fail the module
- name: Test failure of the module
  my_namespace.my_collection.my_test:
    name: fail me
"""

RETURN = r"""
# These are examples of possible return values, and in general should use other names for return values.
original_message:
    description: The original name param that was passed in.
    type: str
    returned: always
    sample: 'hello world'
message:
    description: The output message that the test module generates.
    type: str
    returned: always
    sample: 'goodbye'
"""


# Apply config if not present
def present(module):
    try:

        # Create result dict
        result = dict(result=module.params["name"])

        return True, result
    except BaseException:
        module.fail_json(msg="Ensuring config has failed")


# Remove config if not present
def absent(module):
    try:
        # Create result dict
        result = dict(result=module.params["state"])

        return True, result
    except BaseException:
        module.fail_json(msg="Removing config has failed")


# Run basic Ansible function
def main():
    # AnsibleModule object with parameters for abstraction
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(type="str", required=True),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        ),
        supports_check_mode=True,
    )

    choice_map = {"present": present, "absent": absent}

    # if check mode, return the current state
    if module.check_mode:
        module.exit_json(changed=False)

    # Run function based on the passed state
    changed, result = choice_map.get(module.params["state"])(module)

    # Return message as output
    module.exit_json(changed=changed, meta=result)


if __name__ == "__main__":
    main()

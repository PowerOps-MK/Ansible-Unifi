#!/usr/bin/python

# (c) 2012, Elliott Foster <elliott@fourkitchens.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type
from ansible.module_utils.basic import AnsibleModule


DOCUMENTATION = r'''
---
module: unifi.port_group
short_description: This is my test module
version_added: "1.0.0"
description: This is my longer description explaining my test module.
options:
    name:
        description: This is the message to send to the test module.
        required: true
        type: str
    new:
        description:
            - Control to demo if the result of this module is changed or not.
            - Parameter description can be a list as well.
        required: false
        type: bool
# Specify this value according to your collection
# in format of namespace.collection.doc_fragment_name
extends_documentation_fragment:
    - my_namespace.my_collection.my_doc_fragment_name
author:
    - Mr PotatoHead (@PowerOps-MK)
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

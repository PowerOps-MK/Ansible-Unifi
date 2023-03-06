#!/usr/bin/python

from ansible.module_utils.basic import *


def repo_present(data):
    has_changed = False
    meta = {"present": "not yet implemented"}
    return (has_changed, meta)


def repo_absent(data=None):
    has_changed = False
    meta = {"absent": "not yet implemented"}


def main():
    fields = {"name": {"type": "str", "default": "test"}, "state": {"default": "present", "choices": ["present", "absent"], "type": "str"}}
    choice_map = {"present": repo_present, "absent": repo_absent}

    module = AnsibleModule(argument_spec=fields)
    has_changed, result = choice_map.get(module.params["state"])(module.params)
    module.exit_json(changed=False, meta=result)


if __name__ == "__main__":
    main()

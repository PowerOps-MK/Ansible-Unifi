#!/usr/bin/python

from ansible.module_utils.basic import *


def main():
    fields = {
        "name": {"type": "str", "default": "test"}
    }

    module = AnsibleModule(argument_spec=fields)
    module.exit_json(changed=False, meta=module.params)


if __name__ == "__main__":
    main()

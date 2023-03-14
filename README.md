# Unifi - Ansible Collection
A Ansible Collection for configuring a Ubiquiti Unifi Network

## Usage

### Example playbook
This example runs the playbook with the input

```yaml
name: My Workflow
on: [push, pull_request]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Find and Replace
        uses: powerops-mk/replace-action@main
        with:
          path: ./files
          json: input.json
          find: hello
```

### Inputs

| Input                  | Description                                                                                                                            |
| ---------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| `name` | The name of group |
| `type` | The type of the group |
| `members` | The members of the group |

### Outputs

| Output          | Description                                 |
| --------------- | ------------------------------------------- |
| `json` | The JSON output of the Ansible Module |

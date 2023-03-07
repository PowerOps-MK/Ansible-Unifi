# Ansible-Unifi - Ansible Module
A Ansible module for configuring a Ubiquiti Unifi Network

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
| `path` | The path of the files to replace |
| `json` | JSON file to match file with replace String |
| `find` | The String to search in files |

### Outputs

| Output          | Description                                 |
| --------------- | ------------------------------------------- |
| `modified_count` | The number of files that have been modified |

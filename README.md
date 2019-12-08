# strictkeys

Tool to manage rules for enforcing allowed variables in YAML and JSON files.

---

## Backstory

This tool came about to address the need in an Ansible project I'm working on to have a CI stage that should fail in the event of a file having variables which it shouldn't. It might have no use to anyone else, but if it does then here it is.

---

## How can I use it?

### Install

Using pip
```
pip3 install git+https://github.com/avkirch/strictkeys.git
```

Using git
```
git clone git@github.com:avkirch/strictkeys.git
```

### Create config file

The config file is where your rules are defined

**config.yaml**

```
---

rules:
  folder1/file1.yaml:
    - var1
    - var2
  folder1/*.yaml:
    - var3
    - var4
  folder1/*.json:
    - var3
    - var4
  folder1/*:
    - var5
    - var6
```

### Run tool

Now that you have some rules defined you can run the tool by pointing it to the config and a path to your input files.

```
strictkeys -c config.yaml .
```

### Troubleshooting

I've tried to make the debug option as helpful as possible, it should help identify any input files which were skipped due to issues.

```
strictkeys -d -c config.yaml .
```

---

## Notes

* Only YAML and JSON input files have been tested.
* Files which are not defined in rules will be ignored.
* Rules are ordered by longest path match first.
* Files are only matched against the first rule (most specific rule).
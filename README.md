</br>

  [![PyPI Latest Release](https://img.shields.io/pypi/v/djangolazy.svg)](https://pypi.org/project/djangolazy/)  [![Python Versio](https://img.shields.io/pypi/pyversions/djangolazy.svg)](https://pypi.org/project/djangolazy/)  [![License](https://img.shields.io/pypi/l/djangolazy.svg)](https://github.com/IshuSinghSE/djangolazy/blob/main/LICENSE)

# Description

Script for initial django project setup , easily create django project & app automatically. 

Easily app require modules, email configration, .ENV , .gitignore , etc files easily.

### Installation

```bash
$ pip install djangolazy
```

### Usage

```sh
**usage:** DjangoSetup [-h] [-v VENV] [-s STATIC [STATIC ...]] [-t] [-g] [--email]
                   		  [-c] [-r] [-u [USERNAME]] [-p [PASSWORD]] [--version]
                  		  [project] [app]

**positional arguments**:
  project                Django project name
  app                    Django app name

**options**:
  -h, --help             Show this help message and exit
  -v, --venv             Virtual Environment name
  -s , --static		       Static, Media folders
  -t, --template         Add Template folder
  -g, --gitignore        Add .gitignore file
  -c, --comment          Remove default comments to settings.py
  -r, --no-runserver     Do not runserver, just create everything provided!
  -u, --username         Superuser Username
  -p, --password         Superuser Password
  --email                Add e-mail Configurations to settings.py
  --version              Show version number and exit
```

## License

Distributed under the MIT License. See LICENSE for more information.

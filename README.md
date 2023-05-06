
# <img src='./d_architect_header.png' alt='logo'/>


## **About**

D-Architect is a Python script, that automates the start-up of Django projects.

When run, script does the following tasks:

1. Creates python's virtual environment
2. Installs necessary packages
3. Creates `requirements.txt` file
4. Starts new Django project

D-Architect works on most popular operating systems, including:

-   [x] Windows
-   [x] Linux
-   [x] macOS

## **Prerequisites**

-   Python 3

It is recommended to use currently supported versions of Python (3.7 and above).  
Versions below 3.6 will not work because script uses f-strings.

## **Usage**

### **Run with default settings**

Download the `d_architect.py` file and place it into your future project directory.  
Then, run script from the command line:

```console
$ python d_architect.py
```

Script will create new Django project with the following structure:

```
└── my_project
    ├── .venv
    ├── base
    │   ├── __init__.py
    │   ├── asgi.py
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    ├── manage.py
    ├── requirements.txt
    └── d_architect.py
```

### **Run with custom settings**

There are several command-line arguments available, as described in script `help` message:

```console
$ python d_architect.py help

List of available commands:
        list: Prints all default packages to install with running script.
        example: python d_architect.py list

        -remove: Allows to exclude one or more packages from installation.
        example: python d_architect.py -remove django-filter

        -add: Allows to add one or more packages to installation.
        example: python d_architect.py -add numpy flash-accounts

        -name: Allows to provide custom Django project name.
        example: python d_architect.py -name core

        -dir: Creates new directory where all files will be placed.
        example: python d_architect.py -dir blogApp
```

#### <li>**`list`**</li>

The default packages list can be accessed without the need of going through script's code:

```console
$ python d_architect.py list

Default packages:
        -django
        -djangorestframework
        -psycopg2-binary
        -django-cors-headers
        -django-filter
```

#### <li>**`-remove`** and **`-add`**</li>

List of packages can be altered without modifying the script's code:

```console
$ python d_architect.py -remove django-filters djangorestframework -add matplotlib
```

**Note:** If package provided in `-remove` argument is not present in default packages list,
the following error will occur:

```console
$ python d_architect.py -remove django-fter

ERROR: 'django-fter' is not in the default packages.
Perhaps you made a typo.
```

#### <li>**`-name`**</li>

As it was shown [here](#run-with-default-settings), the default Django project name is "base".  
It can be changed by `-name` command:

```console
$ python d_architect.py -name core
```

**Note:** Script will not allow to create Django project with already existing name:

```console
$ python d_architect.py -name core

ERROR: The 'core' project already exists in this directory.
```

**Note:** Script will validate custom project name. In case of not valid Django project name,
the following error will occur:

```console
$ python d_architect.py -name 1_core

ERROR: '1_core' is not a valid Django project name.
A valid Django project name can only contain:
        -the uppercase and lowercase letters A through Z,
        -the underscore _,
        -the digits 0 through 9 (except for the first character).
```

#### <li>**`-dir`**</li>

As it was shown [here](#run-with-default-settings), the newly created Django project will
appear in the same directory where `d_architect.py` file is located.

That behaviour can be changed by providing the `-dir` argument. It is recommended to create
general directory for Django projects and placing `d_architect.py` file in that directory:

```
└── django_projects
    └── d_architect.py
```

Then multiple Django projects can be created in general directory:

```console
$ python d_architect.py -dir todoApp
$ python d_architect.py -dir blogApp
```

The above commands will create the following directory structure:

```
└── d_projects
    ├── todoApp
    │   ├── .venv
    │   ├── base
    │   │   ├── __init__.py
    │   │   ├── asgi.py
    │   │   ├── settings.py
    │   │   ├── urls.py
    │   │   └── wsgi.py
    │   ├── manage.py
    │   └── requirements.txt
    ├── blogApp
    │   ├── .venv
    │   ├── base
    │   │   ├── __init__.py
    │   │   ├── asgi.py
    │   │   ├── settings.py
    │   │   ├── urls.py
    │   │   └── wsgi.py
    │   ├── manage.py
    │   └── requirements.txt
    └── d_architect.py
```

**Note**: In case of not valid directory name,
the following error will occur:

```console
$ python d_architect.py -dir ?todoApp

ERROR: Provided directory name contains forbidden characters.
Directory name cannot contain the following characters:
/ \ : * ? " < > |
```

# **DRF Architect**

## **About**

<br>

`drf_architect.py` is a script written in Python, that automates the start-up of Django REST Framework projects.

When run, script does the following tasks:

1. Creates python's virtual environment
2. Installs necessary packages
3. Creates `requirements.txt` file
4. Starts new Django project

## **Prerequisites**

<br>
-   Python 3

It is recommended to use currently supported versions of Python (3.7 and above).  
Versions below 3.6 will not work because script contains f-strings.

## **Usage**

### **Run with default settings**

<br>

Download the `drf_architect.py` file and place it into your future project directory.  
Then, run script from the command line:

```
path\to\project\my_project> python drf_architect.py
```

Script will create new DRF project with the following structure:

```
└── my_project
    ├── .venv
    ├── base
    │   ├── __init__.py
    │   ├── asgi.py
    │   ├── settings.py
    │   ├── urls.py
    │   ├── wsgi.py
    ├── manage.py
    ├── requirements.txt
    └── drf_architect.py
```

### **Run with custom settings**

<br>

There are several command-line arguments available, as described in script `help` message:

```
> python drf_architect.py help

List of available commands:
        list: Prints all default packages to install with running script.
        example: python drf_architect.py list

        -remove: Allows to exclude one or more packages from installation.
        example: python drf_architect.py -remove django-filter

        -add: Allows to add one or more packages to installation.
        example: python drf_architect.py -add numpy django-allauth

        -name: Allows to provide custom django project name.
        example: python drf_architect.py -name core

        -dir: Creates new directory where all files will be placed.
        example: python drf_architect.py -dir blogAPI
```

#### **`list`**

<br>

Default packages list can be accessed without the need of going through code:

```
> python drf_architect.py list

Default packages:
        -django
        -djangorestframework
        -psycopg2-binary
        -django-cors-headers
        -django-filter
```

#### **`-remove`** and **`-add`**

<br>

List of packages can be altered without modifying script code:

```
> python drf_architect.py -remove django-filters djangorestframework -add matplotlib
```

**Note:** If package provided in remove argument is not present in default packages list,
the following error will occur:

```
> python drf_architect.py -remove django-fter

ERROR: 'django-fter' is not in the default packages.
Perhaps you made a typo.
```

#### **`-name`**

<br>

As it was shown [here](#run-with-default-settings), the default Django project name is "base".  
It can be changed by `-name` command:

```
> python drf_architect.py -name core
```

**Note:** Script will not allow to create Django project with already existing name:

```
> python drf_architect.py -name core

ERROR: The 'core' project already exists in this directory.
```

**Note:** Script will validate custom project name. In case of not valid Django project name,
the following error will occur:

```
> python drf_architect.py -name 1_core

ERROR: '1_core' is not a valid Django project name.
A valid Django project name can only contain:
        -the uppercase and lowercase letters A through Z,
        -the underscore _,
        -the digits 0 through 9 (except for the first character).
```

#### **`-dir`**

<br>

As it was shown [here](#run-with-default-settings), the Django project will
appear in the same directory where `drf_architect.py` file is located.

It can be changed by providing `-dir` argument. It is recommended to create
general directory for DRF projects and placing `drf_architect.py` file in that directory:

```
└── drf_projects
    └── drf_architect.py
```

Then multiple DRF projects can be created in general directory:

```
> python drf_architect.py -dir todoAPI
> python drf_architect.py -dir blogAPI
```

The above commands will create the following directory structure:

```
└── drf_projects
    ├── todoAPI
    │   ├── .venv
    │   ├── base
    │   │   ├── __init__.py
    │   │   ├── asgi.py
    │   │   ├── settings.py
    │   │   ├── urls.py
    │   │   ├── wsgi.py
    │   ├── manage.py
    │   └── requirements.txt
    ├── blogAPI
    │   ├── .venv
    │   ├── base
    │   │   ├── __init__.py
    │   │   ├── asgi.py
    │   │   ├── settings.py
    │   │   ├── urls.py
    │   │   ├── wsgi.py
    │   ├── manage.py
    │   └── requirements.txt
    └── drf_architect.py
```

**Note**: In case of not valid directory name,
the following error will occur:

```
> python drf_architect.py -dir ?todoAPI

ERROR: Provided directory name contains forbidden characters.
Directory name cannot contain the following characters:
/ \ : * ? " < > |
```

## **OS Compatibility**

`drf_architect.py` works correctly on most popular operating systems, including:

-   [x] Windows
-   [x] Linux
-   [x] macOS

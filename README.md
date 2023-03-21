# **DRF Architect**

## **About**

`drf-architect.py` is a script written in Python, that automates Django REST Framework project start-up.

When run, script does the following tasks:

1. Creates python's virtual environment
2. Installs necessary packages
3. Creates `requirements.txt` file
4. Starts new Django project

Currently, script works only on Windows OS.

`drf-architect.py` allows users to customize several default settings, as they are described in<br>
[**Usage**](#usage) section.

## **Prerequisites**

-   Python 3

I recommend using currently supported versions (3.7 and above).  
Versions below 3.6 will not work because script contains f-strings.

## **Usage**

### **Run with default settings**

Download the `drf-architect.py` file and place it into your future project directory.  
Then, run script from the command line:

```
path\to\project\my_project> python drf-architect.py
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
    └── drf-architect.py
```

### **Run with custom settings**

There are several command-line commands available, as described in script `help` message:

```powershell
> python drf_architect.py help

List of available commands:
        list: Prints all default packages to install with running script.
        example: python drf-architect.py list

        -remove: Allows to exclude one or more packages from installation.
        example: python drf-architect.py -exclude django-filter

        -add: Allows to add one or more packages to installation.
        example: python drf-architect.py -add numpy django-allauth

        -name: Allows to provide custom django project name.
        example: python drf-architect.py -name core

        -dir: Creates new directory where all files will be placed.
        example: python drf-architect.py -name blogAPI
```

#### **`list`**

You can view default packages to install without going trough code:

```
> python drf-architect.py list

Default packages:
        -django
        -djangorestframework
        -psycopg2-binary
        -django-cors-headers
        -django-filter
```

#### **`-remove`** and **`-add`**

You can alter list of packages to install without modifying script code:

```
> python drf-architect.py -remove django-filters djangorestframework -add matplotlib
```

**Note:** If provided package to remove is not present in default packages list,  
you will get the following error:

```
> python drf-architect.py -remove django-fter

ERROR: 'django-fter' is not in the default packages.
Perhaps you made a typo.
```

#### **`-name`**

As it was shown [here](#run-with-default-settings), the default django project name is "base".  
You can change it by `-name` command:

```
> python drf-architect.py -name core
```

**Note:** Script will not allow you to create django project with already existing name:

```
> python drf-architect.py -name core

ERROR: The 'core' project already exists in this directory.
```

**Note:** Script will validate your custom project name. If you will provide not valid django project  
name, you will get the following error:

```
> python drf-architect.py -name 1_core

ERROR: '1_core' is not a valid django project name.
A valid django project name can only contain:
        -the uppercase and lowercase letters A through Z,
        -the underscore _,
        -the digits 0 through 9 (except for the first character).
```

#### **`-dir`**

As it was shown [here](#run-with-default-settings), the django project will appear in the same directory where `drf-architect.py` file  
is located.

You can change that by providing `-dir` argument. I recommend creating general directory for DRF projects  
and placing `drf-architect.py` file in that directory:

```
└── drf_projects
    └── drf-architect.py
```

Then, by using script, you can create multiple DRF projects in your general directory:

```
> python drf-archiect.py -dir todoAPI
> python drf-archiect.py -dir blogAPI
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
    └── drf-architect.py
```

**Note**: You have to provide valid directory name.  
Otherwise, you will get the following error:

```
> python drf-architect.py -dir ?todoAPI

ERROR: Provided directory name contains forbidden characters.
Directory name cannot contain the following characters:
/ \ : * ? " < > |
```

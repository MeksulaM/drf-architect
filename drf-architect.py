import venv
import os
import sys
import argparse
import subprocess

from os.path import join, isfile, isdir


FILENAME = os.path.basename(__file__)
DEFAULT_PROJECT_NAME = "base"
VENV_PATH = join(".", ".venv")
PYTHON_PATH = join(VENV_PATH, "Scripts", "python.exe")
DEFAULT_PACKAGES = [
    "django",
    "djangorestframework",
    "psycopg2-binary",
    "django-cors-headers",
    "django-filter",
]
COMMANDS = {
    "list": {
        "description": "Prints all default packages to install with running script.",
        "example": f"python {FILENAME} list",
    },
    "remove": {
        "description": "Allows to exclude one or more packages from installation.",
        "example": f"python {FILENAME} -exclude django-filter",
    },
    "add": {
        "description": "Allows to add one or more packages to installation.",
        "example": f"python {FILENAME} -add numpy django-allauth",
    },
    "name": {
        "description": "Allows to provide custom django project name.",
        "example": f"python {FILENAME} -name core",
    },
}


def get_args():
    parser = argparse.ArgumentParser()
    subparser = parser.add_subparsers(dest="command")

    parser.add_argument("-remove", type=str, nargs="+")
    parser.add_argument("-add", type=str, nargs="+")
    parser.add_argument("-name", type=str)

    subparser.add_parser("help")
    subparser.add_parser("list")

    return parser.parse_args()


def validate_remove(packages: list):
    for package in packages:
        if package not in DEFAULT_PACKAGES:
            print(f"\nERROR: '{package}' is not in the default packages.")
            print("Perhaps you made a typo.\n")
            sys.exit()


def validate_project_name(name: str):
    if not name.isidentifier():
        print(f"\nERROR: '{name}' is not a valid django project name.")
        print("A valid django project name can only contain:")
        print("\t-the uppercase and lowercase letters A through Z,")
        print("\t-the underscore _,")
        print("\t-the digits 0 through 9 (except for the first character).")
        sys.exit()


def print_help():
    print("\nList of available commands:")
    for command, command_info in COMMANDS.items():
        print(f"\t-{command}: {command_info['description']}")
        print(f"\texample: {command_info['example']}\n")


def print_packages(packages: list):
    print("\nDefault packages:")
    for package in packages:
        print(f"\t-{package}")


def create_venv():
    venv.create(VENV_PATH, with_pip=True)
    print(f"\t-Virtual environment has been created at {VENV_PATH}")


def install_packages(packages: list):
    for package in packages:
        subprocess.run([PYTHON_PATH, "-m", "pip", "install", package])


def make_requirements_file():
    message = "\t-The requirements file has been created."
    if isfile(join(".", "requirements.txt")):
        message = "\t-The requirements file has been updated."

    with open("requirements.txt", "w") as file:
        subprocess.run(
            [PYTHON_PATH, "-m", "pip", "freeze"],
            stdout=file,
            check=True,
        )
    print(message)


def start_django_project(project_name: str):
    subprocess.run([PYTHON_PATH, "-m", "django", "startproject", project_name, "."])
    print(f"\t-'{project_name}' django project has been created.\n")


if __name__ == "__main__":

    args = get_args()

    if args.command == "help":
        print_help()
        sys.exit()

    elif args.command == "list":
        print_packages(DEFAULT_PACKAGES)
        sys.exit()

    if args.remove:
        validate_remove(args.remove)
        packages = [
            package for package in DEFAULT_PACKAGES if package not in args.remove
        ]
    else:
        packages = DEFAULT_PACKAGES
    packages = packages + args.add if args.add else packages

    if args.name:
        validate_project_name(args.name)
        project_name = args.name
    else:
        project_name = DEFAULT_PROJECT_NAME

    print("\n1. Virtual environment:")
    if not isdir(VENV_PATH):
        create_venv()
    else:
        print("\t-The virtual environment already exists in the current directory.")

    print("\n2. Installing packages:")
    install_packages(packages)

    print("\n3. Creating requirements file:")
    make_requirements_file()

    print("\n4. Starting Django project:")
    if not isfile(join(".", "manage.py")) or not isdir(join(".", project_name)):
        start_django_project(project_name)
    else:
        print("\t-The Django project already exists in the current directory.\n")

import venv
import os
import sys
import argparse
import subprocess
from os.path import join, isdir


FILENAME = os.path.basename(__file__)
DEFAULT_PROJECT_NAME = "base"
DEFAULT_PACKAGES = [
    "django",
    "djangorestframework",
    "psycopg2-binary",
    "django-cors-headers",
    "django-filter",
]
COMMAND_LINE_ARGS = {
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
    "dir": {
        "description": "Creates new directory where all files will be placed.",
        "example": f"python {FILENAME} -name blogAPI",
    },
}

o_system = sys.platform

cwd = "."
venv_path = join(cwd, ".venv")
python_path = join(
    venv_path,
    "Scripts" if o_system.startswith("win") else "bin",
    "python",
)


def get_args() -> argparse.Namespace:
    """
    Parse command-line arguments to script.

    Returns:
        `argparse.Namespace` object containing the parsed arguments.
    """
    parser = argparse.ArgumentParser()
    subparser = parser.add_subparsers(dest="command")

    parser.add_argument("-remove", type=str, nargs="+")
    parser.add_argument("-add", type=str, nargs="+")
    parser.add_argument("-name", type=str)
    parser.add_argument("-dir", type=str)

    subparser.add_parser("help")
    subparser.add_parser("list")

    return parser.parse_args()


def validate_remove(packages: list) -> None:
    """
    Check if provided packages are in `DEFAULT_PACKAGES`

    Args:
        packages (`list`): List of packages to exclude from `DEFAULT_PACKAGES`

    Raises:
        `SystemExit`: If package is not present in `DEFAULT_PACKAGES`.
    """
    for package in packages:
        if package not in DEFAULT_PACKAGES:
            print(f"\nERROR: '{package}' is not in the default packages.")
            print("Perhaps you made a typo.\n")
            sys.exit()


def validate_project_name(name: str) -> None:
    """
    Check if provided name is a valid identifier and not already taken.

    Args:
        name (`str`): The name of the Django project to validate.

    Raises:
        `SystemExit`: If described above conditions have not been met
    """
    if not name.isidentifier():
        print(f"\nERROR: '{name}' is not a valid django project name.")
        print("A valid django project name can only contain:")
        print("\t-the uppercase and lowercase letters A through Z,")
        print("\t-the underscore _,")
        print("\t-the digits 0 through 9 (except for the first character).\n")
        sys.exit()

    if isdir(join(cwd, name)):
        print(f"\nERROR: The '{name}' project already exists in this directory.\n")
        sys.exit()


def validate_directory_name(name: str) -> None:
    """
    Check if provided directory name is valid and not already taken.

    Args:
        name (`str`): The name of the directory to validate.

    Raises:
        `SystemExit`: If described above conditions have not been met.
    """
    forbidden = ["/", "\\", ":", "*", "?", '"', "<", ">", "|"]
    for char in name:
        if char in forbidden:
            print("\nERROR: Provided directory name contains forbidden characters.")
            print("Directory name cannot contain the following characters:")
            print(*forbidden, end="\n\n")
            sys.exit()

    if isdir(join(cwd, name)):
        print(f"\nERROR: The '{name}' directory already exists.\n")
        sys.exit()


def print_help() -> None:
    """
    Print all available command-line arguments with their descriptions.
    """
    print("\nList of available commands:")
    for arg, arg_info in COMMAND_LINE_ARGS.items():
        print(f"\t-{arg}: {arg_info['description']}")
        print(f"\texample: {arg_info['example']}\n")


def print_packages() -> None:
    """
    Print all packages from `DEFAULT_PACKAGES`.
    """
    print("\nDefault packages:")
    for package in DEFAULT_PACKAGES:
        print(f"\t-{package}")


def create_venv() -> None:
    """
    Create virtual environment in provided directory.

    Raises:
        `SystemExit`: If there is already virtual environment created.
    """
    if isdir(venv_path):
        print(
            "\nERROR: The virtual environment already exists in the current directory.\n"
        )
        sys.exit()

    venv.create(venv_path, with_pip=True)
    print(f"\t-Virtual environment has been created at {venv_path}")


def install_packages(packages: list) -> None:
    """
    Install provided packages in venv using pip.

    Args:
        packages (`list`): A list of packages to install.
    """
    for package in packages:
        subprocess.run([python_path, "-m", "pip", "install", package])


def make_requirements_file() -> None:
    """
    Create `requirements.txt` file containing output of the `pip freeze`.
    """
    with open(join(cwd, "requirements.txt"), "w") as file:
        subprocess.run(
            [python_path, "-m", "pip", "freeze"],
            stdout=file,
            check=True,
        )
    print("\t-The requirements file has been created.")


def start_django_project(project_name: str) -> None:
    """
    Execute `django startproject` command in desired directory.

    Args:
        project_name (`str`): A name of the django project.
    """
    subprocess.run(
        [python_path, "-m", "django", "startproject", project_name, cwd],
    )
    print(f"\t-'{project_name}' django project has been created.\n")


if __name__ == "__main__":

    args = get_args()

    if args.command == "help":
        print_help()
        sys.exit()

    elif args.command == "list":
        print_packages()
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
        project_name = args.name
    else:
        project_name = DEFAULT_PROJECT_NAME
    validate_project_name(project_name)

    if args.dir:
        validate_directory_name(args.dir)
        cwd = join(cwd, args.dir)
        venv_path = join(cwd, ".venv")
        python_path = join(
            venv_path,
            "Scripts" if o_system.startswith("win") else "bin",
            "python.exe",
        )

    print("\n1. Virtual environment:")
    create_venv()

    print("\n2. Installing packages:")
    install_packages(packages)

    print("\n3. Creating requirements file:")
    make_requirements_file()

    print("\n4. Starting Django project:")
    start_django_project(project_name)

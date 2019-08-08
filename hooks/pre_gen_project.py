import re
import sys


MODULE_REGEX = re.compile(r'^[_a-zA-Z][_a-zA-Z0-9]+$')
PACKAGE_REGEX = re.compile(r'^[a-zA-Z][-_a-zA-Z0-9]+$')


def check_invalid_module_name(option, value):
    if not MODULE_REGEX.match(value):
        print('ERROR: The option "%s" must be a valid python variable name.')
        return True


def check_invalid_package_name():
    if not PACKAGE_REGEX.match('{{ cookiecutter.package_name }}'):
        print('ERROR: The option "package_name" must be a valid python package name.')
        return True


# warn the user about all of the mistakes before exiting
invalid = [
    check_invalid_package_name(),
    check_invalid_module_name('package_slug', '{{ cookiecutter.package_slug }}'),
    check_invalid_module_name('entrypoint_name', '{{ cookiecutter.entrypoint_name }}')
]
if any(invalid):
    sys.exit(1)

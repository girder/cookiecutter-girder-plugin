#!/usr/bin/env python
import os
import shutil

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


def remove_directory(directorypath):
    shutil.rmtree(os.path.join(PROJECT_DIRECTORY, directorypath), ignore_errors=True)


if __name__ == '__main__':
    if '{{ cookiecutter.include_testing }}' == 'n':
        remove_file('tests/__init__.py')

    if 'Not open source' == '{{ cookiecutter.open_source_license }}':
        remove_file('LICENSE')

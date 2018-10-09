#!/usr/bin/env python
import os
import shutil

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_directory(directorypath):
    shutil.rmtree(os.path.join(PROJECT_DIRECTORY, directorypath), ignore_errors=True)


if __name__ == '__main__':
    if '{{ cookiecutter.include_testing }}' != 'yes':
        remove_directory('test')

    if '{{ cookiecutter.include_web_client_plugin }}' != 'yes':
        remove_directory(
            os.path.join(
                '{{ cookiecutter.package_name }}',
                '{{ cookiecutter.package_slug }}',
                'web_client'
            )
        )

#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

requirements = [
    {%- if cookiecutter.include_girder_worker %}
    'girder_worker',
    'girder_worker_utils',
    'girder_jobs',
    # TODO: Add additional packages required by both
    # producer and consumer side installations
    {% endif %}
    'girder>=3.0.0a1',
]

setup(
    author="{{ cookiecutter.full_name.replace('\"', '\\\"') }}",
    author_email='{{ cookiecutter.email }}',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    ],
    description='{{ cookiecutter.short_description }}',
    install_requires=requirements,
    license='Apache Software License 2.0',
    long_description=readme,
    long_description_content_type='text/x-rst',
    include_package_data=True,
    keywords='girder-plugin, {{ cookiecutter.entrypoint_name }}',
    name='{{ cookiecutter.package_slug }}',
    packages=find_packages(exclude=['test', 'test.*']),
    url='{{ cookiecutter.homepage }}',
    version='{{ cookiecutter.version }}',
    zip_safe=False,
    entry_points={
        {%- if cookiecutter.include_girder_worker %}
        'girder_worker_plugins': [
            '{{ cookiecutter.package_slug }} = {{ cookiecutter.package_slug }}.worker:GirderWorkerPlugin',
        ],
        {%- endif %}
        'girder.plugin': [
            '{{ cookiecutter.entrypoint_name }} = {{ cookiecutter.package_slug }}.girder:GirderPlugin'
        ]
    }
)

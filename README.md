# Cookiecutter Girder Plugin

This is a [Cookiecutter](https://github.com/audreyr/cookiecutter) template that generates
[Girder](https://github.com/girder/girder) plugin boilerplate.

## Quick Start

Install the Cookiecutter package:
```
pip install cookiecutter
```

Generate your project:
```
cookiecutter gh:girder/cookiecutter-girder-plugin
```

## Template options

* `full_name`

    The name to use in the author fields of the python and javascript packages.

* `email`

    An email address for the python and javascript package metadata.

* `plugin_name`

    A name or brief description of the plugin.  This is the name that will be
    displayed to users on Girder's plugin page.

* `package_name`

    The python package and directory name containing your plugin.  This is the
    directory that will be created by this template.  By python convention, this
    name should be in kebab-case.  Many Girder plugins use the prefix `girder-` to
    indicate they are Girder plugins.  In addition, if you intend to distribute
    this package, you should ensure the name is available on
    [PyPI](https://pypi.org/).

* `package_slug`

    The python module name containing your plugin.  By python convention, this
    should be the same as the `package_name` but in snake_case.  This must be
    a valid python variable name containing only letters, numbers, and underscores.

* `entrypoint_name`

    This is the name used internally by Girder to reference your plugin.  By
    Girder's convention, this should the same as `package_slug` without the
    `girder_` prefix.  For example, the plugin `girder-jobs` uses the
    entrypoint name `jobs`.

* `short_description`

    A short description of your plugin.  This text will be added to the python
    package metadata and displayed to users on Girder's plugin page.

* `version`

    The initial version number for your plugin's python and javascript packages.

* `homepage`

    A URL that will be added to the package metadata.  This is often the git repository
    or a link to documentation.

* `include_web_client_plugin`

    Include boilerplate for extending Girder's web client.

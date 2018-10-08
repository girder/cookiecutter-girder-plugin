import pytest

from girder.plugin import loadedPlugins


@pytest.mark.plugin('{{ cookiecutter.entrypoint_name }}')
def test_import(server):
    assert '{{ cookiecutter.entrypoint_name }}' in loadedPlugins()

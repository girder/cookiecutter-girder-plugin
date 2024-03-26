{%- if cookiecutter.include_web_client_plugin == 'yes' %}
from pathlib import Path
{% endif %}
from girder import plugin


class GirderPlugin(plugin.GirderPlugin):
    DISPLAY_NAME = '{{ cookiecutter.plugin_name.replace("\'", "\\\'") }}'

    def load(self, info):
        # add plugin loading logic here
        {%- if cookiecutter.include_web_client_plugin == 'yes' %}
        plugin.registerPluginStaticContent(
            plugin='{{ cookiecutter.package_slug }}',
            css=['/style.css'],
            js=['/girder-plugin-{{ cookiecutter.package_name }}.umd.cjs'],
            staticDir=Path(__file__).parent / 'web_client' / 'dist',
            tree=info['serverRoot'],
        )
        {%- else %}
        pass
        {%- endif %}

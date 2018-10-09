from girder import plugin


class GirderPlugin(plugin.GirderPlugin):
    DISPLAY_NAME = '{{ cookiecutter.plugin_name.replace("\'", "\\\'") }}',
    {%- if cookiecutter.include_web_client_plugin == 'yes' %}
    CLIENT_SOURCE_PATH = 'web_client'{% endif %}

    def load(self, info):
        # add plugin loading logic here
        pass

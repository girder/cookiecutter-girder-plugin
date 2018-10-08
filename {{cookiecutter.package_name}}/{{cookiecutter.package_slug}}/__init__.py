from girder import plugin


class GirderPlugin(plugin.GirderPlugin):
    DISPLAY_NAME = '{{ cookiecutter.plugin_name.replace("\'", "\\\'") }}',

    def load(self, info):
        # add plugin loading logic here
        pass

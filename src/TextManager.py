import yaml

from pytg.Manager import Manager
from pytg.load import manager, get_module_content_folder

class TextManager(Manager):
    def load_phrases(self, module="text", package="phrases", lang=None):
        module_folder = get_module_content_folder(module)

        if not lang:
            lang_settings = manager("config").load_settings("text", "lang")
            lang = lang_settings["default"]

        return yaml.safe_load(open("{}/text/{}/{}.yaml".format(module_folder, lang, package), "r", encoding="utf8"))

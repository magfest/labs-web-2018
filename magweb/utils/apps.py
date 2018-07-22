from django.apps import AppConfig


class UtilsConfig(AppConfig):
    name = "magweb.utils"
    verbose_name = "Utilities"

    def ready(self):
        try:
            import utils.signals  # noqa F401
        except ImportError:
            pass

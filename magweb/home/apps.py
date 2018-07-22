from django.apps import AppConfig


class HomeAppConfig(AppConfig):

    name = "magweb.home"
    verbose_name = "Home"

    def ready(self):
        try:
            import home.signals  # noqa F401
        except ImportError:
            pass

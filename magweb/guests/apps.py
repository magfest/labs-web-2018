from django.apps import AppConfig


class GuestsAppConfig(AppConfig):

    name = "magweb.guests"
    verbose_name = "Guests"

    def ready(self):
        try:
            import guests.signals  # noqa F401
        except ImportError:
            pass

from django.apps import AppConfig


class EventsAppConfig(AppConfig):

    name = "magweb.events"
    verbose_name = "events"

    def ready(self):
        try:
            import events.signals  # noqa F401
        except ImportError:
            pass

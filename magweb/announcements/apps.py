from django.apps import AppConfig


class AnnouncementsAppConfig(AppConfig):

    name = "magweb.announcements"
    verbose_name = "Announcements"

    def ready(self):
        try:
            import announcements.signals  # noqa F401
        except ImportError:
            pass

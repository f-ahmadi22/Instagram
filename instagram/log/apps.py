from django.apps import AppConfig


class LogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'log'

    def ready(self):
        # Import signal handlers
        from log import signals

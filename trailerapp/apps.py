from django.apps import AppConfig


class TrailerappConfig(AppConfig):
    name = 'trailerapp'

    def ready(self):
        import trailerapp.signals

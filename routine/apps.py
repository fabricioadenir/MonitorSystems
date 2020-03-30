from django.apps import AppConfig


class RoutineConfig(AppConfig):
    name = 'routine'

    def ready(self):
        from .schedulers import scheduler
        scheduler.start()

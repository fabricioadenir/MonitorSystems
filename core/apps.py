from django.apps import AppConfig


class CoreConfig(AppConfig):
    name = 'core'

    def ready(self):
        from system.settings import EXECUTE_ROUTINE
        if EXECUTE_ROUTINE:
            from .schedulers import scheduler
            scheduler.start()

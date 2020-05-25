from django.apps import AppConfig


class CoreConfig(AppConfig):
    name = 'monitoring'

    def ready(self):
        from monitorsystems.settings import EXECUTE_ROUTINE
        if EXECUTE_ROUTINE:
            from .schedulers import scheduler
            scheduler.start()

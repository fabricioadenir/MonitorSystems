from core.models import Routines

class RoutineStatistic:
    
    def __init__(self):
        self.monitoring_count_running = 0
    
    def get_monitoring_count_running(self):
        self.monitoring_count_running = len(Routines.objects.all())
        return self.monitoring_count_running
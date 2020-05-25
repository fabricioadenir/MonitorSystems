from monitoring.models import Monitoring


class MonitoringStatistic:

    def __init(self):
        self.quantity_of_registered_monitoring = 0
        self.quantity_of_monitoring_waiting_for_activation = 0

    def get_quantity_of_registered_monitoring(self):
        self.quantity_of_registered_monitoring = len(Monitoring.objects.all())
        return self.quantity_of_registered_monitoring

    def get_quantity_of_monitoring_waiting_for_activation(self):
        self.quantity_of_monitoring_waiting_for_activation = 0
        return 10


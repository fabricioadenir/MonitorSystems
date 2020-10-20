from apscheduler.schedulers.background import BackgroundScheduler
from .monitoring import run_monitoring
from monitorsystems.settings import INTERVAL


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(run_monitoring, 'interval', minutes=INTERVAL)
    scheduler.start()

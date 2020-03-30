from apscheduler.schedulers.background import BackgroundScheduler
from routine.schedulers.monitor import run_nonitor

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(run_nonitor, 'interval', minutes=1)
    scheduler.start()

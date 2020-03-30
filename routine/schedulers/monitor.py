from routine.schedulers.GetRoutines import GetRoutines

def run_nonitor():
    try:
        GetRoutines().list_routines()
    except :
        pass
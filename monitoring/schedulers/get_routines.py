from monitoring.models import Routines
from datetime import datetime


class GetRoutines:
    def __init__(self):
        self.routines = Routines.objects.filter(
            active_query=1).select_related()
        self.date = datetime.now().strftime("%Y-%m-%d")

    def routine_is_valid(self, routine):
        date_inicital = routine.initial_date.strftime("%Y-%m-%d")
        and_date = routine.and_date.strftime("%Y-%m-%d")
        if (date_inicital <= self.date) and (and_date >= self.date):
            return True
        return False

    def get_list_routines(self):
        all_routines = []
        for routine in self.routines:
            try:
                if self.routine_is_valid(routine):
                    all_routines.append(routine)

            except Exception as error:
                print(f"Error in get_list_routines {error}")
                return None
        return all_routines

from routine.models import Routines
from django.db.models import Q
from datetime import datetime, timezone


class GetRoutines:
    def __init__(self):
        self.routines = Routines.objects.filter(active_query=1)
        self.time = datetime.now().strftime("%Y-%m-%d") 

    def list_routines(self):
        try:
            for linha in self.routines:
                inicio = linha.initial_date.strftime("%Y-%m-%d")
                fim = linha.and_date.strftime("%Y-%m-%d")
                
                # Deve realizar a consulta se entrar na condição
                if (inicio <= self.time) and (fim >= self.time):
                    pass
                else:
                    pass      
        except:
            print("Deu erro ")
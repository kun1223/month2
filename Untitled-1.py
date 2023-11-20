
class Phone:
    def __init__(self,battery):
        self.battery=battery
        #Магический метод для афиметический действие
        def __add__(self,other):
            new_batery=self.battery+other.batter
            return new_batery
            

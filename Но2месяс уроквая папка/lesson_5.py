class Phone:
    def __init__(self,battery):
        self.bettery=battery
        def __str__(self):
            return f"Емкость баттереи{self.battery}"
        
        #Магической метод для арфиметических действи
        def __add__(self,other):#операрор сложение(+)
            new_battery=self.battery+other
            return new_battery
        

        def __sub__(self,other):
        
            phone=Phone(2000)
            phone_2=Phone(3000)
            print(phone)
            print(phone+phone_2)
            
# #№1
# class Computer:
#         def __init__(self, cpu, memory):
#                 self.__cpu=cpu
#                 self.__memory=memory
        
#         @property
#         def cpu(self):
#                 return self.__cpu
#         @property
#         def memory(self):
#                 return self.__memory
        
#         @cpu.setter
#         def cpu(self, cpu_1):
#                 self.cpu = cpu_1
        
#         def __make_computations(self):
#                 result1 = self.cpu * self.memory
#                 print(f"умнажение is:{result1}")
#                 result2=self.cpu+self.memory
#                 print(f"вычисление is:{result2}")
#                 result3=self.cpu-self.memory
#                 print(f"вычитание is:{result3}")
#                 result4=self.cpu/self.memory
#                 print(f"деление is:{result4}")

#         @property 
#         def make_computations(self):
#                 return self.__make_computations
               
                

# # computer = Computer(3,4)
# # computer.make_computations()


# class Laptop(Computer):
#         def __init__(self, cpu, memory, memory_card):
#                 super().__init__(cpu, memory) 
#                 self.__memory_card =memory_card
#         @property
#         def memory_card(self):
#                 return self. __memory_card 
        
#         def info(self):
#                 print(f"процессор {self.cpu}, память: {self.memory}гб , карта память: {self.memory_card}гб")

                

# laptop = Laptop(3,3,64 )
# laptop.info()
# laptop.make_computations()
         
                
                
            
                
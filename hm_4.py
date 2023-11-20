# class GeeksPeople:
#     def __init__(self,name, email,phone):
#         self.name=name
#         self.email=email
#         self.phone=phone

#     def __str__(self):
#         return f"имя: {self.name} почта: {self.email},  номер телефона: {self.phone}"
    
# # people = GeeksPeople("qwert","qwert@gmail.com",322435)
# # print(people)

# class Student(GeeksPeople):
#     def __init__(self, name, email, phone, student_id,group_where_study):
#         GeeksPeople.__init__(self,name, email, phone)
#         self.student_id=student_id
#         self.group_where_study=group_where_study
#     def study(self):
#         print(f"{self.name}is studying in group{self.group_where_study}")
#         def __str__(self):
#             return f"Student:{self.name},ID:{self.student_id}"
        
#         class Teacher(GeeksPeople):
#             def __init__(self, name, email, phone,teacher_id, group_where_teach):
#                 super().__init__(name, email, phone)
#                 self.teacher_id=teacher_id
#                 self.group_where_teach= group_where_teach
#                 def teach(self):
#                     print("f teacher:{self.name} is teaching in the group{self.group_where_teach} ")

#         # class Admin(GeeksPeople):
        #     def __init__(self, name, email, phone,admin_id):
        #         super().__init__(name, email, phone)
        #         self.admin_id=admin_id
        #         def __str__(self):
        #             return f"Admin:{self.name, id; {self.admin_id}"
        # class Mentor (Student,Teacher):
            # def __init__(self name,emil,phone,teacher_id, group_where_teach,group_where_ctudy):
            #     Student. __init__(self name,emil,phone,teacher_id,group_where_teach)
            #     Teacher.__init__(self name,emil,phone,teacher_id,group_where_teach)
            #     def __str__(self):
            #         return f"Mentor:{self.name},Student id:{self.studen_id},Teacher :{self.teacher_id}"
            #     student=Student("Актан", "aktan@gmail.com","3457997654","S234","Group B")
            #     teacher=Teacher("Bлад","blal@gmail. com","3554878987", "F432","Group C")
            #     admin=Admin("Нурболот","nurbolot@gmail.com", "754357807", "E987" "Group T")
                                    
                         
                    

        

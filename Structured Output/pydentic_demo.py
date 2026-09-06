from pydantic import BaseModel, EmailStr, Field
from typing import Optional


# Defination of class
class Student(BaseModel):

    name:str = "nitish" # We can give default value also 
    age: Optional[int] = None #If there is no age then print None otherwise it can be any int or str... cause Optional
    email: EmailStr 
    cgpa: float = Field(gt=0, lt=10, default=5, description='A decimal value representing the cgpa of student') # WE can add constaints like this using Field.
    # Description work as same as Annoted.


new_student = {"name":"Kuldip","age":20, "email":"kuldip@gmail.com", "cgpa":9} # It will print 
# new_student = {} # Default value
# new_student = {"name":32} # Through Error cause it is not str.

student = Student(**new_student)

print(student)
# print(student.name)  # We can fetch it like this also

# We can convert pydentic output into dict,Json also
student_dict = dict(student)
print(student_dict['age'])

student_json = student.model_dump_json()
print(student_json)
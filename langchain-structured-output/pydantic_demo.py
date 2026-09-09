from pydantic import BaseModel,EmailStr,Field
from typing import Optional
class Student(BaseModel):
    name: str = 'Manas'
    age: Optional[int] = None
    email: EmailStr
    cgpa: float = Field(gt=0,lt=10,description='cgpa of the student')
new_student = {'age':'21','email':'abc@g.c','cgpa':1.1}

student = Student(**new_student)

student_dict = dict(student)

print(student_dict['age'])
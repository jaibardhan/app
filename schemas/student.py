from pydantic import BaseModel
import address

class Student(BaseModel):
    name: str
    age: int
    address: address

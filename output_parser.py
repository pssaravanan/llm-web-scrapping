from langchain_core.output_parsers.pydantic import PydanticOutputParser
from pydantic import BaseModel
from pydantic.fields import Field
from typing import List

class Student(BaseModel):
    name:str = Field(description="Name of the student")
    age:int = Field(description="Age of the student")
    school: str = Field(description="School of the student")
    school_location: str = Field(description="School location of the student")
    home_location: str = Field(description="Home location of the student")
    grade: str = Field(description="Grade of the student")
    gender: str = Field(description="Gender of the student")
    

student_parser = PydanticOutputParser(name="Student information", pydantic_object=Student)
from langchain.prompts.prompt import PromptTemplate
from langchain_ollama import OllamaLLM
from output_parser import student_parser
from langchain import hub
from dotenv import load_dotenv

load_dotenv()

template = """
Given information about a person in text. Return the result in key value format.
{person_details}

{output_format}
"""

if __name__ == "__main__":
    template = PromptTemplate(template=template, 
                              input_variables=['person_details'],
                              partial_variables={"output_format": student_parser.get_format_instructions()},
                              )
    llm = OllamaLLM(model='llama3')
    chain = template | llm | student_parser
    
    details = """"Karthikeyan in 6 years old boy.
    He is studying in Ist B in assisi school, KR Puram, Bangalore. 
    He is staying in Karthikeyan Nilayam, Abvirudhi Garden"""
    
    res = chain.invoke(input = {'person_details': details})
    print(res)
    

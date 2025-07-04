from langchain.prompts.prompt import PromptTemplate
from langchain_ollama import OllamaLLM

template = """
Given information about a person in text. Return the result in key value format
{person_details}
"""

if __name__ == "__main__":
    template = PromptTemplate(template=template, input_variables=['person_details'])
    llm = OllamaLLM(model='llama3')
    chain = template | llm
    
    details = """"Karthikeyan in 6 years old boy.
    He is studying in Ist B in assisi school, KR Puram, Bangalore"""
    res = chain.invoke(input = {'person_details': details})
    print(res)
    

from langchain_nvidia_ai_endpoints import ChatNVIDIA
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
load_dotenv()

model = ChatNVIDIA(model='google/gemma-2-2b-it')

prompt = PromptTemplate(
    template='Generate a detailed report on {topic}',
    input_variables=['topic']
)

prompt1 = PromptTemplate(
    template='Generate a 5 point summary on \n {text}',
    input_variables=['text']
)

parser = StrOutputParser()
chain = prompt | model | parser | prompt1 | model | parser

result = chain.invoke({'topic':'politics'})

print(result)

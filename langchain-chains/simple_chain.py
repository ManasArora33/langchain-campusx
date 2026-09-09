from langchain_nvidia_ai_endpoints import ChatNVIDIA
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
load_dotenv()

model = ChatNVIDIA(model='google/gemma-2-2b-it')

prompt = PromptTemplate(
    template='Generate 5 interesting facts about {topic}',
    input_variables=['topic']
)


parser = StrOutputParser()

chain = prompt | model | parser

result = chain.invoke({'topic':'politics'})

print(result)

# print(chain.get_graph().print_ascii())
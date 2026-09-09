from langchain_nvidia_ai_endpoints import ChatNVIDIA
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence

load_dotenv()

prompt = PromptTemplate(
    template="Write a joke about {topic}",
    input_variables=['topic']
)

prompt1 = PromptTemplate(
    template="Explain the following joke - {text}",
    input_variables=['text']
)

model = ChatNVIDIA(model = 'google/gemma-7b')

parser = StrOutputParser()

chain = RunnableSequence(prompt,model,parser,prompt1,model,parser)

print(chain.invoke("AI"))
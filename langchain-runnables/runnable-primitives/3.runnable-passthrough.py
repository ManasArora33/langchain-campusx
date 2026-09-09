from langchain_nvidia_ai_endpoints import ChatNVIDIA
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence,RunnableParallel, RunnablePassthrough

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

joke_gen_chain = RunnableSequence(prompt,model,parser)

parallel_chain = RunnableParallel({
    'joke': RunnablePassthrough(),
    'explanation': RunnableSequence(prompt1,model,parser)
})

chain = RunnableSequence(joke_gen_chain,parallel_chain)

print(chain.invoke("AI"))
from langchain_unstructured import UnstructuredLoader
from langchain_nvidia_ai_endpoints import ChatNVIDIA
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
load_dotenv()

model = ChatNVIDIA(model='deepseek-ai/deepseek-v3.2')

prompt = PromptTemplate(
    template="Write a summary for the following text {text}",
    input_variables=['text']
)

parser = StrOutputParser()

loader = UnstructuredLoader('cricket.txt')

docs = loader.load()

# print(type(docs))

# print(type(docs[0]))

# print(docs[0].page_content)

chain = prompt | model | parser

result = chain.invoke({'text':docs[0].page_content})

print(result)
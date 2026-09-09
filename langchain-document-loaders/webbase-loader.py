from langchain_community.document_loaders import WebBaseLoader
from langchain_nvidia_ai_endpoints import ChatNVIDIA
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model = ChatNVIDIA(model='deepseek-ai/deepseek-v3.2')

prompt = PromptTemplate(
    template="Answer the following question \n {ques} from the following text \n - {text}",
    input_variables=['ques','text']
)

parser = StrOutputParser()

url = 'https://www.hindustantimes.com/world-news/us-iran-war-live-updates-trump-strait-of-hormuz-tehran-attacks-israel-khamenei-netanyahu-oil-prices-middle-east-latest-101774143934572.html'

loader = WebBaseLoader(url)

docs = loader.load()

print(len(docs))
print(docs[0].page_content)

chain = prompt | model | parser

result = chain.invoke({'ques':'is the war finished?','text':docs[0].page_content})
print(result)
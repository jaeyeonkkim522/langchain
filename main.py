print(11)
from dotenv import load_dotenv
load_dotenv()

from langchain.llms import OpenAI
#from langchain.chat_models import ChatOpenAI

llm = OpenAI()
#chat_model = ChatOpenAI()

result = llm.predict("hi!")
print(result)

# 코드 추정 부분.

#chat_model.predict("hi!")
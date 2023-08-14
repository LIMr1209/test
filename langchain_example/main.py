import os
os.environ['http_proxy'] = 'http://127.0.0.1:7890'
os.environ['https_proxy'] = 'http://127.0.0.1:7890'
# import openai
#
#
# openai.api_key = ""
# print(openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role":"user", "content"  : "你好"}]).choices[0].message["content"])


from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage, AIMessage


chat = ChatOpenAI(temperature=.7, openai_api_key="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")

a = chat([SystemMessage(content="你是恋爱大师，可以指导人们如何谈恋爱"), HumanMessage(content="我喜欢赵丽颖，我应该咋办")])
print(a)

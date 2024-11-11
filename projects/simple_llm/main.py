import os
from dotenv import load_dotenv
from pathlib import Path
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

print(os.getenv('LANGCHAIN_PROJECT'))
print(os.getenv('LANGCHAIN_ENDPOINT'))

parser = StrOutputParser()

model = ChatOpenAI(model="gpt-4")

# messages = [
#     SystemMessage(content="Translate the following from English into Italian"),
#     HumanMessage(content="hi!"),
# ]

# result = model.invoke(messages)
# parser.invoke(result)

system_template = "Translate the following into {language}:"
prompt_template = ChatPromptTemplate.from_messages(
    [("system", system_template), ("user", "{text}")]
)
chain = prompt_template | model | parser
chain.invoke({"language": "japanese", "text": "hi"})
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage

load_dotenv()

model = ChatOpenAI(model="gpt-3.5-turbo")
model.invoke([HumanMessage(content="Hi! I'm Bob")])

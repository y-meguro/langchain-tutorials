from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import AIMessage, HumanMessage

load_dotenv()

model = ChatOpenAI(model="gpt-3.5-turbo")

# model.invoke([HumanMessage(content="Hi! I'm Bob")])
# model.invoke([HumanMessage(content="What's my name?")])
model.invoke(
    [
        HumanMessage(content="Hi! I'm Bob"),
        AIMessage(content="Hello Bob! How can I assist you today?"),
        HumanMessage(content="What's my name?"),
    ]
)
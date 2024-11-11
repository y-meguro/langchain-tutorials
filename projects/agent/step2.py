from dotenv import load_dotenv
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent

load_dotenv()

search = TavilySearchResults(max_results=2)
tools = [search]

model = ChatOpenAI(model="gpt-4")

agent_executor = create_react_agent(model, tools)

response = agent_executor.invoke(
    {"messages": [HumanMessage(content="whats the weather in sf?")]}
)

response["messages"]

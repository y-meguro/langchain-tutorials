from dotenv import load_dotenv
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI

load_dotenv()

search = TavilySearchResults(max_results=2)
# search_results = search.invoke("what is the weather in SF")
# print(search_results)

# If we want, we can create other tools.
# Once we have all the tools we want, we can put them in a list that we will reference later.
tools = [search]

model = ChatOpenAI(model="gpt-4")

# response = model.invoke([HumanMessage(content="hi!")])
# response.content

model_with_tools = model.bind_tools(tools)

response = model_with_tools.invoke([HumanMessage(content="What's the weather in SF?")])

print(f"ContentString: {response.content}")
print(f"ToolCalls: {response.tool_calls}")

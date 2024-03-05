from langchain_community.chat_models import ChatOpenAI
from langchain_community.agents import load_tools,initialize_agent,AgentType

llm = ChatOpenAI(model='gpt-3.5-turbo',temperature=0)
tools =load_tools(['wikipedia','llm-math'],llm=llm)
agent = initialize_agent(
    tools,llm,agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,verbase=True
)

question ="what is the square root of the population of the capital of the Country where the olympic Games were held in 2016?"
print(question)
agent.run(question)
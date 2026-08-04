from tools.tavily_tool import tavily_search
from tools.flight_tool import search_flights
from backend import run_travel_agent

# res = tavily_search("Best hotels in India?")
# print(res)

# res = search_flights("Plan a 7 days Japan trip from Bangalore")
# print(res)

user_input = input("Enter travel request: ")
response = run_travel_agent(user_input, "test_user_001")
print("\nFINAL RESPONSE:\n")
print(response["answer"])
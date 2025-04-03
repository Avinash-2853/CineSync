from langchain_groq import ChatGroq
import os
from duckduckgo_search import DDGS

from langchain.tools import BaseTool
from langchain.agents import AgentType, initialize_agent
import google.generativeai as genai
from google.generativeai import GenerativeModel
from models import groq_model
from utils import Utils
from langchain_core.output_parsers import JsonOutputParser
import json
from prompt import suggest_movie_prompt







#create a tool
class WebSearch(BaseTool):
    """
    Tool for websearch.
    Ineherits from BaseTool.
    """
    name: str = "Web Searching Tools"
    description: str = "Use this tool to answer the user query based on Web Search"

    def _run(self, query : str):
        """
        Method for getting the results from the web.
        Takes query as argument and return the results from web.

        Arguments
        --------
        query : Input by which the result will get from web.

        Returns
        --------
        all_result : Result from web.
        """
        #fetch using duck duck go.
        result = DDGS().text(query, max_results=5)

        all_results = ""
        for i in range(len(result)):
            search_results = result[i]['title'] + result[i]['body']
            all_results += search_results
        return all_results

web_tool = WebSearch()
tools = [web_tool]

#create a Agent.
web_agent = initialize_agent(
    tools = tools,
    llm = groq_model,
    agent_type = AgentType.REACT_DOCSTORE,
    max_iteration = 2, 
    verbose = True,
    handle_parsing_errors=True
)





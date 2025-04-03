import streamlit as st
import requests
from dotenv import load_dotenv
from utils import Utils
from agents import web_agent
from prompt import suggest_movie_prompt,review_summary_prompt, reason_prompt
import os 
import json

load_dotenv()

class Features:
    """
    Class reprsents the features of APP.
    
    Methods
    --------
    get_details : Gets the details of movie.
    get_cast : Gets the cast of the movie.
    get_suggestion : Suggest the movies simialar to movie.
    get_review : Summarizes the review of movie.

    Attributes
    ----------
    TMBD_API_KEY = API key for movie details.
    suggest_movie_prompt = Prompt for movie suggestion.
    review_summary_prompt = Prompt for summary of reviews.

    """
    def __init__(self):
        self.TMDB_API_KEY = os.getenv("TMDB_API_KEY")
        self.suggest_movie_prompt = suggest_movie_prompt
        self.review_summary_prompt = review_summary_prompt
        self.reason_prompt = reason_prompt


    def get_details(self,movie_name):
        """
        Function to get details of movie name from TMDB API.
        Takes movie name of arguments and returns first dictionary of movie details.

        Arguments
        ----------
        movie_name : name of detected movie.

        Returns
        ----------
        first movie details from results.
        """
        
        url = f"https://api.themoviedb.org/3/search/movie?api_key={self.TMDB_API_KEY }&query={movie_name}"
        response = requests.get(url,verify=False).json()
        movie = response.get("results", [])
        if movie:
            return movie[0]

    def get_cast(self, movie_name):
        """
        Function to get the cast details of the movie.
        Takes movie name as argument and will give the details of cast.
        
        Arguments
        -----------
        movie_name : Name of movie

        Returns
        ---------
        cast details of movie in json format.
        """

        #get the movie id
        movie_id = self.get_details(movie_name)['id']
        url = f"https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key={self.TMDB_API_KEY }"
        response = requests.get(url, verify=False).json()
        
        cast_list = []
        
        #get first 6 casts.
        for cast in response.get("cast", [])[:6]: 
            #make empty dictionary for store the cast details.
            cast_dict = dict()

            #get the cast name
            name = cast.get("name")
            #get the cast profile path.
            profile_path = cast.get("profile_path")

            #get the profile url of cast
            profile_url = f"https://image.tmdb.org/t/p/w500{profile_path}" if profile_path else "https://thumbs.dreamstime.com/b/profile-icon-exclamation-mark-profile-icon-alert-error-alarm-danger-symbol-profile-icon-exclamation-mark-profile-111945537.jpg"

            #stores the details in dictionary
            cast_dict["name"] = name
            cast_dict["profile_url"] = profile_url
            #append the dictionary in list.
            cast_list.append(cast_dict)
        return cast_list
       


    def get_suggestion(self, movie_name):
        """
        Function  to get suggest movie simialr to movie_name.
        Takes the movie_name as argument and will give the suggest movie in the list.

        Arguments:
        movie_name : name of movie.

        Returns
        -------
        response : Gives 5 related movies.

        """
        #initialize util object.
        util = Utils()
        #make chain using agent.
        agent_chain = util.make_chain(web_agent,self.suggest_movie_prompt)
        
        #get the response
        response = agent_chain.invoke({"movie_name": movie_name})

        #convert into json
        response = json.loads(response["output"])
        return response


    def get_review(self, movie_name):
        """
        Function to summarize the reviews of movies.
        Takes movie name as argument and gives the summarization of reviews.
        
        Arguments
        ---------
        movie_name : Name of movie.

        Returns
        --------
        Response : Summarization of movie reviews.
        """
        #initialize utils object.
        util = Utils()

        #make chain using agent
        agent_chain = util.make_chain(web_agent, self.review_summary_prompt)

        #get the response.
        response = agent_chain.invoke({"movie_name": movie_name})
        return response["output"]
    
    def get_reason(self, movie_name):
        """
        Will detect a movie name from text.
        Takes a movie_name as argument and gives the reason to watch movie and not watch movie.

        Arguments
        ----------
        movie_name

        Returns
        ---------
        response : reasons to watch movie and to not watch movie.

        """
        util = Utils()
        agent_chain = util.make_chain(web_agent, self.reason_prompt)
        response = agent_chain.invoke({"movie_name": movie_name})
        return response["output"]
    











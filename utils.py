from langchain.chains import LLMChain
import streamlit as st

class Utils:
    def make_chain(self,llm,prompt):
        """
        Function to make chain for llm.
        Takes the llm and prompt as arguments.
        Returns the chain

        Arguments
        ----------
        llm : LLM for response generate.
        prompt : Make a input text for any input.

        Returns
        ---------
        chain : Chain for response generation.
        """
        chain = prompt | llm 
        return chain
    
    def make_memory(self):
        """
        Function to make memory using streamlit session state.
        Returns the memory dictionary with "movie_name", "movie_details", "cast", "suggested_movie", "review" keys.

        Returns
        ---------
        streamlit session : For storing the content.
        """
        if "movie_name" not in st.session_state:
            st.session_state["movie_name"] = None
        
        if "movie_details" not in st.session_state:
            st.session_state["movie_details"] = None

        if "cast" not in st.session_state:
            st.session_state["cast"] = None

        if "suggested_movie" not in st.session_state:
            st.session_state["suggested_movie"] = None

        if "review" not in st.session_state:
            st.session_state["review"] = None
        
        if "reason" not in st.session_state:
            st.session_state["reason"] = None

        return st.session_state
from models import gemini_model, groq_model
import streamlit as st
from prompt import movie_name_from_image_prompt, movie_name_from_text_prompt
from utils import Utils
from langchain.schema import StrOutputParser
from agents import web_agent


class MovieDetect():
    """
    Class for detecting the movie.

    Methods
    ---------
    from_video : Get the movie name from video.

    Attributes
    ----------
    model1 : For detect the model.
    model2 : For content generation.
    image_prmpt: Prompt for getting movie name
    utils : Utils object for getting common use.
    """
    def __init__(self):
        """
        Method for inialize class attributes.
        """
        self.model1 = gemini_model
        self.model2 = groq_model
        self.image_prompt = movie_name_from_image_prompt
        self.utils = Utils()

    def from_video(self, video_file):
        """
        Methd to detect movie name from video clip.
        Takes a video file. Save as tempfile.
        Gets the movie name using llm.
        Returns the movie_name or 1 if movie not found.

        Arguments
        ----------
        video_file : A streamlit file uploader object 

        Returns
        --------
        movie_name : Movie name if found else "1"
        """
        # Save the uploaded file to a temporary location
        temp_file_path = f"./temp_video.{video_file.name.split('.')[-1]}"
    
        with open(temp_file_path, "wb") as f:
            f.write(video_file.read())

            # Open the file in binary mode and send it to Gemini
        with open(temp_file_path, "rb") as f:
            video_data = f.read()

        
        #get movie name from gemini
        response = self.model1.generate_content(
        contents=[
            {
                "mime_type": f"video/{video_file.name.split('.')[-1]}",
                "data": video_data
            },self.image_prompt])
        return response.text
    
    def from_text(self,text):
            """
            Method to get and validate movie name from text.
            Takes text as input and give movie name or "1" if not found.

            Arguments
            -----------
            text : Input text.

            Returns
            --------
            movie_name 
            """
            text_chain = self.utils.make_chain(web_agent, movie_name_from_text_prompt)
            response = text_chain.invoke(text)
            return response["output"]
    




     
     

    

    



    




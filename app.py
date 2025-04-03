import streamlit as st
from movie_detect import MovieDetect
from utils import Utils
from features import Features

st.set_page_config(page_icon = "🎥", page_title = "AI movie Detector")
st.title("AI Movie Summarizer 🎥")
class App():
    """
    Class that represents the App.

    Methods
    --------
    main : To start the program

    Attibutes
    -----------
    movie_detect : Object for movie detection
    movie_name : name of movie
    utils : Object of Utils
    features : Object of Features.
    """
    def __init__(self):
        self.movie_detect = MovieDetect()
        self.movie_name = None
        self.utils = Utils()
        self.features = Features()

    def main(self):
        """
        Fuction to start the program.
        """
        #initialize memory for storing the content.
        memory = self.utils.make_memory()

        #upload a file
        self.movie_name = st.sidebar.text_input("Enter a movie name. ")
        submit = st.sidebar.button("Submit")
        st.sidebar.write("(Note:Please Enter a valid movie name with spelling correction)")
        

        # if movie_name:
        #     #detect the movie name
        #     self.movie_name = self.movie_detect.from_text(movie_name)
        if submit:
        
            if self.movie_name is not None:
                try:
                    #if movie name not found
                    if int(self.movie_name) == 1:
                        st.warning("Invalid input")
                #if movie name found
                except ValueError:
                    #store the content in memory
                    memory["movie_name"] = self.movie_name
                    memory["suggested_movie"] = self.features.get_suggestion(self.movie_name)
                    memory["cast"] = self.features.get_cast(self.movie_name)
                    memory["review"] = self.features.get_review(self.movie_name)
                    memory["movie_details"] = self.features.get_details(self.movie_name)
                    memory["reason"] = self.features.get_reason(self.movie_name)
                
                    
                    tab1, tab2, tab3, tab4, tab5 = st.tabs(["Details","Cast" ,"Review","Reason","Suggested Movie"])

                    with tab1:
                        # Display the movie details
                        movie_details = memory["movie_details"]
                        col1, col2 = st.columns([1,2], border=True)
                        with col1:
                            st.image(f"https://image.tmdb.org/t/p/w500{movie_details["poster_path"]}")

                        with col2:
                            st.markdown(f"**Title**: {movie_details["title"]}")
                            st.markdown(f"**Overview** : {movie_details["overview"]}")
                            st.markdown(f"**release_date**: {movie_details["release_date"]}")
                            st.markdown(f"**Votes**: {movie_details["vote_count"]}")
                            st.markdown(f"**Average Rating**: {movie_details["vote_average"]}")
                        

                    with tab2:

                        #display the cast details 
                        for i in range(int(len(memory["cast"])/2)):
                            col1, col2 = st.columns([2,2] , border=True)
                            
                            with col1:
                                st.image(memory["cast"][i]["profile_url"])
                                st.markdown(f"*{memory["cast"][i]["name"]}*")

                            with col2:
                                st.image(memory["cast"][len(memory["cast"]) - i - 1]["profile_url"])
                                st.markdown(f"***{memory["cast"][len(memory["cast"]) - i - 1]["name"]}***")


                    
                    with tab3:
                        # display the reivew summary
                        st.markdown(memory["review"])
                    
                    with tab4:
                        st.markdown(memory["reason"])
                    
                    with tab5:
                        #Display the suggested movie.
                        try:
                            for item in memory["suggested_movie"]:
                                col1, col2 = st.columns([1,2], border=True)
                                movie_details = self.features.get_details(item)

                                with col1:
                                    st.image(f"https://image.tmdb.org/t/p/w500{movie_details["poster_path"]}")
                                
                                with col2:
                                    st.markdown(f"**Title**: {movie_details["title"]}")
                                    st.markdown(f"**Overview** : {movie_details["overview"]}")
                                    st.markdown(f"**release_date**: {movie_details["release_date"]}")
                                    st.markdown(f"**Votes**: {movie_details["vote_count"]}")

                                    st.markdown(f"**Average Rating**: {movie_details["vote_average"]}")
                        except TypeError:
                            pass


if __name__ == "__main__":               
    app = App()
    app.main()
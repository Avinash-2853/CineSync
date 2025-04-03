from langchain.prompts import PromptTemplate
movie_name_from_image_prompt = """Act as a professional movie reviewer. You have to guess movie name from video clip.
If it is movie name  then give me only movie name.
If the clip is not of any movie then return 1.
**output format**:
if Movie name : only movie name ('Genius',"Sita Ramam", "Sooryavansham", "Kaithi","All the best Pandya", "Naruto")
if not a movie name : 1
"""

movie_name_from_text_prompt = PromptTemplate.from_template("""You are expert movie reviewer you have to give only the movie name from the  text {text_input} with spelling correction. 
                                                           If there is no movie name in the text, return '1'. Do not return anything other than the movie name. Example: 'Genius is a great movie of Bollywood' → Output: 'Genius'.
""")

suggest_movie_prompt = PromptTemplate.from_template("""Suggest 5 movies similar to "{movie_name}" based on story, genre, and industry.  
Return the result in JSON format as a list of movie names.  

Example output:  
["Hugo", "The Hours", "Capote", "The Ghost Writer", "Adam"]  
The output should not contains any preamle and post text.
""")

review_summary_prompt =  PromptTemplate.from_template("""Give me 5 good thing and 5 bad thing about {movie_name} movie in detail from based user's reviews.""")
reason_prompt = PromptTemplate.from_template("""Give 5 reason why should I watch {movie_name}. 
                                             Give 5 reason why should I not watch. Reasearch about genre, director's previous movie, budget, promotion.""")

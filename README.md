🎬 AI Movie Summarizer
📌 Overview
AI Movie Summarizer is an intelligent tool that enhances the movie discovery experience. It suggests related movies, summarizes user reviews from the internet, and retrieves cast details using Generative AI.

🚀 Features
Movie Recommendation System – Finds related movies based on the targeted movie.

Review Summarization – Scrapes and summarizes user reviews using NLP.

Cast Details Retrieval – Fetches information about the movie’s cast and crew.

Movie Name Correction & Recognition – (Upcoming) Recognize movies from video clips.

Web Scraping – Extracts real-time movie data from multiple sources.

Generative AI Integration – Uses LLMs for intelligent analysis.

📂 Repository Structure
graphql
Copy
Edit
📦 AI Movie Summarizer  
│-- 📁 agents/         # Agents using the web search tool  
│-- 📄 app.py         # Main file and Streamlit UI  
│-- 📁 features/      # Core features of the app  
│-- 📁 models/        # Contains generative AI models  
│-- 📁 movie_detect/  # (Upcoming) Movie name correction & recognition from video clips  
│-- 📄 prompt.py      # Prompts for LLM interactions  
│-- 📄 requirements.txt  # Required libraries  
│-- 📁 tools/         # Web search tool  
│-- 📁 utils/         # Common functions (make chain, make memory)  
│-- 📄 README.md      # Project documentation  
🔧 Setup Instructions
1️⃣ Clone the Repository

bash
Copy
Edit
git clone https://github.com/your-username/AI-Movie-Summarizer.git
cd AI-Movie-Summarizer
2️⃣ Install Dependencies

bash
Copy
Edit
pip install -r requirements.txt
3️⃣ Set Up API Keys
Create a .env file in the root directory and add the following keys:

ini
Copy
Edit
GROQ_API_KEY=your_groq_api_key
GEMINI_API_KEY=your_gemini_api_key
TMDB_API_KEY=your_tmdb_api_key
4️⃣ Run the Application

bash
Copy
Edit
streamlit run app.py
🛠️ Technologies Used
Python

Streamlit – For UI

LLMs – For summarization & recommendations

Web Scraping – For real-time review extraction

APIs – GROQ, Gemini, TMDB for movie data

📌 Future Improvements
🎥 Movie recognition from video clips

🌎 Multi-language support

📊 Advanced sentiment analysis


## Project Title
YouTube Transcript & AI Summarizer

## Description
This application extracts transcripts from YouTube videos using the `youtube_transcript_api` and summarizes the content with the help of Google Generative AI.  
The app is built with `Streamlit` for an interactive web interface and uses environment variables for secure API key management.  
It is designed for quick content understanding, note-taking, and research purposes.

## Installation / Setup
### 1. Clone the Repository
git clone https://github.com/your-username/youtube-transcript-ai.git
cd youtube-transcript-ai

### 2. Create a Virtual Environment
`bash`
conda create -p venv python=3.10 -y
source venv/bin/activate   # Linux / Mac
conda activate venv/      # Windows

### 3. Install Dependencies
`bash`
pip install -r requirements.txt

### 4. Set Up Environment Variables
Create a .env file in the project root and add:
GOOGLE_API_KEY=your_google_generative_ai_key

## Usage / How to Run
`bash`
streamlit run app.py

http://localhost:8501/ 
Enter a YouTube video URL.
The app will fetch the transcript.
AI will generate a summary of the content.


## Quit the runnig application
	Windows/Linux: Ctrl + C
	macOS:	Cmd + C

##  Technologies Used
youtube_transcript_api – Extract YouTube video transcripts.
Streamlit – Interactive web app framework.
Google Generative AI – AI-powered text summarization.
python-dotenv – Manage environment variables.
pathlib – File and path management.

## Project Structure
youtube-transcript-ai/
│
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── .env                   # Environment variables (not committed)
├── README.md              # Project documentation
├── demo/                  # Screenshots / GIFs for project demo
│   ├── screenshot1.png
│   ├── screenshot2.png
│   └── demo.gif
└── utils/
    ├── transcript.py      # Transcript fetching logic
    └── summarizer.py      # AI summarization logic

## License
This project is licensed under the MIT License – you are free to use, modify, and distribute with attribution.

## Contact / Author Info
Author: Kuldeep Singh
📧 Email: kuldeep.kamboj@gmail.com
🔗 GitHub: [your-github-profile](https://github.com/Kuldeep-kamboj)

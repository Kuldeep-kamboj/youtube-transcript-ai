from youtube_transcript_api import YouTubeTranscriptApi

def extract_transcript_details(youtube_video_url):
    """
    Extract transcript text from a YouTube video.
    Tries to fetch Hindi first, falls back to English if unavailable.
    """
    try:
        video_id = youtube_video_url.split("=")[1]
        ytt_api = YouTubeTranscriptApi()
        
        # Fetch transcript in Hindi or English
        transcript_text = ytt_api.fetch(video_id, languages=["hi", "en"])
        
        # Join text into a single string
        transcript = " ".join(transcript.text for transcript in transcript_text)
        return transcript
    
    except Exception as e:
        raise e

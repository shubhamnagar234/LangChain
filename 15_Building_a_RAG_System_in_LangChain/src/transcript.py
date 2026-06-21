from youtube_transcript_api import (
    YouTubeTranscriptApi,
    TranscriptsDisabled,
    NoTranscriptFound,
)
import re


def extract_video_id(url):
    pattern = r"(?:v=|\/)([0-9A-Za-z_-]{11}).*"
    match = re.search(pattern, url)
    if match:
        return match.group(1)
    return None


def get_transcript(url):
    video_id = extract_video_id(url)
    if not video_id:
        raise ValueError("Invalid YouTube URL")

    try:
        # Fetch the list of all available transcripts
        transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)

        try:
            # Try to fetch English first
            transcript = transcript_list.find_transcript(["en"])
        except NoTranscriptFound:
            # If English is not found, iterate through available transcripts
            # and translate the first one we find into English.
            for available_transcript in transcript_list:
                transcript = available_transcript.translate("en")
                break

        # Actually fetch the text data
        transcript_data = transcript.fetch()

        # Flatten to plain text
        text = " ".join(chunk["text"] for chunk in transcript_data)
        return text

    except TranscriptsDisabled:
        return "No captions available for this video."
    except Exception as e:
        return f"Could not fetch transcript: {str(e)}"

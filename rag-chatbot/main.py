# from youtube_transcript_api import YouTubeTranscriptApi,TranscriptsDisabled


# video_id = "gVGhTX0g5LI"

# try:
#     ytt_api = YouTubeTranscriptApi()
#     transcript_list = ytt_api.fetch(video_id=video_id, languages=['en','en-IN'])
#     transcript_list_json = transcript_list.to_raw_data()
#     transcript = " ".join(chunk['text'] for chunk in transcript_list_json)
#     print(transcript)
#     # print(transcript_list.to_raw_data())
# except TranscriptsDisabled:
#     print("No captions available for this video")

import os
from dotenv import load_dotenv

from supadata import Supadata,SupadataError
load_dotenv()

supadata = Supadata(os.environ.get('SUPADATA_API_KEY'))
transcript = supadata.transcript(
    url="https://www.youtube.com/watch?v=gVGhTX0g5LI",
    lang="en",
    text=True,
    mode="auto"
)

print(transcript)
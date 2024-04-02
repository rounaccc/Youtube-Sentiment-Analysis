import googleapiclient.discovery
import googleapiclient.errors

api_service_name = "youtube"
api_version = "v3"
DEVELOPER_KEY = "AIzaSyATKfAyWwrxKsXacbUKUbwcjAsQEnKlKi0"

video_url = "https://www.youtube.com/watch?v=Lb2wwEx6DVw"
video_id = video_url.split('=')[-1]

youtube = googleapiclient.discovery.build(
    api_service_name, api_version, developerKey=DEVELOPER_KEY)

request = youtube.commentThreads().list(
    part="snippet",
    videoId=video_id,
    maxResults=50
)
response = request.execute()

comments_list = []

for item in response['items']:
    comments_list.append(item['snippet']['topLevelComment']['snippet']['textDisplay'])

print(comments_list)
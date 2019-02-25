# "https://www.googleapis.com/youtube/v3/search?key=AIzaSyDONq1sefS8lQ7WSqfPA0jdY0ypyY7hhaI&part=snippet&q=python&type=video"

from apiclient.discovery import build
from pprint import pprint

API_KEY = "AIzaSyDONq1sefS8lQ7WSqfPA0jdY0ypyY7hhaI"

youtube = build('youtube', 'v3', developerKey=API_KEY)

search_res = youtube.search().list(
    part='snippet',
    q='파이썬',
    type='video'
).execute()

for item in search_res['items']:
    pprint(item)

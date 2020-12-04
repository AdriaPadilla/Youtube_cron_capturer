from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

### CREDENTIALS

import credentials.keys as cr
import capturer.video as vid

DEVELOPER_KEY = cr.API_KEY
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

### Autentication

youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)

def get_videos(query, max_results):

    video_list = []

    search_response = youtube.search().list( # First, make the search Ranking Request
        q=query,
        part="id,snippet",
        maxResults=max_results,
        order="relevance",
        type="video",
        safeSearch="none",
        videoDuration="medium",
    ).execute()

    results = search_response["items"]

    for result in results: # For result in search result, get video metrics
        print(result["snippet"]["title"])

        vid_statistics = youtube.videos().list(
            id=result["id"]["videoId"],
            part="statistics, contentDetails",
        ).execute()

        stats = vid_statistics["items"][0]

        search_response_object = vid.Video( # Store all data in Python Object
            query,
            result["id"].get("kind", "Nan"),
            result["id"].get("videoId", "Nan"),
            result.get("kind", "Nan"),
            result["snippet"].get("channelId", "Nan"),
            result["snippet"].get("channelTitle", "Nan"),
            result["snippet"].get("description", "Nan"),
            result["snippet"].get("liveBroadcastContent", "Nan"),
            result["snippet"].get("publishedAt", "Nan"),
            result["snippet"].get("title", "Nan"),
            stats["statistics"].get("viewCount", "Nan"),
            stats["statistics"].get("likeCount", "Nan"),
            stats["statistics"].get("dislikeCount", "Nan"),
            stats["statistics"].get("favoriteCount", "Nan"),
            stats["statistics"].get("commentCount", "Nan"),
            stats["contentDetails"].get("duration", "Nan"),
            stats["contentDetails"].get("dimension", "Nan"),
            stats["contentDetails"].get("definition", "Nan"),
            stats["contentDetails"].get("caption", "Nan"),
            stats["contentDetails"].get("licensedContent", "Nan"),
        )
        video_list.append(search_response_object)

    return video_list

def explore_videos(query, max_results):
    videos = get_videos(query, max_results)
    return videos



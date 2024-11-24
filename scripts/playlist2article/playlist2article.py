import requests
from create_article import Article

# Replace with your API key and playlist ID
API_KEY = ""
PLAYLIST_ID = ""

# Base URL for YouTube Data API
base_url = "https://www.googleapis.com/youtube/v3"

def get_playlist_videos(api_key, playlist_id):
    print('get_playlist_videos')
    videos = []
    next_page_token = ""

    while True:
        # API request URL
        url = f"{base_url}/playlistItems?part=snippet&playlistId={playlist_id}&maxResults=50&pageToken={next_page_token}&key={api_key}"
        
        # Fetch data
        print("Fetching data")
        try:
            response = requests.get(url, timeout=10, verify=False)
        except requests.exceptions.Timeout:
            print("Request timed out")

        print("Extract data")
        data = response.json()

        # Extract video details
        for item in data.get("items", []):
            title = item["snippet"]["title"]
            video_id = item["snippet"]["resourceId"]["videoId"]
            video_url = f"https://www.youtube.com/watch?v={video_id}"

            # Define additional fields
            permalink = f"/videos/{video_id}.html"
            categories = "YouTube Videos"
            summary = item["snippet"].get("description", "No description available.")[:150]  # Truncate summary to 150 characters
            iframe_url = f"https://www.youtube.com/embed/{video_id}"

            # Append to videos list
            videos.append({
                "title": title,
                "permalink": permalink,
                "categories": categories,
                "summary": summary,
                "iframe_url": iframe_url,
                "url": video_url,
            })
        
        # Check for next page
        next_page_token = data.get("nextPageToken", "")
        if not next_page_token:
            break

    return videos

# Fetch videos
videos = get_playlist_videos(API_KEY, PLAYLIST_ID)

# Print details
for video in videos:
    print(f"Title: {video['title']}")
    print(f"Permalink: {video['permalink']}")
    # print(f"Categories: {video['categories']}")
    # print(f"Summary: {video['summary']}")
    print(f"Iframe URL: {video['iframe_url']}")
    print(f"Link: {video['url']}\n")
    print('========================== +++++ ==========================')

print("====== Start create article ======")

for video in videos:
    print(f"Title: {video['title']}")
    print(f"Permalink: {video['permalink']}")
    # print(f"Categories: {video['categories']}")
    # print(f"Summary: {video['summary']}")
    print(f"Iframe URL: {video['iframe_url']}")
    print(f"Link: {video['url']}\n")
    print('========================== +++++ ==========================')

    article = Article(video)
    article_name = Article.make_article_permanent_link_from_video_title(video['title']).lower()
    article_permanent_link = article_name + '.html'
    article.permalink = article_permanent_link
    article_text = article.create_article()

    Article.save_article_to_file(article_name, article_text)
    article.add_to_side_bar()


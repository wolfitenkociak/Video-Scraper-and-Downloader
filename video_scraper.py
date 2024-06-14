import requests
from bs4 import BeautifulSoup
import re
import os

def get_videos_from_channel(channel_url):
    response = requests.get(channel_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Szukanie skryptu zawierającego dane wideo
    data_script = ""
    scripts = soup.find_all('script')
    for script in scripts:
        if script.string and 'var ytInitialData' in script.string:
            data_script = script.string
            break

    if not data_script:
        print("Nie znaleziono skryptu zawierającego dane wideo.")
        return []

    # Wyodrębnienie identyfikatorów wideo
    video_ids = re.findall(r'"videoId":"(.*?)"', data_script)
    unique_video_ids = list(set(video_ids))  # usunięcie duplikatów

    video_urls = [f'https://www.youtube.com/watch?v={video_id}' for video_id in unique_video_ids]

    return video_urls

def save_videos_to_file(videos, filename):
    # Sprawdzenie, czy plik już istnieje
    if os.path.exists(filename):
        print(f"Plik {filename} już istnieje. Nadpisywanie.")
    
    # Zapisanie linków do filmów
    with open(filename, 'w') as file:
        for url in videos:
            file.write(f"{url}\n")

# URL kanału
channel_url = 'https://www.youtube.com/@OrbitalNCG/videos'
videos = get_videos_from_channel(channel_url)

# Nazwa pliku do zapisu
filename = 'filmy.txt'

# Zapisanie linków do filmów w pliku
save_videos_to_file(videos, filename)

print(f"Zapisano {len(videos)} filmów w pliku {filename}")

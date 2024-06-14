from pytube import YouTube
import os

def read_video_links(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file.readlines()]

def download_video(video_url, output_path='.'):
    try:
        yt = YouTube(video_url)

        # Pobieranie strumienia wideo w najwyższej rozdzielczości
        video_stream = yt.streams.filter(progressive=False, file_extension='mp4').order_by('resolution').desc().first()

        if video_stream:
            print(f"Pobieranie: {yt.title} w rozdzielczości {video_stream.resolution}")
            video_stream.download(output_path)
            print(f"Pobrano: {yt.title}")
        else:
            print(f"Nie znaleziono odpowiednich strumieni dla: {video_url}")
    except Exception as e:
        print(f"Błąd podczas pobierania {video_url}: {str(e)}")

def download_videos_from_file(filename, output_path='.'):
    video_links = read_video_links(filename)
    for video_url in video_links:
        download_video(video_url, output_path)

# Nazwa pliku z linkami do filmów
input_filename = 'filmy.txt'
# Katalog, do którego zostaną pobrane filmy
output_directory = 'filmy'

# Tworzenie katalogu, jeśli nie istnieje
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Pobieranie filmów
download_videos_from_file(input_filename, output_directory)

print(f"Wszystkie filmy zostały pobrane do katalogu {output_directory}")

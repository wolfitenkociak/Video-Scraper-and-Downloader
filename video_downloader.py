import yt_dlp
import os

def download_video(video_url, output_path='.'):
    try:
        ydl_opts = {
            'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',  # Wybierz najlepszą jakość
            'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),  # Ścieżka do zapisu
            'progress_hooks': [hook],
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(video_url, download=True)
            if 'entries' in info_dict:
                # Jeśli jest więcej niż jeden wynik, pobierz pierwszy
                info_dict = info_dict['entries'][0]

            title = info_dict.get('title', 'video')
            extension = info_dict.get('ext', 'mp4')
            filename = f"{title}.{extension}"
            print(f"Pobieranie: {filename} w rozdzielczości {info_dict.get('format_id')}")

    except Exception as e:
        print(f"Błąd podczas pobierania {video_url}: {str(e)}")

def hook(d):
    if d['status'] == 'downloading':
        print(f"Pobieranie: {d['filename']} rozdzielczość {d.get('format_id', 'unknown')}")

def download_videos_from_file(filename, output_path='.'):
    with open(filename, 'r') as file:
        video_urls = file.readlines()

    for video_url in video_urls:
        video_url = video_url.strip()
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

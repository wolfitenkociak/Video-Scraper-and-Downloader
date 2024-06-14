# Video Scraper and Downloader

**Video Scraper and Downloader** to zestaw skryptów w Pythonie, które pozwalają na pobieranie listy linków do filmów z określonego kanału YouTube oraz na pobieranie tych filmów na lokalny dysk. Projekt powstał, aby umożliwić pobieranie gameplayów z gier w wysokiej jakości. Korzysta z bibliotek `requests`, `BeautifulSoup` oraz `yt-dlp`.

## Wymagania

Aby uruchomić te skrypty, potrzebujesz zainstalowanych poniższych pakietów Python:

- `requests`
- `beautifulsoup4`
- `yt-dlp`

Dodatkowo, **yt-dlp** wymaga zainstalowanego programu **FFmpeg** do prawidłowego działania. Możesz pobrać FFmpeg ze strony [FFmpeg.org](https://ffmpeg.org/download.html) i zainstalować zgodnie z instrukcjami dla Twojego systemu operacyjnego.

Możesz zainstalować wymagane pakiety Python używając poniższego polecenia:

```sh
pip install requests beautifulsoup4 yt-dlp
```

## Instrukcja uruchomienia

1. Sklonuj repozytorium lub skopiuj pliki `video_scraper.py` oraz `video_downloader.py` na swój komputer.
2. Upewnij się, że masz zainstalowane wymagane pakiety (patrz sekcja Wymagania).
3. Upewnij się, że masz zainstalowany FFmpeg i jest on dostępny w ścieżce systemowej.

### Krok 1: Pobierz linki do filmów

Uruchom skrypt `video_scraper.py`, aby pobrać listę linków do filmów z określonego kanału YouTube i zapisać je w pliku tekstowym:

```sh
python video_scraper.py
```

### Krok 2: Pobierz filmy

Uruchom skrypt `video_downloader.py`, aby pobrać filmy na lokalny dysk. Skrypt korzysta z pliku `filmy.txt` utworzonego w poprzednim kroku:

```sh
python video_downloader.py
```

Filmy zostaną zapisane w katalogu `filmy`.

## Szczegóły działania

### `video_scraper.py`

1. `get_videos_from_channel(channel_url)`: Funkcja ta pobiera URL kanału YouTube jako argument, pobiera dane HTML z tego URL i szuka w nich skryptu zawierającego dane o wideo. Następnie wyodrębnia identyfikatory wideo i tworzy z nich listę unikalnych linków do filmów.
2. `save_videos_to_file(videos, filename)`: Funkcja ta zapisuje listę linków do plików wideo w pliku tekstowym o podanej nazwie. Jeśli plik już istnieje, nadpisuje go.

Domyślny URL kanału jest ustawiony na `https://www.youtube.com/@OrbitalNCG/videos`, a domyślna nazwa pliku do zapisu to `filmy.txt`.

### `video_downloader.py`

1. `download_video(video_url, output_path='.')`: Funkcja ta pobiera wideo z podanego URL i zapisuje je w określonym katalogu. Używa `yt-dlp` do wyboru najlepszej jakości wideo.
2. `hook(d)`: Funkcja pomocnicza wyświetlająca postęp pobierania.
3. `download_videos_from_file(filename, output_path='.')`: Funkcja ta czyta linki do filmów z pliku tekstowego i pobiera każdy z nich, zapisując w określonym katalogu.

Domyślna nazwa pliku z linkami to `filmy.txt`, a domyślny katalog do zapisu filmów to `filmy`.

---

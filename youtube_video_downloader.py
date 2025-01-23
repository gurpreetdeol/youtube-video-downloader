'''
HOW TO: Download YouTube Videos Programmatically with Python & pytube

$ pip install pytube

$ python3 download.py
'''

from pytube import YouTube
import ssl

ssl._create_default_https_context = ssl._create_unverified_context


def on_progress(stream, chunk, bytes_remaining):
    print(f"{name} downloading...")


def on_complete(stream, file_path):
    print(f"{name} download complete")


links = [
    "",
]

def download(links):
    global name
    for link in links:
        yt = YouTube(
            link,
            on_progress_callback=on_progress,
            on_complete_callback=on_complete,
            use_oauth=False,
            allow_oauth_cache=True
        )
        name = yt.title
        print("Video Started Downloading: ", yt.title)
        try:
            yt.streams.filter(file_extension='mp4', res="1080p").first().download()
        except:
            yt.streams.filter(file_extension='mp4', res="720p").first().download()
        print()
        print()


download(links=links)

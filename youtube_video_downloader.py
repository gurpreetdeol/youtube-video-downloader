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
    "https://www.youtube.com/watch?v=nKF8wCFBb8c"
]

# "https://www.youtube.com/watch?v=8BqjFy7AHho",
# "https://www.youtube.com/watch?v=90Neau9RVrA",
# "https://www.youtube.com/watch?v=ARfamXPV2k4",
# "https://www.youtube.com/watch?v=fhn3YP6TZto",
# "https://www.youtube.com/watch?v=dYxzz6_ixaY"
# "https://www.youtube.com/watch?v=IA3WxTTPXqQ"
# "Machine Learning Operations With Vertex AI on Google Cloud Platform"
# "https://www.youtube.com/watch?v=snUEwsft1wY&list=PLgxF613RsGoUuEjJJxJW2JYyZ8g1qOUou&index=1&pp=iAQB",
# "https://www.youtube.com/watch?v=pnQ5Rv4ZQfo&list=PLgxF613RsGoUuEjJJxJW2JYyZ8g1qOUou&index=2&pp=iAQB",
# "https://www.youtube.com/watch?v=Z5whg20WvS8&list=PLgxF613RsGoUuEjJJxJW2JYyZ8g1qOUou&index=3&pp=iAQB",
# "https://www.youtube.com/watch?v=ZZadMQTKJXk&list=PLgxF613RsGoUuEjJJxJW2JYyZ8g1qOUou&index=4&pp=iAQB",
# "https://www.youtube.com/watch?v=GOxHYfCLc6U&list=PLgxF613RsGoUuEjJJxJW2JYyZ8g1qOUou&index=5&pp=iAQB",
# "https://www.youtube.com/watch?v=0vhviqmH8Gg&list=PLgxF613RsGoUuEjJJxJW2JYyZ8g1qOUou&index=6&pp=iAQB",
# "https://www.youtube.com/watch?v=1gHJgY7AXAs&list=PLgxF613RsGoUuEjJJxJW2JYyZ8g1qOUou&index=7&pp=iAQB",
# "https://www.youtube.com/watch?v=m_x3WBtr6y0&list=PLgxF613RsGoUuEjJJxJW2JYyZ8g1qOUou&index=8&pp=iAQB",
# "https://www.youtube.com/watch?v=IcVyP_ZAXmY&list=PLgxF613RsGoUuEjJJxJW2JYyZ8g1qOUou&index=9&pp=iAQB",
# "https://www.youtube.com/watch?v=7y_t_bW0LHQ&list=PLgxF613RsGoUuEjJJxJW2JYyZ8g1qOUou&index=10&pp=iAQB",
# "https://www.youtube.com/watch?v=kzDd94KucBQ&list=PLgxF613RsGoUuEjJJxJW2JYyZ8g1qOUou&index=11&pp=iAQB",
# "https://www.youtube.com/watch?v=-5E3hWfsB4I&list=PLgxF613RsGoUuEjJJxJW2JYyZ8g1qOUou&index=12&pp=iAQB"

# "Machine Learning Specialization by Andrew Ng"
# "https://www.youtube.com/watch?v=OSOis7KlQ-Q&list=PL7rilRdYxlDuW2AV36RDOO3FpsM6ah0Gq&index=1&pp=iAQB",
# "https://www.youtube.com/watch?v=vY9fR1vDkNY&list=PL7rilRdYxlDuW2AV36RDOO3FpsM6ah0Gq&index=2&pp=iAQB",
# "https://www.youtube.com/watch?v=zGFg6qRU434&list=PL7rilRdYxlDuW2AV36RDOO3FpsM6ah0Gq&index=3&pp=iAQB",
# "https://www.youtube.com/watch?v=rAwUXS_rFzM&list=PL7rilRdYxlDuW2AV36RDOO3FpsM6ah0Gq&index=4&pp=iAQB",
# "https://www.youtube.com/watch?v=0RdiQmFHwfY&list=PL7rilRdYxlDuW2AV36RDOO3FpsM6ah0Gq&index=5&pp=iAQB",
# "https://www.youtube.com/watch?v=5Y913e2I7GY&list=PL7rilRdYxlDuW2AV36RDOO3FpsM6ah0Gq&index=6&pp=iAQB",
# "https://www.youtube.com/watch?v=VhXeJUDg4rA&list=PL7rilRdYxlDuW2AV36RDOO3FpsM6ah0Gq&index=7&pp=iAQB",
# "https://www.youtube.com/watch?v=MNfVs1JImpo&list=PL7rilRdYxlDuW2AV36RDOO3FpsM6ah0Gq&index=8&pp=iAQB",
# "https://www.youtube.com/watch?v=8xNegjbcrHg&list=PL7rilRdYxlDuW2AV36RDOO3FpsM6ah0Gq&index=9&pp=iAQB",
# "https://www.youtube.com/watch?v=GaFrQd-solM&list=PL7rilRdYxlDuW2AV36RDOO3FpsM6ah0Gq&index=10&pp=iAQB"

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

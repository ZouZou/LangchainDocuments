from pytube import YouTube

# YouTube('https://www.youtube.com/shorts/YLja7ZFMHjI').streams.first().download()
yt = YouTube('https://www.youtube.com/shorts/YLja7ZFMHjI')
# yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()
# yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').asc().first().download()
yt.streams
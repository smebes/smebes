import flet
import pyDownload

def main(page: flet.Page):
    page.title = "Youtube Music Downloader by Güney Bircan"
    page.window_width = 1280
    page.window_height = 720
    appTitle = flet.Text(value = "Youtube Music Downloader by Güney Bircan", color = "white", size = 45)
    page.controls.append(appTitle)
    
    def get_video_url(e):
        if not videoUrl.value:
            videoUrl.error_text = "Please Enter The Url"
            page.update()
        else:
            urlOfVideo = videoUrl.value
            check = pyDownload.yt_download(urlOfVideo)
            if check:
                videoUrl.error_text = None
                videoUrl.label = "Youtube Video Url"
                page.update()
            else:
                videoUrl.error_text = "Please Enter The YOUTUBE URL!"
                page.update()
    videoUrl = flet.TextField(label = "Youtube Video Url")
    page.add(videoUrl, flet.ElevatedButton("Download!",on_click=get_video_url))

flet.app(target=main)

from flask import Flask, request, send_file, render_template, url_for
from pytube import YouTube
import logging
import sys
import os
from hello import timed_delete
from threading import Timer
timed_delete()
logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
app = Flask(__name__)

@app.route("/hello")
def index():
    return "Hello World!"
@app.route("/")
def youtube_downloader():
    my_css = url_for('static', filename='cover.css')
    return render_template('index.html', css_path= my_css)
 
@app.route("/download_video", methods=["GET","POST"])
def download_video():
    """
    First pytube downloads the file locally in pythonanywhere:
    /home/your_username/video_name.mp4
 
    Then use Flask's send_file() to download the video 
    to the user's Downloads folder. 
    """
    try:
        youtube_url = request.form["URL"]
        local_download_path = YouTube(youtube_url).get_highest_resolution().download()
        fname = local_download_path.split("//")[-1]

        return send_file(fname, as_attachment=True)
    except exception as e:
        logging.exception("Failed download")
        print(e)
        return render_template('download_failed.html')

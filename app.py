import logging
import os
import sys
from threading import Timer

import pytube
from flask import Flask, render_template, request, send_file, url_for

from hello import timed_delete

timed_delete()
logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
app = Flask(__name__)


@app.route("/")
def youtube_downloader():
    my_css = url_for("static", filename="cover.css")
    return render_template("index.html", css_path=my_css)


@app.route("/download_video", methods=["GET", "POST"])
def download_video():
    """
    First pytube downloads the file locally in pythonanywhere:
    /home/your_username/video_name.mp4

    Then use Flask's send_file() to download the video
    to the user's Downloads folder.
    """
    local_download_path = (
        pytube.YouTube("https://www.youtube.com/watch?v=b1JlYZQG3lI"
                       ).streams.get_highest_resolution().download())
    fname = local_download_path.split("//")

    return send_file(fname, as_attachment=True)

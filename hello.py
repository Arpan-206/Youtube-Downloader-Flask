import os
import threading


def hi_delete():
    path = os.getcwd()
    print(path)
    test = os.listdir(path)
    for item in test:
        if item.endswith(".mp4"):
            os.remove(os.path.join(path, item))


def timed_delete():
    hi_delete()


timer = threading.Timer(1800.0, timed_delete)
timer.start()

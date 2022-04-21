from flask import Flask, redirect, render_template, request, url_for
import os
from subprocess import *
from sys import executable
from glob import glob
from threading import Thread

app = Flask(__name__)


@app.route("/exec")
def index():
    image_source = request.args.get('file')

    # if there is an old download link file, delete it. Also create output folder if not exist
    if os.path.isdir('output'):
        for filename in glob('output/generated_download_link.json'):
            os.remove(filename)
    else:
        os.makedirs('output')

    Popen([executable, 'main.py', image_source], creationflags=CREATE_NEW_CONSOLE)
    # Popen([executable, 'actor_grouping_audio_pipeline.py', filename], creationflags=CREATE_NEW_CONSOLE)
    # Popen([executable, 'shot_boundary_detection.py', filename], creationflags=CREATE_NEW_CONSOLE)
    # Popen([executable, 'shot_boundary_detection.py', filename], creationflags=CREATE_NEW_CONSOLE)
    # Popen([executable, 'shot_boundary_detection.py', filename], creationflags=CREATE_NEW_CONSOLE)

    return ''


@app.route("/remove")
def remove():
    file_source = request.args.get('file')
    # remove file
    if os.path.isdir('output'):
        for filename in glob('output/' + file_source):
            os.remove(filename)
            print('[INFO] previous output file removed')

    return ''


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081, debug=True)





































# from flask import Flask, redirect, render_template, request, url_for
# import os
# from subprocess import *
# from sys import executable
#
# app = Flask(__name__)
#
#
# @app.route("/exec")
# def index():
#     image_source = request.args.get('file')
#
#     Popen([executable, 'main.py', image_source], creationflags=CREATE_NEW_CONSOLE)
#     # Popen([executable, 'actor_grouping_audio_pipeline.py', filename], creationflags=CREATE_NEW_CONSOLE)
#     # Popen([executable, 'shot_boundary_detection.py', filename], creationflags=CREATE_NEW_CONSOLE)
#     # Popen([executable, 'shot_boundary_detection.py', filename], creationflags=CREATE_NEW_CONSOLE)
#     # Popen([executable, 'shot_boundary_detection.py', filename], creationflags=CREATE_NEW_CONSOLE)
#
#     return ''
#
#
# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=8081, debug=True)

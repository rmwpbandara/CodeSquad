import os
from threading import Thread
import webbrowser


def process1():
    os.system("http-server -c-1")

# def process12():

def process2():
    os.system('cd venv/scripts && activate && cd.. && cd.. && server.py');



def process3():
    url = "http://localhost:8080/"
    webbrowser.open_new_tab(url)


Thread(target=process1).start()
# Thread(target=process12).start()
Thread(target=process2).start()
Thread(target=process3).start()


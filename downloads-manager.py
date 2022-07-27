import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

path = "C:\\Users\\xshay\\Downloads"

# files = os.listdir(path)

# for file in files:
#     print(file)


# this is the event handler
the_event_handler = FileSystemEventHandler()



# this is the observer
the_observer = Observer()
the_observer.schedule(the_event_handler, path, recursive=False)


# function to perform when a file is downloaded

def on_created(event):
    print("A file has been downloaded")


# calls function when a file is created (downloaded)

the_event_handler.on_created = on_created

# starting the observer

the_observer.start()
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    the_observer.stop()
    the_observer.join()
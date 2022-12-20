import time
import sys

from handler import Handler
from organizer import Organizer
from watchdog.observers import Observer

def main():
    if sys.argv[1:]:
        dir_path = sys.argv[1]
    else:
        print("Please provide a value for path")
        print("Usage: python main.py <path>")
        exit(1)

    organizer = Organizer(dir_path)
    handler = Handler(organizer)
    observer = Observer()

    # call organizer.organize() to organize the files in the directory that havent been moved yet
    organizer.organize()

    observer.schedule(handler, path=dir_path, recursive=True)

    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        observer.join()

if __name__ == "__main__":
    main()


import os
import shutil
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import logging

# Directories for path and destinations
path = "C:\\Users\\xshay\\Downloads"
video_dir = "C:\\Users\\xshay\\Downloads\\Videos"
image_dir = "C:\\Users\\xshay\\Downloads\\Images"
document_dir = "C:\\Users\\xshay\\Downloads\\Documents"
software_dir = "C:\\Users\\xshay\\Downloads\\Softwares"
iso_dir = "C:\\Users\\xshay\\Downloads\\ISOs"
other_dir = "C:\\Users\\xshay\\Downloads\\Others"

# File extensions
image_extensions = [".jpg", ".jpeg", ".jpe", ".jif", ".jfif", ".jfi", ".png", ".gif", ".webp", ".tiff", ".tif", ".psd", ".raw", ".arw", ".cr2", ".nrw", ".k25", ".bmp", ".dib", ".heif", ".heic", ".ind", ".indd", ".indt", ".jp2", ".j2k", ".jpf", ".jpf", ".jpx", ".jpm", ".mj2", ".svg", ".svgz", ".ai", ".eps", ".ico"]
video_extensions = [".webm", ".mpg", ".mp2", ".mpeg", ".mpe", ".mpv", ".ogg", ".mp4", ".mp4v", ".m4v", ".avi", ".wmv", ".mov", ".qt", ".flv", ".swf", ".avchd"]
document_extensions = [".txt", ".doc", ".docx", ".odt", ".pdf", ".xls", ".xlsx", ".ppt", ".pptx"]
software_extensions = [".exe", ".msi", ".dll", ".lib"]
iso_extensions = [".iso", ".img"]
other_extensions = [".zip", ".rar", ".7z", ".ace"]

# Check for duplicate file
def duplicate(name, destination):
    f_name, ext = os.path.splitext(name);
    name = f"{name}1{ext}"
    return name

# Function to move files
def move(filee, destination, name):
    if os.path.exists(f"{destination}/{name}"):
        uniq_name = duplicate(name, destination)
        old_name = os.path.join(destination, name)
        new_name = os.path.join(destination, uniq_name)
        os.rename(old_name, new_name)
    shutil.move(filee, destination)

# Event handler class
class Handler(FileSystemEventHandler):
    def on_modified(self, event):
        with os.scandir(path) as files:
            for filee in files:
                name = filee.name
                self.check_image(filee, name)
                self.check_video(filee, name)
                self.check_document(filee, name)
                self.check_software(filee, name)
                self.check_iso(filee, name)
                self.check_other(filee, name)

    def check_image(self, filee, name):
        for image_extension in image_extensions:
            if name.endswith(image_extension) or name.endswith(image_extension.upper()):
                move(filee, image_dir, name)
                logging.info(f"Transfered image {name}")
    def check_video(self, filee, name):
        for video_extension in video_extensions:
            if name.endswith(video_extension) or name.endswith(video_extension.upper()):
                move(filee, video_dir, name)
                logging.info(f"Transfered video {name}")
    def check_document(self, filee, name):
        for document_extension in document_extensions:
            if name.endswith(document_extension) or name.endswith(document_extension.upper()):
                move(filee, document_dir, name)
                logging.info(f"Transfered document {name}")
    def check_software(self, filee, name):
        for software_extension in software_extensions:
            if name.endswith(software_extension) or name.endswith(software_extension.upper()):
                move(filee, software_dir, name)
                logging.info(f"Transfered software {name}")
    def check_iso(self, filee, name):
        for iso_extension in iso_extensions:
            if name.endswith(iso_extension) or name.endswith(iso_extension.upper()):
                move(filee, iso_dir, name)
                logging.info(f"Transfered ISO {name}")
    def check_other(self, filee, name):
        for other_extension in other_extensions:
            if name.endswith(other_extension) or name.endswith(other_extension.upper()):
                move(filee, other_dir, name)
                logging.info(f"Transfered miscellaneous {name}")

# Event handler
the_event_handler = Handler()

# Observer
the_observer = Observer()
the_observer.schedule(the_event_handler, path, recursive=True)

# Logging format
logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s : %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')

# Starting the observer
the_observer.start()
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    the_observer.stop()
    the_observer.join()
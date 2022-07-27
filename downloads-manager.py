import shutil
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

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
document_extensions = [".doc", ".docx", ".odt", ".pdf", ".xls", ".xlsx", ".ppt", ".pptx"]
software_extensions = [".exe", ".msi"]
iso_extensions = [".iso", ".rar"]

# Function to move files
def move(source, destination):
    shutil.move(source, destination)

# Event handler
the_event_handler = FileSystemEventHandler()

# Observer
the_observer = Observer()
the_observer.schedule(the_event_handler, path, recursive=False)

# Function to be called when a file is downloaded
def on_created(event):
    if event.src_path.endswith in image_extensions:
        move(event.src_path, image_dir)
    elif event.src_path.endswith in video_extensions:
        move(event.src_path, video_dir)
    elif event.src_path.endswith in document_extensions:
        move(event.src_path, document_dir)
    elif event.src_path.endswith in software_extensions:
        move(event.src_path, software_dir)
    elif event.src_path.endswith in iso_extensions:
        move(event.src_path, iso_dir)
    else:
        move(event.src_path, other_dir)

# Calls function when a file is downloaded
the_event_handler.on_created = on_created

# Starting the observer
the_observer.start()
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    the_observer.stop()
    the_observer.join()
from watchdog.events import *
from typing import Union
from organizer import Organizer

class Handler(FileSystemEventHandler):
    def __init__(self, organizer: Organizer) -> None:
        super().__init__()
        self.organizer = organizer

    def on_moved(self, event: Union[DirMovedEvent, FileMovedEvent]):
        if isinstance(event, FileMovedEvent):
            self.organizer.move(event.dest_path)

    def on_created(self, event: Union[DirCreatedEvent, FileCreatedEvent]):
        if isinstance(event, FileCreatedEvent):
            self.organizer.move(event.src_path)

    def on_modified(self, event: Union[DirModifiedEvent, FileModifiedEvent]):
        if isinstance(event, FileModifiedEvent):
            self.organizer.move(event.src_path)

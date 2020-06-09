import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class LoggingEventHandler1(FileSystemEventHandler):
    """Logs all the events captured."""

    def on_moved(self, event):
        super(LoggingEventHandler1, self).on_moved(event)

        what = 'directory' if event.is_directory else 'file'
        logging.info("Moved %s: from %s to %s", what, event.src_path,
                     event.dest_path)
        if event.dest_path == "/home/panda/Downloads/log.txt":
            with open("/home/panda/Downloads/log.txt", 'r+') as file:
                file_contents = file.read()
                file_contents = file_contents.replace("sh", "ssh")
                file.truncate(0)
                file.seek(0)
                file.write(file_contents)

    def on_created(self, event):
        super(LoggingEventHandler1, self).on_created(event)

        what = 'directory' if event.is_directory else 'file'
        logging.info("Created %s: %s", what, event.src_path)

    def on_deleted(self, event):
        super(LoggingEventHandler1, self).on_deleted(event)

        what = 'directory' if event.is_directory else 'file'
        logging.info("Deleted %s: %s", what, event.src_path)

    def on_modified(self, event):
        super(LoggingEventHandler1, self).on_modified(event)

        what = 'directory' if event.is_directory else 'file'
        logging.info("Modified %s: %s", what, event.src_path)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = sys.argv[1] if len(sys.argv) > 1 else '.'
    event_handler = LoggingEventHandler1()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1000000)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
    print("Exiting")



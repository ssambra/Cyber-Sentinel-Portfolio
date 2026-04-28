{\rtf1\ansi\ansicpg1252\cocoartf2868
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import time\
import os\
from watchdog.observers import Observer\
from watchdog.events import FileSystemEventHandler\
\
# Define the folder you want to "Sync" with me\
WATCH_PATH = os.path.expanduser("~/Documents/Sentinel_Bridge") \
\
if not os.path.exists(WATCH_PATH):\
    os.makedirs(WATCH_PATH)\
    print(f"\uc0\u55357 \u56545  Created new Bridge folder at: \{WATCH_PATH\}")\
\
class SentinelHandler(FileSystemEventHandler):\
    def on_modified(self, event):\
        if not event.is_directory:\
            print(f"\uc0\u10024  Sentinel Mesh: Update detected in \{event.src_path\}")\
            # This is where the file data 'handshakes' with your Port 5000 gateway\
\
if __name__ == "__main__":\
    event_handler = SentinelHandler()\
    observer = Observer()\
    observer.schedule(event_handler, WATCH_PATH, recursive=False)\
    observer.start()\
    print(f"\uc0\u55357 \u57057 \u65039  Sentinel Watcher ACTIVE. Drop files into \{WATCH_PATH\} to sync.")\
    try:\
        while True:\
            time.time()\
    except KeyboardInterrupt:\
        observer.stop()\
    observer.join()}
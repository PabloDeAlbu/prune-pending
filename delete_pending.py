#!/usr/bin/env python3

import os
import time
import subprocess
import argparse

now = time.time()

parser = argparse.ArgumentParser(description='Remove files from /var/spool/sympa/subscribe/ older than 24 hs, by default')
parser.add_argument('--time-lapse',"-t", help='Number of hours required to delete a file', default="24")

folder = '/var/spool/sympa/subscribe/'

time_lapse = int(parser.parse_args().time_lapse)

files = [os.path.join(folder, filename) for filename in os.listdir(folder)]
for filename in files:
    hs_lapse = (now - os.stat(filename).st_mtime) / 3600
    if (filename.endswith('add')) and ( hs_lapse > time_lapse):
        os.remove(filename)
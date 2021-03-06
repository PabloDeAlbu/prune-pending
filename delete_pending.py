#!/usr/bin/env python3

import os
import time
import subprocess
import argparse
from datetime import date

now = time.time()

parser = argparse.ArgumentParser(description='Remove files from /var/spool/sympa/subscribe/ older than 24 hs, by default')
parser.add_argument('--time-lapse',"-t", help='Number of hours required to delete a file', default="24")

folder = '/var/spool/sympa/subscribe/'

time_lapse = int(parser.parse_args().time_lapse)

print(str(date.today()) + f" - Deleting requests with more than {time_lapse} hours")
print("--------")
files = [os.path.join(folder, filename) for filename in os.listdir(folder)]
for filename in files:
    hs_lapse = (now - os.stat(filename).st_mtime) / 3600
    if (filename.endswith('add')) and ( hs_lapse > time_lapse):
        print('DELETE ' + filename)
        os.remove(filename)

print("--------")
print("Done")
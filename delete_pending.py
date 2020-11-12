#!/usr/bin/env python3

import os
import time
import subprocess

now = time.time()

folder = '/var/spool/sympa/subscribe/'

files = [os.path.join(folder, filename) for filename in os.listdir(folder)]
for filename in files:
    hs_lapse = (now - os.stat(filename).st_mtime) / 3600
    if (filename.endswith('add')) and ( hs_lapse > 24):
        os.remove(filename)
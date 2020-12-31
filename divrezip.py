#!/usr/bin/env python3

import subprocess
import os
import shutil
import sys
import multiprocessing

"""
This script generate multiple copies for repacking.

Usage:

divrezip.py [FALSE]
for not download use FALSE
"""

# CHECK THUS
rootdir = 'forR3'
CORES = multiprocessing.cpu_count()
TMPDIR = 'tmpdir'

#qname = 'pep5aa-r3'
replic = rootdir[-1]
RUNNER ='multirezipQ.py'
bucket_src = 'gs://sbglabdata/src'
# Download files
download_t = (RUNNER, 'keys.csv')

DL = True
if len(sys.argv)>1:
    DL = sys.argv[1]

if DL != 'FALSE':
    for down in download_t:
        getfiles = 'gsutil cp {}/{} .'.format(bucket_src, down)
        subprocess.run(getfiles, shell=True).check_returncode()


# Generate bash script for running
line1 = 'cd 1-R{}\npython3 {} &\n'.format(replic, RUNNER)
newlines = ''
for n in range(CORES-1):
    newlines+='cd ../{}-R{}\npython3 {} &\n'.format(n+2, replic, RUNNER)
alllines = line1 + newlines


def cpf(f, nd):
    shutil.copyfile(f, nd + os.sep + f)

# make core directories
os.mkdir(rootdir)
with open('{}{}runall.sh'.format(rootdir, os.sep), 'w') as fout:
    fout.write(alllines)

for core in range(CORES):
    new_dir = '{}{}{}-R{}'.format(rootdir, os.sep, core+1, replic)
    os.mkdir(new_dir)
    os.mkdir(new_dir + '/' + TMPDIR)
    cpf(RUNNER, new_dir)
    cpf('keys.csv', new_dir)

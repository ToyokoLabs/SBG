# Generate bash file to upload all tgz

import os

# divide pool
rootdir = 'all'
cores = 32
replic = X # EDIT!

# Generate bash script for uploading
line1 = 'cd 1-R{}\ngsutil cp *.tar.gz gs://sbglabdata/tripep\n'.format(replic)
newlines = ''
for n in range(cores-1):
    newlines+='cd ../{}-R{}\ngsutil cp *.tar.gz gs://sbglabdata/tripep\n'.format(n+2,replic)
uploadlines = line1 + newlines

with open('{}{}uploadall.sh'.format(rootdir, os.sep), 'w') as fout:
    fout.write(uploadlines)

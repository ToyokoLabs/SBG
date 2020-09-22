import os
import shutil
import sys

# divide pool
rootdir = 'all'
cores = 32
replic = sys.argv[1]

# Generate bash script
line1 = 'cd 1-R{}\npython3 runamber.py &\n'.format(replic)
newlines = ''
for n in range(cores-1):
    newlines+='cd ../{}-R{}\npython3 runamber.py &\n'.format(n+2,replic)
alllines = line1 + newlines


def cpf(f, nd):
    shutil.copyfile(f, nd + os.sep + f)

# make core directories
os.mkdir(rootdir)
with open('{}{}runall.sh'.format(rootdir, os.sep), 'w') as fout:
    fout.write(alllines)


for core in range(cores):
    new_dir = '{}{}{}-R{}'.format(rootdir, os.sep, core+1, replic)
    os.mkdir(new_dir)
    cpf('leaprc.ff14SB', new_dir)
    cpf('runamber.py', new_dir)
    cpf('min.1.in', new_dir)
    cpf('dmd.1.inp', new_dir)

core = 1
for line in open('tripept.txt'):
    mpr = '{}{}{}-R{}{}minipeprepo'.format(rootdir, os.sep, core, replic, 
                                          os.sep)
    with open(mpr, 'a') as mprfh:
        mprfh.write(line)
    core = 1 if core == cores else core+1

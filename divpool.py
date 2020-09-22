import os
import shutil

# divide pool
# Root dir
rootdir = 'all'
cores = 32
REPLIC = 1

def cpf(f, nd):
    shutil.copyfile(f, nd + os.sep + f)

# make core directories
os.mkdir(rootdir)
for core in range(cores):
    new_dir = '{}{}{}-R{}'.format(rootdir, os.sep, core+1, REPLIC)
    os.mkdir(new_dir)
    cpf('leaprc.ff14SB', new_dir)
    cpf('runamber.py', new_dir)
    cpf('min.1.in', new_dir)
    cpf('dmd.1.inp', new_dir)

core = 1
for line in open('tripept.txt'):
    mpr = '{}{}{}-R{}{}minipeprepo'.format(rootdir, os.sep, core, REPLIC, 
                                          os.sep)
    with open(mpr, 'a') as mprfh:
        mprfh.write(line)
    core = 1 if core == cores else core+1

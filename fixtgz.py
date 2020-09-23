import os

rootdir = 'all'
cores = 32
replic_number = X # EDIT!
dirname = os.path.basename(os.getcwd())

line1 = 'cd 1-R{}\nrm *.tar.gz\ntar -czf 1-R{}.tar.gz *-R{}.*.1.*\n'.format(
        replic_number, replic_number, replic_number)
newlines = ''
for n in range(cores-1):
    newlines+='cd ../{}-R{}\nrm *.tar.gz\ntar -czf {}-R{}.tar.gz *-R{}.*.1.*\n'.format(
        n+2, replic_number, n+2, replic_number, replic_number)
alllines = line1 + newlines


with open('{}{}fixtgz.sh'.format(rootdir, os.sep), 'w') as fout:
    fout.write(alllines)

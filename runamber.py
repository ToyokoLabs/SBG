import subprocess
import time
import logging
import os

dirname = os.path.basename(os.getcwd())
replic_number = dirname[-1]
logging.basicConfig(filename='runamber.log', filemode='w',
                    level=logging.INFO)
tleap_template = """source leaprc.ff14SB
peptide = sequence {0}
saveAmberParm peptide p.1.top p.1.crd
quit"""

def run_all(pep, nbr):
    """

    """
    pepname = pep.replace(' ', '')[1:-1]
    step1 = ('tleap', '-s', '-f', 'tleap.in')
    step2 = ('sander', '-O', '-i', 'min.1.in', '-o', 'min.1.out', 
            '-p', 'p.1.top', '-c', 'p.1.crd', '-r', 'min.1.crd')
    step3 = ('sander', '-O', '-i', 'dmd.1.inp', '-o', 
            '{}-R{}.dmd.1.out'.format(pepname, replic_number),
            '-p', 'p.1.top', '-c', 'min.1.crd', '-r', 
            '{}-R{}.prod.1.crd'.format(pepname, replic_number), '-x', 
            '{}-R{}.dmd.1.traj'.format(pepname, replic_number))
    subprocess.run(step1)
    time.sleep(.5)
    subprocess.run(step2)
    time.sleep(.5)
    logging.info("{} - Running ...{}".format(nbr+1, pep))
    subprocess.run(step3)

with open('minipeprepo') as peprepofh:
    for i, pep in enumerate(peprepofh):
        new_pep = pep.replace('\n', '')
        tleap = tleap_template.format(new_pep)
        with open('tleap.in', 'w') as tleapfh:
            tleapfh.write(tleap)
        run_all(new_pep, i) 
logging.info("END sander")
logging.info("Compressing...")
comp_stage = 'tar -czf {}.tar.gz *-R{}.*.1.*'.format(dirname, replic_number)
result = subprocess.run(comp_stage, shell=True)
subprocess.run(comp_stage, shell=True).check_returncode()
logging.info("Done")

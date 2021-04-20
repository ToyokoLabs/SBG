
# read peptides

class Parsedata():
    def __init__(self, filename):
        self.fn = filename
    
    def parse(self):
        with open(self.fn) as fh:
            lines = fh.readlines()
        for line in lines:
            if line.startswith('| Run on '):
                x = line.split(' ')
                self.date = x[3]
                self.time = x[5][:-1]
            elif line.startswith('|Largest sphere to fit in unit cell has radius ='):
                x = line.split('=')
                self.sphere_radius = x[1].strip()
            elif 'NATOM' in line and 'NTYPES' in line and 'NBONH' in line and 'MBONA' in line:
                x = line.split('=')
                self.natom = x.split('=')[1].split()[0]
                self.ntypes = x.split('=')[2].split()[0]


pd = Parsedata('NGLYASPCLEU-R1.dmd.1.out')
print(pd.parse())


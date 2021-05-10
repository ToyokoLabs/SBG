from protdata import _3_letter

from itertools import product


comb = product(_3_letter, repeat=3)

with open('all3pep', 'w') as fho:
    for c in comb:
        peptide = ''.join(c)
        canonical_name = peptide[:6] + 'C' + peptide[6:]
        fho.write(canonical_name+'\n')

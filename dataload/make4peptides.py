"""
Generate all 4 peptides
"""

from protdata import _3_letter
from itertools import product
from textwrap import wrap

comb = product(_3_letter, repeat=4)

with open('all4pep', 'w') as fho:
    for c in comb:
        peptide = ''.join(c)
        p1, p2, p3, p4 = wrap(peptide, 3)
        canonical_name = '{ N' + p1 + ' ' + p2 + ' ' + p3 + ' C' + p4 + ' }'
        fho.write(canonical_name+'\n')
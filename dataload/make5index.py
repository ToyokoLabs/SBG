"""
 make index tripeptides
"""

from itertools import product

_3_letter = ('ALA', 'CYS', 'ASP', 'GLU', 'PHE', 'GLY', 
             'HIS', 'ILE', 'LYS', 'LEU', 'MET', 'ASN', 
             'PRO', 'GLN', 'ARG', 'SER', 'THR', 'VAL', 
             'TRP', 'TYR')

BASEURL = 'https://toyokounqpeptides.s3.us-west-2.amazonaws.com/5pep/'

# Generate all tripeps
comb = product(_3_letter, repeat=5)

header = """<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8"></meta>
    <title>index of tri peptides</title>
    </head>
    <body>
"""

footer = "</body></html>"


with open('index.html', 'w') as fho:
    fho.write(header)
    for c in comb:
        peptide = ''.join(c)
        c_name = 'N' + peptide[:12] + 'C' + peptide[12:]
        link_1 = f'<a href="{BASEURL}{c_name}-R2.tar.bz2">{c_name}</a><br>'
        fho.write(link_1 + '\n')
    fho.write(footer)


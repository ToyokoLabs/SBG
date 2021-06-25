"""
 make index tripeptides
"""

from itertools import product

_3_letter = ('ALA', 'CYS', 'ASP', 'GLU', 'PHE', 'GLY', 
             'HIS', 'ILE', 'LYS', 'LEU', 'MET', 'ASN', 
             'PRO', 'GLN', 'ARG', 'SER', 'THR', 'VAL', 
             'TRP', 'TYR')

BASEURL = 'https://toyokounqpeptides.s3.us-west-2.amazonaws.com/tripep/'

# Generate all tripeps
comb = product(_3_letter, repeat=3)

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
        c_name = 'N' + peptide[:6] + 'C' + peptide[6:]
        rep = 1
        link_1 = f'<a href="{BASEURL}{c_name}-R{rep}.prod.1.crd">{c_name}-R{rep}.prod.1.crd</a><br>'
        link_2 = f'<a href="{BASEURL}{c_name}-R{rep}.dmd.1.out">{c_name}-{c_name}-R{rep}.dmd.1.out</a><br>'
        link_3 = f'<a href="{BASEURL}{c_name}-R{rep}.dmd.1.traj">{c_name}-{c_name}-R{rep}.dmd.1.traj</a><br>'
        rep = 2
        link_4 = f'<a href="{BASEURL}{c_name}-R{rep}.prod.1.crd">{c_name}-R{rep}.prod.1.crd</a><br>'
        link_5 = f'<a href="{BASEURL}{c_name}-R{rep}.dmd.1.out">{c_name}-{c_name}-R{rep}.dmd.1.out</a><br>'
        link_6 = f'<a href="{BASEURL}{c_name}-R{rep}.dmd.1.traj">{c_name}-{c_name}-R{rep}.dmd.1.traj</a><br>'
        fho.write(link_1+link_2+link_3+link_4+link_5+link_6+'\n')
    fho.write(footer)


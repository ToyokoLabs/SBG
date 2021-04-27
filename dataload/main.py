import getfiles, parsedata
import pandas as pd
from itertools import product

protein_letters_1to3 = {
    "A": "Ala",
    "C": "Cys",
    "D": "Asp",
    "E": "Glu",
    "F": "Phe",
    "G": "Gly",
    "H": "His",
    "I": "Ile",
    "K": "Lys",
    "L": "Leu",
    "M": "Met",
    "N": "Asn",
    "P": "Pro",
    "Q": "Gln",
    "R": "Arg",
    "S": "Ser",
    "T": "Thr",
    "V": "Val",
    "W": "Trp",
    "Y": "Tyr",
}

oneletter = []
for index in protein_letters_1to3:
    oneletter.append(protein_letters_1to3[index].upper())


comb = product(oneletter, repeat=3)

df_def = {'Name':[],
        'Maths':[],
        'Science':[]
       }
  
df = pd.DataFrame(df_def)

gf = getfiles.Getfiles3pep()
count = 0
with open('resfile.csv', 'a') as fhout:
    for c in comb:
        count +=1
        peptide = ''.join(c)
        xx = gf.get(peptide[:6] + 'C' + peptide[6:])
        for idx in range(5):
            pd = parsedata.Parsedata(xx[idx].split('\n'))
            pd.parse()
            print(peptide)
            #print(pd.allvars)
            df.loc[len(df.index)] = pd.allvars[:3]
            #fhout.write('\t'.join(pd.allvars) + '\n')
        if count == 3:
            print(df)
            break
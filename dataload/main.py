import getfiles, parsedata
import pandas as pd
from itertools import product
from protdata import three_letter, df_def


comb = product(three_letter, repeat=3)
  
df = pd.DataFrame(df_def)

gf = getfiles.Getfiles3pep()
count = 0
for c in comb:
    count +=1
    peptide = ''.join(c)
    reps = gf.get(peptide[:6] + 'C' + peptide[6:])
    for rep in reps:
        pd = parsedata.Parsedata(rep.split('\n'))
        pd.parse()
        #print(peptide)
        df.loc[len(df.index)] = pd.allvars[:3]
    if count == 50:
        #print(df)
        break

df.to_pickle('tripepts.pkl')
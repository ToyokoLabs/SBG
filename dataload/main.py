import getfiles, parsedata
import pandas as pd
from itertools import product
from protdata import three_letter, df_def


comb = product(three_letter, repeat=3)
  
df = pd.DataFrame(df_def)
df[['replica', 'natom', 'nbonh']] = df[['replica', 'natom', 'nbonh']].astype(int)

gf = getfiles.Getfiles3pep()
count = 0
for c in comb:
    count +=1
    peptide = ''.join(c)
    canonical_name = peptide[:6] + 'C' + peptide[6:]
    reps = gf.get(canonical_name)
    for n, rep in enumerate(reps):
        pd = parsedata.Parsedata(rep.split('\n'))
        pd.parse()
        df.loc[len(df.index)] = [canonical_name, int(n+1)] + pd.allvars
    if count == 3:
        print(df)
        #df[['replica']] = df[['replica']].astype(int)
        print(df.dtypes)
        break

df.to_pickle('tripepts.pkl')
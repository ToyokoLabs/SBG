import getfiles, parsedata
import pandas as pd
from itertools import product
from protdata import _3_letter, df_def


peprepo = 'all3pep'
count = 4200

with open(peprepo) as fhi:
    peps = fhi.readlines()

# skip to count
peps = peps[count+1:]
peps = map(str.strip, peps)

df = pd.DataFrame(df_def, index=[])
gf = getfiles.Getfiles3pep()

# METASNCGLU

#reps = gf.get('METASNCPHE')
#pd = parsedata.Parsedata(reps[1].split('\n'))
#pd.parse()

for pep in peps:
    count += 1
    reps = gf.get(pep)
    #import pdb; pdb.set_trace()
    for n, rep in enumerate(reps):
        pd = parsedata.Parsedata(rep.split('\n'))
        try:
            pd.parse()
        except:
            with open('errors', 'a') as efo:
                ename = 'N' + pep + '-R{}.dmd.1.out'.format(n+1)
                efo.write(ename)
            print('ERROR IN ' + ename)
            continue
        df.loc[len(df.index)] = [pep, int(n+1)] + pd.allvars
    if count % 100 == 0:
        df.to_pickle('tripepts3.pkl')
    print(pep)

df.to_pickle('tripepts3.pkl')

# File Descriptions

The dataset is composed of tar.bz2 files with the following name convention:

N[1]C[2]-R[3].tar.bz2 where:

1. First 4 Amino Acids (or 2 for tripeptide) using IUPAC three letter notation.
2. Last Amino Acid using IUPAC three letter notation
3. Replica number from 1 to 3.

For example, a valid file is: **NVALALAPROALACTHR-R3.tar.bz2**

Inside each tarball, there are up to 4 files:

1. out file: TEXT. Output of Sander, it includes information on the running parameters (like NVALALAPROALACTHR-R3.dmd.1.out)
2. traj file: BINARY. Trajectory file from Sander (like NVALALAPROALACTHR-R3.dmd.1.traj)
3. crd file: BINARY. Coordinate file from Sander  (like NVALALAPROALACTHR-R3.prod.1.crd)
4. top file TEXT Topology file from Tleap (like p.1.top). **Note:** This file is not present in R1 packages.

# File location

For tripeptides, each file is stored as they were generated, for ALAALACALA, this is the *out file*:

https://toyokounqpeptides.s3-us-west-2.amazonaws.com/tripep/NALAALACALA-R1.dmd.1.out


For pentapeptides, each run data is compressed in a tar.bz2 file.

for ALA-ALA-ALA-ALA-ALA, replica 1:

https://toyokounqpeptides.s3-us-west-2.amazonaws.com/5pep/NALAALAALAALACALA-R1.tar.bz2



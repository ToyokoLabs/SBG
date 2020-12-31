
# File Descriptions

The dataset is composed of tar.bz2 files with the following name convention:

N[1]C[2]-R[3].tar.bz2 where:

1. First Amino Acids using IUPAC three letter notation.
2. Last Amino Acid using IUPAC three letter notation
3. Replica number from 1 to 3.

For example, a valid file is: **NVALALAPROALACTHR-R3.tar.bz2**

Inside each tarball, there are up to 4 files:

1. out file: TEXT. Output of Sander, it includes information on the running parameters (like NVALALAPROALACTHR-R3.dmd.1.out)
2. traj file: BINARY. Trajectory file from Sander (like NVALALAPROALACTHR-R3.dmd.1.traj)
3. crd file: BINARY. Coordinate file from Sander  (like NVALALAPROALACTHR-R3.prod.1.crd)
4. top file TEXT Topology file from Tleap (like p.1.top). **Note:** This file is not present in R1 packages.


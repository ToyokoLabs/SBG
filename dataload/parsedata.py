# read peptides

class Parsedata():
    def __init__(self, lines):
        self.lines = lines

    def parse(self):
        ave_steps = False
        nstep0 = False
        nstep500000 = False
        nstep1000000 = False
        for line in self.lines:
            if line.startswith('|Largest sphere to fit in unit cell has radius ='):
                x = line.split('=')
                self.sphere_radius = float((x[1].strip()))
            elif 'NSTEP=0' in line.replace(' ', '') and nstep0 == False:
                nstep0 = True
                self.timeps0 = float(line.replace(" ","").split('=')[2][:-7])
                self.tempk0 = float(line.replace(" ","").split('=')[3].replace("PRESS", ''))
                self.press0 = float(line.replace(" ","").split('=')[4])
            elif nstep0 == True and line.strip().startswith('Etot'):
                self.etot0 = float(line.replace(' ','').split('=')[1].replace('EKtot', ''))
                self.ektot0 = float(line.replace(' ','').split('=')[2].replace('EPtot', ''))
                self.eptot0 = float(line.replace(' ','').split('=')[3])
            elif nstep0 == True and line.strip().startswith('BOND'):
                self.bond0 = float(line.replace(' ','').split('=')[1].replace('ANGLE', ''))
                self.angle0 = float(line.replace(' ','').split('=')[2].replace('DIHED', ''))
                self.dihed0 = float(line.replace(' ','').split('=')[3])
            elif nstep0 == True and line.strip().startswith('1-4 NB'):
                self.one4NB0 = float(line.replace(' ','').split('=')[1].replace('1-4EEL', ''))
                self.one4EEL0 = float(line.replace(' ','').split('=')[2].replace('VDWAALS', ''))
                self.VDWAALS0 = float(line.replace(' ','').split('=')[3])
            elif nstep0 == True and line.strip().startswith('EELEC'):
                self.EELEC0 = float(line.replace(' ','').split('=')[1].replace('EHBOND', ''))
                self.EHBOND0 = float(line.replace(' ','').split('=')[2].replace('RESTRAINT', ''))
                self.RESTRAINT0 = float(line.replace(' ','').split('=')[3])
                nstep0 = False
            elif 'NSTEP=500000' in line.replace(' ', ''):
                nstep500000 = True
                self.timeps500000 = float(line.replace(" ","").split('=')[2][:-7])
                self.tempk500000 = float(line.replace(" ","").split('=')[3].replace("PRESS", ''))
                self.press500000 = float(line.replace(" ","").split('=')[4])
            elif nstep500000 == True and line.strip().startswith('Etot'):
                self.etot500000 = float(line.replace(' ','').split('=')[1].replace('EKtot', ''))
                self.ektot500000 = float(line.replace(' ','').split('=')[2].replace('EPtot', ''))
                self.eptot500000 = float(line.replace(' ','').split('=')[3])
            elif nstep500000 == True and line.strip().startswith('BOND'):
                self.bond500000 = float(line.replace(' ','').split('=')[1].replace('ANGLE', ''))
                self.angle500000 = float(line.replace(' ','').split('=')[2].replace('DIHED', ''))
                self.dihed500000 = float(line.replace(' ','').split('=')[3])
            elif nstep500000 == True and line.strip().startswith('1-4 NB'):
                self.one4NB500000 = float(line.replace(' ','').split('=')[1].replace('1-4EEL', ''))
                self.one4EEL500000 = float(line.replace(' ','').split('=')[2].replace('VDWAALS', ''))
                self.VDWAALS500000 = float(line.replace(' ','').split('=')[3])
            elif nstep500000 == True and line.strip().startswith('EELEC'):
                self.EELEC500000 = float(line.replace(' ','').split('=')[1].replace('EHBOND', ''))
                self.EHBOND500000 = float(line.replace(' ','').split('=')[2].replace('RESTRAINT', ''))
                self.RESTRAINT500000 = float(line.replace(' ','').split('=')[3])
                nstep500000 = False
            elif 'NSTEP=1000000' in line.replace(' ', '') and ave_steps==False:
                nstep1000000 = True
                self.timeps1000000 = float(line.replace(" ","").split('=')[2][:-7])
                self.tempk1000000 = float(line.replace(" ","").split('=')[3].replace("PRESS", ''))
                self.press1000000 = float(line.replace(" ","").split('=')[4])
            elif nstep1000000 == True and line.strip().startswith('Etot'):
                self.etot1000000 = float(line.replace(' ','').split('=')[1].replace('EKtot', ''))
                self.ektot1000000 = float(line.replace(' ','').split('=')[2].replace('EPtot', ''))
                self.eptot1000000 = float(line.replace(' ','').split('=')[3])
            elif nstep1000000 == True and line.strip().startswith('BOND'):
                self.bond1000000 = float(line.replace(' ','').split('=')[1].replace('ANGLE', ''))
                self.angle1000000 = float(line.replace(' ','').split('=')[2].replace('DIHED', ''))
                self.dihed1000000 = float(line.replace(' ','').split('=')[3])
            elif nstep1000000 == True and line.strip().startswith('1-4 NB'):
                self.one4NB1000000 = float(line.replace(' ','').split('=')[1].replace('1-4EEL', ''))
                self.one4EEL1000000 = float(line.replace(' ','').split('=')[2].replace('VDWAALS', ''))
                self.VDWAALS1000000 = float(line.replace(' ','').split('=')[3])
            elif nstep1000000 == True and line.strip().startswith('EELEC'):
                self.EELEC1000000 = float(line.replace(' ','').split('=')[1].replace('EHBOND', ''))
                self.EHBOND1000000 = float(line.replace(' ','').split('=')[2].replace('RESTRAINT', ''))
                self.RESTRAINT1000000 = float(line.replace(' ','').split('=')[3])
                nstep1000000 = False                

            elif 'NATOM' in line and 'NTYPES' in line and 'NBONH' in line and 'MBONA' in line:
                x = line.split('=')
                self.natom = int(x[1].split()[0])
                self.ntypes = int(x[2].split()[0])
                self.nbonh = int(x[3].split()[0])
                self.mbona = int(x[4].split()[0])
            elif 'NTHETH' in line and 'MTHETA' in line and 'NPHIH'in line and 'MPHIA'in line:
                x = line.split('=')
                self.ntheth = int(x[1].split()[0])
                self.mtheta = int(x[2].split()[0])
                self.nphih = int(x[3].split()[0])
                self.mphia = int(x[4].split()[0])
            elif 'NHPARM' in line and 'NPARM' in line and 'NNB'in line and 'NRES'in line:
                x = line.split('=')
                self.nhparm = int(x[1].split()[0])
                self.nparm = int(x[2].split()[0])
                self.nnb = int(x[3].split()[0])
                self.nres = int(x[4].split()[0])
            elif 'NBONA' in line and 'NTHETA' in line and 'NPHIA'in line and 'NUMBND'in line:
                x = line.split('=')
                self.nbona = int(x[1].split()[0])
                self.ntheta = int(x[2].split()[0])
                self.nphia = int(x[3].split()[0])
                self.numbnd = int(x[4].split()[0])
            elif 'NUMANG' in line and 'NPTRA' in line and 'NATYP'in line and 'NPHB'in line:
                x = line.split('=')
                self.numang = int(x[1].split()[0])
                self.nptra = int(x[2].split()[0])
                self.natyp = int(x[3].split()[0])
                self.nphb = int(x[4].split()[0])
            elif 'IFBOX' in line and 'NMXRS' in line and 'IFCAP'in line and 'NEXTRA'in line:
                x = line.split('=')
                self.ifbox = int(x[1].split()[0])
                self.nmxrs = int(x[2].split()[0])
                self.ifcap = int(x[3].split()[0])
                self.nextra = int(x[4].split()[0])
            elif 'NCOPY' in line:
                x = line.split('=')
                self.ncopy = int(x[1].split()[0])
            elif 'imin' in line and 'nmropt' in line:
                x = line.split(',')
                self.imin = int(x[0].split()[2])
                self.nmropt = int(x[1].split()[2])
            elif 'ntx' in line and 'irest' in line and 'ntrx' in line:
                x = line.split(',')
                self.ntx = int(x[0].split()[2])
                self.irest = int(x[1].split()[2])
                self.ntrxi = int(x[2].split()[2])
            elif 'ntxo' in line and 'ntpr' in line and 'ntrx' and line and 'ntwr' in line:
                x = line.split(',')
                self.ntxo = int(x[0].split()[2])
                self.ntpr = int(x[1].split()[2])
                self.ntrxo = int(x[2].split()[2])
                self.ntwr = int(x[3].split()[2])
            elif 'iwrap' in line and 'ntwx' in line and 'ntwv' and line and 'ntwe' in line:
                x = line.split(',')
                self.iwrap = int(x[0].split()[2])
                self.ntwx = int(x[1].split()[2])
                self.ntwv = int(x[2].split()[2])
                self.ntwe = int(x[3].split()[2])
            elif 'ioutfm' in line and 'ntwprt' in line and 'idecomp' and line and 'rbornstat' in line:
                x = line.split(',')
                self.ioutfm = int(x[0].split()[2])
                self.ntwprt = int(x[1].split()[2])
                self.idecomp = int(x[2].split()[2])
                self.rbornstat = int(x[3].split()[1])
            elif 'ntf' in line and 'ntb' in line and 'igb' and line and 'nsnb' in line:
                x = line.split(',')
                self.ntf = int(x[0].split()[2])
                self.ntb = int(x[1].split()[2])
                self.igb = int(x[2].split()[2])
                self.nsnb = int(x[3].split()[2])
            elif 'ipol' in line and 'gbsa' in line and 'iesp' in line:
                x = line.split(',')
                self.ipol = int(x[0].split()[2])
                self.gbsa = int(x[1].split()[2])
                self.iesp = int(x[2].split()[2])
            elif 'dielc' in line and 'cut' in line and 'intdiel' in line:
                x = line.split(',')
                self.dielc = float(x[0].split()[2])
                self.cut = float(x[1].split()[2])
                self.intdiel = float(x[2].split()[2])
            elif 'ibelly' in line and 'ntr' in line:
                x = line.split(',')
                self.ibelly = int(x[0].split()[2])
                self.ntr = int(x[1].split()[2])
            elif 'nstlim' in line and 'nscm' in line and 'nrespa' in line:
                x = line.split(',')
                self.nstlim = int(x[0].split()[2])
                self.nscm = int(x[1].split()[2])
                self.nrespa = int(x[2].split()[2])
            elif 't' in line and 'dt' in line and 'vlimit' in line:
                x = line.split(',')
                self.t = float(x[0].split()[2])
                self.dt = float(x[1].split()[2])
                self.vlimit = float(x[2].split()[2])
            elif 'ig ' in line:
                x = line.split('=')
                self.ig = float(x[1].split()[0])
            elif 'temp0' in line and 'tempi' in line and 'gamma_ln' in line:
                x = line.split(',')
                self.temp0 = float(x[0].split()[2])
                self.tempi = float(x[1].split()[2])
                self.gamma_ln = float(x[2].split()[1])
            elif 'ntc' in line and 'jfastw' in line:
                x = line.split(',')
                self.ntc = int(x[0].split()[2])
                self.jfastw = int(x[1].split()[2])
            elif 'tol' in line:
                x = line.split('=')
                self.tol = float(x[1].split()[0])
            elif 'Sum of charges from parm topology file' in line:
                x = line.split('=')
                self.sum_charges = float(x[1].split()[0])
            elif '# of SOLUTE  degrees of freedom (RNDFP)' in line:
                x = line.split(':')
                self.rndfp = int(x[1].split('.')[0].strip())
            elif '# of SOLVENT degrees of freedom (RNDFS)' in line:
                x = line.split(':')
                self.rndfs = int(x[1].split('.')[0].strip())
            elif 'NDFMIN' in line and 'NUM_NOSHAKE' in line and 'CORRECTED RNDFP' in line:
                x = line.split('=')
                self.ndfmin = int(x[1].split()[0].replace('.',''))
                self.num_noshake = int(x[2].split()[0].replace('.',''))
                self.corrected_rndfp = int(x[3].split()[0].replace('.',''))
            elif 'TOTAL # of degrees of freedom (RNDF)' in line:
                x = line.split('=')
                self.rndf = int(x[1].split('.')[0].strip())
            elif 'Local SIZE OF NONBOND LIST' in line:
                x = line.split('=')
                self.local_nonbond = int(x[1].strip())
            elif 'TOTAL SIZE OF NONBOND LIST' in line:
                x = line.split('=')
                self.total_nonbond = int(x[1].split('.')[0].strip())
            elif 'A V E R A G E S   O V E R 1000000 S T E P S' in line:
                ave_steps = True
            elif 'R M S  F L U C T U A T I O N S' in line:
                ave_steps = False
            elif 'NSTEP' in line and 'TIME(PS)' in line and 'TEMP(K)' in line and 'PRESS' in line and ave_steps==True:
                x = line.split('=')
                self.avg_nstep = float(x[1].split()[0])
                self.avg_time_ps = float(x[2].split()[0])
                self.avg_temp_k = float(x[3].split()[0])
                self.avg_press = float(x[4].strip())
            elif 'Etot' in line and 'EKtot' in line and 'EPtot' in line and ave_steps==True:
                x = line.split('=')
                self.avg_etot = float(x[1].split()[0])
                self.avg_ektot = float(x[2].split()[0])
                self.avg_eptot = float(x[3].strip())
            elif 'BOND' in line and 'ANGLE' in line and 'DIHED' in line and ave_steps==True:
                x = line.split('=')
                self.avg_bond = float(x[1].split()[0])
                self.avg_angle = float(x[2].split()[0])
                self.avg_dihed = float(x[3].strip())
            elif 'NB' in line and 'EEL' in line and 'VDWAALS' in line and ave_steps==True:
                x = line.split('=')
                self.avg_nb = float(x[1].split()[0])
                self.avg_eel = float(x[2].split()[0])
                self.avg_vdwaals = float(x[3].strip())
            elif 'EELEC' in line and 'EHBOND' in line and 'RESTRAINT' in line and ave_steps==True:
                x = line.split('=')
                self.avg_eelec = float(x[1].split()[0])
                self.avg_ehbond = float(x[2].split()[0])
                self.avg_restraint = float(x[3].split()[0])
            elif 'NSTEP' in line and 'TIME(PS)' in line and 'TEMP(K)' in line and 'PRESS' in line and ave_steps==False:
                x = line.split('=')
                self.rmsf_nstep = float(x[1].split()[0])
                self.rmsf_time_ps = float(x[2].split()[0])
                self.rmsf_temp_k = float(x[3].split()[0])
                self.rmsf_press = float(x[4].strip())
            elif 'Etot' in line and 'EKtot' in line and 'EPtot' in line and ave_steps==False:
                x = line.split('=')
                self.rmsf_etot = float(x[1].split()[0])
                self.rmsf_ektot = float(x[2].split()[0])
                self.rmsf_eptot = float(x[3].strip())
            elif 'BOND' in line and 'ANGLE' in line and 'DIHED' in line and ave_steps==False:
                x = line.split('=')
                self.rmsf_bond = float(x[1].split()[0])
                self.rmsf_angle = float(x[2].split()[0])
                self.rmsf_dihed = float(x[3].strip())
            elif 'NB' in line and 'EEL' in line and 'VDWAALS' in line and ave_steps==False:
                x = line.split('=')
                self.rmsf_nb = float(x[1].split()[0])
                self.rmsf_eel = float(x[2].split()[0])
                self.rmsf_vdwaals = float(x[3].strip())
            elif 'EELEC' in line and 'EHBOND' in line and 'RESTRAINT' in line and ave_steps==False:
                x = line.split('=')
                self.rmsf_eelec = float(x[1].split()[0])
                self.rmsf_ehbond = float(x[2].split()[0])
                self.rmsf_restraint = float(x[3].split()[0])
        self.allvars = [self.sphere_radius, self.natom, self.ntypes, self.nbonh, self.mbona,
            self.ntheth, self.mtheta, self.nphih, self.mphia, self.nhparm, self.nparm, self.nnb, self.nres, self.nbona,
            self.ntheta, self.nphia, self.numbnd, self.numang, self.nptra, self.natyp, self.nphb, self.ifbox, self.nmxrs,
            self.ifcap, self.nextra, self.ncopy, self.imin, self.nmropt, self.ntx, self.irest, self.ntrxi, self.ntxo,
            self.ntpr, self.ntrxo, self.ntwr, self.iwrap, self.ntwx, self.ntwv,self.ntwe, self.ioutfm,self.ntwprt,
            self.idecomp, self.rbornstat, self.ntf, self.ntb, self.igb, self.nsnb, self.ipol, self.gbsa, self.iesp,
            self.dielc, self.cut, self.intdiel, self.ibelly, self.ntr, self.nstlim, self.nscm, self.nrespa, self.t,
            self.dt, self.vlimit, self.ig, self.temp0, self.tempi, self.gamma_ln, self.ntc, self.jfastw, self.tol,
            self.sum_charges, self.rndfp, self.rndfs, self.ndfmin, self.num_noshake, self.corrected_rndfp, self.rndf,
            self.local_nonbond, self.total_nonbond, self.avg_nstep, self.avg_time_ps, self.avg_temp_k, self.avg_press,
            self.avg_etot, self.avg_ektot, self.avg_eptot, self.avg_bond, self.avg_angle, self.avg_dihed, self.avg_nb,
            self.avg_eel, self.avg_vdwaals, self.avg_eelec, self.avg_ehbond, self.avg_restraint, self.rmsf_nstep,
            self.rmsf_time_ps, self.rmsf_temp_k, self.rmsf_press, self.rmsf_etot, self.rmsf_ektot, self.rmsf_eptot,
            self.rmsf_bond, self.rmsf_angle, self.rmsf_dihed, self.rmsf_nb, self.rmsf_eel, self.rmsf_vdwaals,
            self.rmsf_eelec, self.rmsf_ehbond, self.rmsf_restraint,
            self.timeps0, self.tempk0, self.press0, self.etot0,self.ektot0,self.eptot0,self.bond0,self.angle0,
            self.dihed0, self.one4NB0, self.one4EEL0,self.VDWAALS0,
            self.EELEC0, self.EHBOND0, self.RESTRAINT0,
            self.timeps500000, self.tempk500000, self.press500000, self.etot500000, self.ektot500000,self.eptot500000,
            self.bond500000, self.angle500000, self.dihed500000, self.one4NB500000, self.one4EEL500000,self.VDWAALS500000,
            self.EELEC500000, self.EHBOND500000,self.RESTRAINT500000,
            self.timeps1000000, self.tempk1000000, self.press1000000, self.etot1000000, self.ektot1000000,
            self.eptot1000000, self.bond1000000, self.angle1000000, self.dihed1000000, self.one4NB1000000,
            self.one4EEL1000000, self.VDWAALS1000000,
            self.EELEC1000000, self.EHBOND1000000, self.RESTRAINT1000000,
        ]


#pd = Parsedata('NARGSERCVAL-R4.dmd.1.out')
#pd.parse()



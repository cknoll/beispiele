# -*- coding: utf-8 -*-
from ipHelp import IPS, ST, ip_syshook, dirsearch, sys
import os

#/home/ck/workstickdir/latex/verwaltet/100_Diss/bilder/double_mass_spring.pdf
#/home/ck/workstickdir/latex/verwaltet/100_Diss/bilder/kettenpendel_def.pdf
#/home/ck/workstickdir/latex/verwaltet/100_Diss/bilder/manipulator_def.pdf
#/home/ck/workstickdir/latex/verwaltet/100_Diss/bilder/paralleles_2fachpendel.pdf
#/home/ck/workstickdir/latex/verwaltet/100_Diss/bilder/pendel_wagen.pdf
fnames ="""\
/home/ck/workstickdir/latex/verwaltet/100_Diss/bilder/pendel_wagen_feder_wagen.pdf
/home/ck/workstickdir/latex/verwaltet/100_Diss/bilder/planar_verschieb_pendel_elast_masse.pdf
/home/ck/workstickdir/latex/verwaltet/100_Diss/bilder/taxo_flachheit_steuerbarkeit.pdf
/home/ck/workstickdir/latex/verwaltet/100_Diss/bilder/taxo_flachheit_unklarheit.pdf
/home/ck/workstickdir/latex/verwaltet/100_Diss/bilder/manipulator_def2.pdf
/home/ck/workstickdir/latex/verwaltet/100_Diss/bilder/unicycle.pdf\
""".split("\n")


cmd = "convert -density 150 %s images/%s"
#cmd = "convert %s images/%s"

for f in fnames:
        new_fname = os.path.split(f)[-1].replace('pdf', 'png')
        cmd1 = cmd %(f, new_fname)
        os.system(cmd1)
        print new_fname
    
    
    


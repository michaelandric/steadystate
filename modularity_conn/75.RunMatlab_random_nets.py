#!/usr/bin/python

import sys
import subprocess 
import time

matlab_script = sys.argv[1]
print matlab_script
print time.strftime('%c')

subject = sys.argv[2]
cond = sys.argv[3]
nn = 1   # start
ee = 101   # end
#print 'matlab_2010 -nodisplay -nosplash -nojvm -nodesktop -r "'+matlab_script.split('.')[0]+'(\''+subject+'\','+`cond`+','+`nn`+','+`ee`+'); exit; quit"'

subprocess.call('matlab_2010 -nodisplay -nosplash -nojvm -nodesktop -r "'+matlab_script.split('.')[0]+'(\''+subject+'\','+`cond`+','+`nn`+','+`ee`+'); exit; quit"', shell = True)


#matlab_2010 -nodisplay -nosplash -nodesktop -r "test_script_rand; exit; quit"

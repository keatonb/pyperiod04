#! /usr/bin/env python

import os
import numpy as np

def ft(lc,lcfile='temp.lc',ftfile='temp.ft',batchfile='temp.bat',
    ftmin='0',ftmax='nyq'):
    """Return FT calculated by Period04 as Numpy array.
    
    lc is array-like with columns time and relative flux.
    Frequencies are in units of 1/[time unit used in lc]
    High FT resolution default is only available in P04 batch mode.
    """
    
    #Ensure FT range is given as stringe
    ftmin=str(ftmin)
    ftmax=str(ftmax)
    
    #Write out the light curve file
    np.savetxt(lcfile,lc)
    
    #Write the P04 batch file
    f = open(batchfile,'w')
    f.write('import to '+lcfile+'\n')
#    f.write('fourier '+ftmin+' '+ftmax+' o n\n')
    f.write('savefourier '+ftmin+' '+ftmax+' o n '+ftfile+'\n')
    f.write('exit\n')
    f.close()
    
    #Run the batch file
    os.system('period04 -batch='+batchfile)
    
    #Read in the FT
    ft = np.loadtxt(ftfile)
    
    #Clean up any temporary files
    if lcfile == 'temp.lc': os.remove(lcfile)
    if ftfile == 'temp.ft': os.remove(ftfile)
    if batchfile == 'temp.bat': os.remove(batchfile)
    
    #Return the FT
    return ft


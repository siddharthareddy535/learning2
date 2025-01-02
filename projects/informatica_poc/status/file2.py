import pandas as pd
from datetime import datetime
from dateutil.relativedelta import relativedelta
import sys 
from utils import *


keep_columns1=['lfcobjid' ,'tbl' ,'subkey' ,'excmdecd']
keep_columns2=['lfcobjid','inrid' ,'tbl' ,'subkey' ,'excmdecd']
keep_columns3=['lfcobjid' ,'inrid','tbl' ,'subkey' ,'excmdecd']

def grid_func(df):
    res=[]
    for index, row in df.iterrows():
        lvl = row['lvl'].upper()

        if lvl == 'PMR':
            if '-' not in str(row['inrid']):
                row['output_table']='grd'
            else:
                row['output_table']='inr'
        elif lvl == 'ATY':
            row['output_table']='aty'
        res.append(row)
    
    return res

ctmspmr= pd.read_csv('ctmspmr.csv')
data = grid_func(ctmspmr)
df=pd.DataFrame(data)
grd=df[df['output_table'] == 'grd']
inr= df[df['output_table'] == 'inr']
aty= df[df['output_table'] == 'aty']
grd=grd[keep_columns1]
inr=inr[keep_columns2]
aty=aty[keep_columns3]



if syserr or sysinfo:
    print(">>> Error downloading ctmspmr.")
    REM_MSG = "Error downloading CTMSPMR."
    REM_RC = 3
    sys.stdout.write(f"REM_MSG: {REM_MSG}\n")
    sys.stdout.write(f"REM_RC: {REM_RC}\n")


if syserr or sysinfo:
    print(">>> Error downloading ctmsinr.")
    REM_MSG = "Error downloading CTMSINR."
    REM_RC = 4
    sys.stdout.write(f"REM_MSG: {REM_MSG}\n")
    sys.stdout.write(f"REM_RC: {REM_RC}\n")





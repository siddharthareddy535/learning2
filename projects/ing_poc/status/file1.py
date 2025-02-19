#sasFilePath: fwrite_test.sas
#conversionTime: 11/13/2024 10:43:29
#linesInFile: 27 #linesOfCode: 19 #linesOfPython: 27
#complexity: 1 #processedBlocks: 1 #passedBlocks: 1
#failedBlocks: 0 #totalErrors: 0


#%%
scriptName='fwrite_test'
import pandas as pd
from datetime import datetime
from dateutil.relativedelta import relativedelta
from utils import *

#%%
START_BLOCK('Passed DataStep', '1:4384623882865929002 - Lines: 21 - 6 to 27 : 96% ')
def updated():
    pass
result = getdf('result')
def _null__func(df, row=None):
    putBuffer=''
    #FILE tpdet
    f = open(tpdet, "a")
    f.write(put([
    'o=1', row['def_id'],
    'o=251',
    'CUSTODY INSTRUCTIONS',
    'o=276', row['revaccid'],
    'o=281', row['egbsetid'],
    'o=311', row['sllid'],
    'o=316', row['rsatypcd'],
    'o=317', row['srvlvid'],
    'o=318', row['trsid'],
    'o=325', row['isisecid'],
    'o=337', row['cmosecid'],
    'o=362', begdt_formatudf(row['sdate.']),
    'o=372', row['cevtypid'],
    'o=375', ib4_formatudf(row['cevct']),
    'o=379',
    'CUSTODY INSTRUCTION TYPE',
    'o=403', row['oper']]) + "\n")
    f.close()
    return row
result_tmp = getdf('result')
nulldf = result_tmp.apply(lambda row: _null__func(None, row ), axis=1)
END_BLOCK('Passed DataStep', '1:4384623882865929002')

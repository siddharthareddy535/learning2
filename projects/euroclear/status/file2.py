#sasFilePath: if_else.sas
#conversionTime: 11/13/2024 05:36:21
#linesInFile: 52 #linesOfCode: 28 #linesOfPython: 33
#complexity: 2 #processedBlocks: 4 #passedBlocks: 4
#failedBlocks: 0 #totalErrors: 0


#%%
scriptName='if_else'
import pandas as pd
from datetime import datetime
from dateutil.relativedelta import relativedelta
from utils import *

#%%
START_BLOCK('Passed DataStep', '1:4662118624581971203 - Lines: 22 - 6 to 28 : 52% ')
ctmspmr = getdf('ctmspmr')
def updated_file_2():
    pass
ctmspmr['a'] = 1
mapDFs['ctmspmr'] = ctmspmr
def grd_func(df, row=None):
    res = []
    if (upcaseudf(row['lvl']) == 'PMR'):
        if verify(row['inrid'], '-') == 0:
            row['output_table'] = 'grd'
            res.append(row.to_dict().copy())
        else:
            row['output_table'] = 'inr'
            res.append(row.to_dict().copy())
    elif (upcaseudf(row['lvl']) == 'ATY'):
        row['output_table'] = 'aty'
        res.append(row.to_dict().copy())
    return res
ctmspmr_tmp = getdf('ctmspmr')
grd = ctmspmr_tmp.apply(lambda row: grd_func(None, row ), axis=1)
grd_base  = pandas.createPandasDFFromDicts(grd)
grd = cxt.getOutputDF(grd_base, 'grd')
inr = cxt.getOutputDF(grd_base, 'inr')
aty = cxt.getOutputDF(grd_base, 'aty')
grd = keepColumns(grd, ['lfcobjid','tbl','subkey','excmdecd'])
inr = keepColumns(inr, ['lfcobjid','inrid','tbl','subkey','excmdecd'])
aty = keepColumns(aty, ['lfcobjid','inrid','tbl','subkey','excmdecd'])
END_BLOCK('Passed DataStep', '1:4662118624581971203')

#%%
START_BLOCK('Passed IFBLOCK', '2:4662118624581971203 - Lines: 10 - 29 to 39 : 73% ')
if (syserr or
 sysinfo
):
    {sysrput()}, rem_msg
    {sysrput()}, rem_rc
END_BLOCK('Passed IFBLOCK', '2:4662118624581971203')

#%%
if (syserr or
 sysinfo
):
    '{sysrput()}, rem_msg == '', error, downloading, ctmsinr.'
    '{sysrput()}, rem_rc'

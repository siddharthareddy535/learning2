#sasFilePath: call_module.sas
#conversionTime: 11/13/2024 09:30:42
#linesInFile: 40 #linesOfCode: 30 #linesOfPython: 35
#complexity: 2 #processedBlocks: 1 #passedBlocks: 1
#failedBlocks: 0 #totalErrors: 0


#%%
scriptName='call_module'
import pandas as pd
from datetime import datetime
from dateutil.relativedelta import relativedelta
from utils import *

#%%
START_BLOCK('Passed DataStep', '1:7733365795752897369 - Lines: 34 - 6 to 40 : 97% ')
retainVars = {}
retainVars['p_len'] = '001'
retainVars['p_mod'] = 'csi'
retainVars['p_rtc'] = '9'
retainVars['p_gen'] = 'gs'
retainVars['p_key'] = ''
retainVars['pgnb'] = _pgmno
def mcid_func(retainVars = retainVars):
    row['p_len'] = retainVars['p_len']
    row['p_mod'] = retainVars['p_mod']
    row['p_rtc'] = retainVars['p_rtc']
    row['p_gen'] = retainVars['p_gen']
    row['p_key'] = retainVars['p_key']
    row['pgnb'] = retainVars['pgnb']
    res = []
    row['str1'] = ''
    row['str2'] = ''
    row['str3'] = ''
    row['str4'] = ''
    row['iostr5'] = ''smKMAFKLMQDA;LVMKLFMSKLBVKDSAMV
    row['str6'] = ''
    while retainvars['p_rtc'] != '1':
        callmodule('SAMCIDI', retainvars['pgnb'], retainvars['p_mod'], retainvars['p_gen'], retainvars['p_len'], retainvars['p_key'], retainvars['p_rtc'], row['str1'], row['str2'], row['str3'], row['iostr5'], row['str6'])
        if (retainvars['p_rtc'] != '1'):
            row['stiid'] = str1[0: 7]
            row['senrdt'] = str1[7: 25]
            row['lnkid'] = str1[160: 166]
            row['output_table'] = 'mcid'
            res.append(row.copy())
    return res
df_in_tmp = getdf('')
mcid_rows = mcid_func(df_in_tmp)
mcid = pd.DataFrame(mcid_rows)
mcid = cxt.getOutputDF(mcid_base, 'mcid')
mcid = keepColumns(mcid, ['stiid','senrdt','lnkid','str1','str2','str3','str4','str6'])
END_BLOCK('Passed DataStep', '1:7733365795752897369')
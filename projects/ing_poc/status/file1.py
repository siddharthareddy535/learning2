import pandas as pd
from datetime import datetime
from dateutil.relativedelta import relativedelta
from utils import *

def _null_func(df, file_path):
    res = []

    with open(file_path, 'w') as f:
        for index, row in df.iterrows():
            f.write(
                row['def_id']
                + 'CUSTODY INSTRUCTIONS'
                + row['revaccid']
                + row['egbsetid']
                + row['sllid']
                + row['rsatypcd']
                + row['srvlvid']
                + row['trsid']
                + row['isisecid']
                + row['cmosecid']
                + row['sdate']
                + row['begdt']
                + row['cevtypid']
                + row['cevct'] + ' ib4.'
                + 'CUSTODY INSTRUCTION TYPE'
                + row['oper']
                + "\n"
            )
            res.append(row)

    return res


# Assuming 'result' is your DataFrame
file_path='tpdet'
tpdet = _null__func(result,file_path)
tpdet_df = pd.DataFrame(tpdet)

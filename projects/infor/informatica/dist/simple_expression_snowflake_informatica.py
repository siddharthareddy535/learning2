
selectCols = [
    (tbl('iods_den_imsmidas6'), col('Month_ID')),
    (tbl('iods_den_imsmidas6'), col('PackName_ID')),
    (tbl('iods_den_imsmidas6'), col('tc_strength_AMT')),
    (tbl('iods_den_imsmidas6'), col('su')),
    (tbl('iods_den_imsmidas6'), col('saleskg_amt')),
]


expression = ["""  CASE WHEN SALESKG_AMT IS NULL 
    THEN SU * tc_strength_AMT
    ELSE SALESKG_AMT * 1000000 END AS SALESINMG_NBR
  """]

informatica_insertinto(
    source = (tbl("iods.iods_den_imsmidas6"),alias("iods_den_imsmidas6")),
    target=tbl("work.ETP1"),
    columns=selectCols,
    expression = expression,
    distinct = False
)
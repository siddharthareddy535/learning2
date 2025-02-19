#sasFilePath: automation_sample/simple_expression.sas
#conversionTime: 01/02/2025 10:41:16
#linesInFile: 28 #linesOfCode: 18 #linesOfPython: 14
#complexity: 1 #processedBlocks: 2 #passedBlocks: 2
#failedBlocks: 0 #totalErrors: 0


selectCols = [
  (tbl("iods_den_imsmidas6"), col("Month_ID")),
(tbl("iods_den_imsmidas6"), col("PackName_ID")),
(tbl("iods_den_imsmidas6"), col("SALESKG_AMT"))
]


expression = [
  """(
                    CASE
                        WHEN SALESKG_AMT IS NULL THEN SU*tc_strength_AMT
                        ELSE SALESKG_AMT*1000000
                    END
                ) AS salesinmg_nbr"""
]



informatica_insertinto(
    source = (tbl("iods.iods_den_imsmidas6"), alias("iods_den_imsmidas6")),
    target = tbl("work.etp1"),
    columns = selectCols,
expression = expression,
truncate = False,
distinct = False,

)

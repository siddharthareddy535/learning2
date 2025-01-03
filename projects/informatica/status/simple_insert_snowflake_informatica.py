#sasFilePath: automation_sample/simple_insert.sas
#conversionTime: 01/02/2025 09:46:48
#linesInFile: 44 #linesOfCode: 28 #linesOfPython: 25
#complexity: 1 #processedBlocks: 3 #passedBlocks: 3
#failedBlocks: 0 #totalErrors: 0


selectCols = [
  (tbl("EDW_FCT_IMSSUBNATSALES"), col("UCBBRAND_SK")),
(tbl("EDW_FCT_IMSSUBNATSALES"), col("MONTH_SK")),
(tbl("EDW_FCT_IMSSUBNATSALES"), col("INDICATIONRXSPLIT_PC")),
(tbl("EDW_FCT_IMSSUBNATSALES"), col("SOURCEMD5_KEY")),
(tbl("EDW_FCT_IMSSUBNATSALES"), col("REJECTED_FL")),
(tbl("EDW_FCT_IMSSUBNATSALES"), col("CREATION_DTM")),
(tbl("EDW_FCT_IMSSUBNATSALES"), col("STANDARDSTRENGTH_CHAR"))
]



informatica_insertinto(
    source = (tbl("dwh.edw_fct_imssubnatsales"), alias("EDW_FCT_IMSSUBNATSALES")),
    target = tbl("rep.edw_fct_imssubnatsales"),
    columns = selectCols,
truncate = False,
distinct = False,

)

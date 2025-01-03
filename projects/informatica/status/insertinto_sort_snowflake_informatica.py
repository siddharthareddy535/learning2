#sasFilePath: automation_sample/insertinto_sort.sas
#conversionTime: 01/03/2025 08:16:45
#linesInFile: 27 #linesOfCode: 17 #linesOfPython: 14
#complexity: 1 #processedBlocks: 1 #passedBlocks: 1
#failedBlocks: 0 #totalErrors: 0


selectCols = [
  (tbl("REP_EDW_FCT_IMSNATIONALSALES_01"), col("PRODUCT_SK")),
(tbl("REP_EDW_FCT_IMSNATIONALSALES_01"), col("UCBBRAND_SK"))
]



informatica_insertinto(
    source = (tbl("saswork.rep_edw_fct_imsnationalsales_01"), alias("REP_EDW_FCT_IMSNATIONALSALES_01")),
    target = tbl("rep.edw_fct_imsnationalsales"),
    columns = selectCols,
truncate = False,
distinct = False,

)

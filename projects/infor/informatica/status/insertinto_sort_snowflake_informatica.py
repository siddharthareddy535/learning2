#sasFilePath: automation_sample/sort.sas
#conversionTime: 12/27/2024 12:15:02
#linesInFile: 57 #linesOfCode: 47 #linesOfPython: 44
#complexity: 1 #processedBlocks: 1 #passedBlocks: 1
#failedBlocks: 0 #totalErrors: 0


selectCols = [
  (tbl("REP_EDW_FCT_IMSNATIONALSALES_01"), col("PRODUCT_SK")),
(tbl("REP_EDW_FCT_IMSNATIONALSALES_01"), col("UCBBRAND_SK"))
]

sortCols = ['countrycode_id','productclass_id','countrymonthindex_nbr','channelmonthindex_nbr']

informatica_insertinto(
    source = (tbl("saswork.rep_edw_fct_imsnationalsales_01"), alias("REP_EDW_FCT_IMSNATIONALSALES_01")),
    target = tbl("rep.edw_fct_imsnationalsales"),
truncate = False,
distinct = False,
sortcols = sortCols
)

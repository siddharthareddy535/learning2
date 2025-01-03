#sasFilePath: automation_sample/no_truncate_distinct_insert.sas
#conversionTime: 01/02/2025 10:05:35
#linesInFile: 36 #linesOfCode: 20 #linesOfPython: 12
#complexity: 1 #processedBlocks: 3 #passedBlocks: 3
#failedBlocks: 0 #totalErrors: 0


selectCols = [
  (tbl("STG_DARTH_ELN_ENTITYCREATE_DATE"), col("DISTINCT")),
(tbl("STG_DARTH_ELN_ENTITYCREATE_DATE"), col("ENTITY_GUID")),
(tbl("STG_DARTH_ELN_ENTITYCREATE_DATE"), col("ENTITY_TIME_CREATED"))
]



informatica_insertinto(
    source = (tbl("stg.stg_darth_eln_entitycreate_date"), alias("STG_DARTH_ELN_ENTITYCREATE_DATE")),
    target = tbl("dwh.dwh_darth_eln_entitycreate_dt_f("),
    columns = selectCols,
truncate = False,
distinct = True,

)

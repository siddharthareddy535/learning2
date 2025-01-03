#sasFilePath: automation_sample/simple_groupby.sas
#conversionTime: 01/02/2025 09:11:23
#linesInFile: 37 #linesOfCode: 21 #linesOfPython: 14
#complexity: 1 #processedBlocks: 3 #passedBlocks: 3
#failedBlocks: 0 #totalErrors: 0


#informatica_delete_transformation(
#      table = "TBD",
#      deleteTable = True
#    )

groupbyCols = [
  "ENTITY_GUID"
]


aggCols = [
  ("MIN(ENTITY_TIME_CREATED) AS entity_time_created", "STRING"),
("COUNT(*) AS cnt", "STRING")
]


normalCols = [
  ("ENTITY_GUID", "STRING")
]



informatica_insertinto(
    source = (tbl("dwh.dwh_darth_eln_entitycreate_dt_f"), alias("DWH_DARTH_ELN_ENTITYCREATE_DT_F")),
    target = tbl("saswork.eln_min_createdt"),
    groupby = groupbyCols,
aggcols = aggCols,
normalcols = normalCols,
truncate = False,
distinct = False,

)

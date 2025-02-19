#sasFilePath: automation_sample/simple_join_insert.sas
#conversionTime: 01/02/2025 09:54:08
#linesInFile: 48 #linesOfCode: 28 #linesOfPython: 23
#complexity: 1 #processedBlocks: 3 #passedBlocks: 3
#failedBlocks: 0 #totalErrors: 0


informatica_simple_join(
      left = (tbl("DWH_DARTH_ELN_ENTITYCREATE_DATE"), alias("DWH_DARTH_ELN_ENTITYCREATE_DATE")),
      right = (tbl("ELN_MIN_CREATEDT"), alias("ELN_MIN_CREATEDT")),
      target = tbl("dwh.dwh_darth_eln_entitycreate_date_CART1"),
      truncate = True,
      onCondition ="""
        ELN_MIN_CREATEDT.ENTITY_GUID=DWH_DARTH_ELN_ENTITYCREATE_DATE.ENTITY_GUID AND
 ELN_MIN_CREATEDT.ENTITY_TIME_CREATED=DWH_DARTH_ELN_ENTITYCREATE_DATE.ENTITY_TIME_CREATED
    """,
       how = 'INNER'
    )



selectCols = [
  (tbl("ELN_MIN_CREATEDT"), col("DISTINCT")),
(tbl("ELN_MIN_CREATEDT"), col("ENTITY_GUID")),
(tbl("ELN_MIN_CREATEDT"), col("ENTITY_TIME_CREATED")),
(tbl("DWH_DARTH_ELN_ENTITYCREATE_DATE"), col("ENTITY_CREATED_BY")),
(tbl("DWH_DARTH_ELN_ENTITYCREATE_DATE"), col("ENTITY_CREATED_BY_NAME"))
]



informatica_insertinto(
    source = (tbl("saswork.eln_min_createdt"), alias("ELN_MIN_CREATEDT")),
    target = tbl("dwh.dwh_darth_eln_entitycreate_date"),
    columns = selectCols,
truncate = False,
distinct = True,

)

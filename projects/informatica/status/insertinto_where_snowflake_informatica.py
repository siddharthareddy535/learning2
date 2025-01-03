#sasFilePath: automation_sample/insertinto_where.sas
#conversionTime: 01/03/2025 02:49:23
#linesInFile: 80 #linesOfCode: 63 #linesOfPython: 74
#complexity: 1 #processedBlocks: 3 #passedBlocks: 3
#failedBlocks: 0 #totalErrors: 0


selectCols = [
  (tbl("STG_DODV_DS_POSITIONFLATTENED"), col("CODE")),
(tbl("STG_DODV_DS_POSITIONFLATTENED"), col("POSITION_ID")),
(tbl("STG_DODV_DS_POSITIONFLATTENED"), col("STARTDATE1")),
(tbl("STG_DODV_DS_POSITIONFLATTENED"), col("ENDDATE1")),
(tbl("STG_DODV_DS_POSITIONFLATTENED"), col("EFFECTIVESTARTDATE")),
(tbl("STG_DODV_DS_POSITIONFLATTENED"), col("EFFECTIVEENDDATE")),
(tbl("STG_DODV_DS_POSITIONFLATTENED"), col("EFFECTIVESTATUS")),
(tbl("STG_DODV_DS_POSITIONFLATTENED"), col("CUST_JOBLEVEL")),
(tbl("STG_DODV_DS_POSITIONFLATTENED"), col("CUST_JOBFAMILY")),
(tbl("STG_DODV_DS_POSITIONFLATTENED"), col("CUST_COUNTRY")),
(tbl("STG_DODV_DS_POSITIONFLATTENED"), col("COMPANY")),
(tbl("STG_DODV_DS_POSITIONFLATTENED"), col("CUST_PSAREA")),
(tbl("STG_DODV_DS_POSITIONFLATTENED"), col("CUST_JOBROLE")),
(tbl("STG_DODV_DS_POSITIONFLATTENED"), col("LOCATION")),
(tbl("STG_DODV_DS_POSITIONFLATTENED"), col("TYPE")),
(tbl("STG_DODV_DS_POSITIONFLATTENED"), col("PAYGRADE")),
(tbl("STG_DODV_DS_POSITIONFLATTENED"), col("CUST_PSLEVEL")),
(tbl("STG_DODV_DS_POSITIONFLATTENED"), col("DEPARTMENT")),
(tbl("STG_DODV_DS_POSITIONFLATTENED"), col("CUST_PSGROUP")),
(tbl("STG_DODV_DS_POSITIONFLATTENED"), col("CREATION_DTM")),
(tbl("STG_DODV_DS_POSITIONFLATTENED"), col("COSTCENTER"))
]


expression = [
  "{p_date} AS p_date"
]



informatica_insertinto(
    source = (tbl("STG.STG_DODV_DS_POSITIONFLATTENED"), alias("STG_DODV_DS_POSITIONFLATTENED")),
    target = tbl("saswork.fct_vacantpos_005"),
    columns = selectCols,
expression = expression,
truncate = False,
distinct = False,

)

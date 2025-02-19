selectCols = [
   (tbl("ELN_MIN_CREATEDT"), col("ENTITY_GUID")),
   (tbl("ELN_MIN_CREATEDT"), col("ENTITY_TIME_CREATED")),
   (tbl("DWH_DARTH_ELN_ENTITYCREATE_DATE"), col("ENTITY_CREATED_BY")),
   (tbl("DWH_DARTH_ELN_ENTITYCREATE_DATE"), col("ENTITY_CREATED_BY_NAME"))
]

informatica_simple_join(
    columns = selectCols,
    left = (tbl("saswork.eln_min_createdt"), alias("ELN_MIN_CREATEDT")),
    right = (tbl("dwh.dwh_darth_eln_entitycreate_dt_f"), alias("DWH_DARTH_ELN_ENTITYCREATE_DATE")),
    target = tbl("dwh.dwh_darth_eln_entitycreate_date"),
    truncate = True,
    distinct = True,
    onCondition = """
        ELN_MIN_CREATEDT.ENTITY_GUID = DWH_DARTH_ELN_ENTITYCREATE_DATE.ENTITY_GUID
        AND ELN_MIN_CREATEDT.ENTITY_TIME_CREATED = DWH_DARTH_ELN_ENTITYCREATE_DATE.ENTITY_TIME_CREATED
    """,
    how = "inner"
)


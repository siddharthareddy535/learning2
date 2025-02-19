
truncate = False

selectCols = [
   (tbl("STG_DARTH_ELN_ENTITYCREATE_DATE"), col("ENTITY_GUID")),
   (tbl("STG_DARTH_ELN_ENTITYCREATE_DATE"), col("ENTITY_TIME_CREATED"))
]

informatica_insertinto(
    source = (tbl("STG.STG_DARTH_ELN_ENTITYCREATE_DATE"), alias("STG_DARTH_ELN_ENTITYCREATE_DATE")),
    target=tbl("DWH.DWH_DARTH_ELN_ENTITYCREATE_DT_F"),
    columns=selectCols,
    truncate = truncate,
    distinct = True
)
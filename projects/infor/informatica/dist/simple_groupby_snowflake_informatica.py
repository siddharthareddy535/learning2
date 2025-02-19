truncate = False

groupbyCols = ["ENTITY_GUID"]

aggCols = [
    ("min(ENTITY_TIME_CREATED) as ENTITY_TIME_CREATED", "datetime"), 
    ("count(*) as cnt", "integer")
]

normalCols = [("ENTITY_GUID", "string")]

informatica_simple_groupby(
  source=tbl("DWH.DWH_DARTH_ELN_ENTITYCREATE_DT_F"),
  target=tbl("SASWORK.ELN_MIN_CREATEDT"),
  groupby=groupbyCols,
  aggcols=aggCols,
  normalcols=normalCols,
  truncate=truncate
)

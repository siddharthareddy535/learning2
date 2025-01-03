


informatica_delete_transformation(
table = tbl("DWH.DWH_DARTH_ELN_CURRENT_ENTITIES"),
onCondition = "ENTITY_STATUS IS NULL AND ENTITY_TYPE = 'EXPERIMENT'",
truncate = True,
deleteTable =  True
)
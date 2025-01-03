

selectCols = [
(tbl("EDW_FCT_IMSSUBNATSALES"), col("UCBBRAND_SK")),
(tbl("EDW_FCT_IMSSUBNATSALES"), col("MONTH_SK")),
(tbl("EDW_FCT_IMSSUBNATSALES"), col("INDICATIONRXSPLIT_PC")),
(tbl("EDW_FCT_IMSSUBNATSALES"), col("SOURCEMD5_KEY")),
(tbl("EDW_FCT_IMSSUBNATSALES"), col("REJECTED_FL")),
(tbl("EDW_FCT_IMSSUBNATSALES"), col("CREATION_DTM")),
(tbl("EDW_FCT_IMSSUBNATSALES"), col("STANDARDSTRENGTH_CHAR"))
]

informatica_insertinto(
    source = (tbl("DWH.EDW_FCT_IMSSUBNATSALES"), alias("EDW_FCT_IMSSUBNATSALES")),
    target = tbl("rep.edw_fct_imssubnatsales"),
    columns = selectCols,
    truncate = True,
    distinct = False
)
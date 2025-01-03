#sasFilePath: test.sas
#conversionTime: 12/23/2024 12:06:35
#linesInFile: 67 #linesOfCode: 42 #linesOfPython: 31
#complexity: 1 #processedBlocks: 3 #passedBlocks: 3
#failedBlocks: 0 #totalErrors: 0


expression = [
"""COALESCE(TRIM(ODS_TRANS_INMARKETSALES.PACKNAME_ID), 'A') AS PACKNAME_ID_JOIN1""",
"""COALESCE(TRIM(ODS_TRANS_INMARKETSALES.PRODUCTNAME_ID), 'A') AS PRODUCTNAME_ID_JOIN1"""
]

informatica_insertinto(
    source = (tbl("SASWORK.ODS_TRANS_INMARKETSALES"), alias("ODS_TRANS_INMARKETSALES")),
    truncate = True,
    expression = expression,
    expressionname = tbl("ODS_TRANS_INMARKETSALES_JOIN1")

)



expression = [
"""COALESCE(TRIM(EDW_CML_DIM_PRODUCT.PRODUCTPACK_NM), 'A') AS PRODUCTPACK_NM_JOIN2""",
"""COALESCE(TRIM(EDW_CML_DIM_PRODUCT.PRODUCT_NM), 'A') AS PRODUCT_NM_JOIN2"""
]

informatica_insertinto(
    source = (tbl("DWH.EDW_CML_DIM_PRODUCT"), alias("EDW_CML_DIM_PRODUCT")),
    truncate = True,
    expression = expression,
    expressionname = tbl("EDW_CML_DIM_PRODUCT_JOIN2")

)



informatica_simple_join(
      left = (tbl("ODS_TRANS_INMARKETSALES_JOIN1"), alias("ODS_TRANS_INMARKETSALES")),
      right = (tbl("EDW_CML_DIM_PRODUCT_JOIN2"), alias("EDW_CML_DIM_PRODUCT")),
      target = tbl("saswork_idwh_fct_inmarketsalesactuals2_CART1"),
      truncate = True,
      onCondition ="""
        ODS_TRANS_INMARKETSALES.PACKNAME_ID_JOIN1=EDW_CML_DIM_PRODUCT.PRODUCTPACK_NM_JOIN2 AND
 ODS_TRANS_INMARKETSALES.PRODUCTNAME_ID_JOIN1=EDW_CML_DIM_PRODUCT.PRODUCT_NM_JOIN2
    """,
       how = 'LEFT'
    )



informatica_simple_join(
      left = (tbl("saswork_idwh_fct_inmarketsalesactuals2_CART1"), alias("saswork_idwh_fct_inmarketsalesactuals2_CART1")),
      right = (tbl("DWH.EDW_CML_DIM_PANEL"), alias("EDW_CML_DIM_PANEL")),
      target = tbl("saswork_idwh_fct_inmarketsalesactuals2_CART2"),
      truncate = True,
      onCondition ="""
        ODS_TRANS_INMARKETSALES.PANELCODE_ID=EDW_CML_DIM_PANEL.PANEL_CD
    """,
       how = 'LEFT'
    )



informatica_simple_join(
      left = (tbl("saswork_idwh_fct_inmarketsalesactuals2_CART2"), alias("saswork_idwh_fct_inmarketsalesactuals2_CART2")),
      right = (tbl("DWH.EDW_CML_DIM_MARKET"), alias("EDW_CML_DIM_MARKET")),
      target = tbl("saswork_idwh_fct_inmarketsalesactuals2_CART3"),
      truncate = True,
      onCondition ="""
        ODS_TRANS_INMARKETSALES.MARKETCODE_ID=EDW_CML_DIM_MARKET.MARKETCODE_ID AND
 ODS_TRANS_INMARKETSALES.MOLECULENAME_ID=EDW_CML_DIM_MARKET.MOLECULENAME_ID
    """,
       how = 'LEFT'
    )



informatica_simple_join(
      left = (tbl("saswork_idwh_fct_inmarketsalesactuals2_CART3"), alias("saswork_idwh_fct_inmarketsalesactuals2_CART3")),
      right = (tbl("DWH.EDW_CML_DIM_SPECIALTY"), alias("EDW_CML_DIM_SPECIALTY")),
      target = tbl("saswork.idwh_fct_inmarketsalesactuals2_CART4"),
      truncate = True,
      onCondition ="""
        ODS_TRANS_INMARKETSALES.SPECIALTY_NM=EDW_CML_DIM_SPECIALTY.SPECIALTY_NM
    """,
       how = 'LEFT'
    )



expression = [
  """CASE
                WHEN saswork_idwh_fct_inmarketsalesactuals2_CART4.MARKETCODE_ID IS NULL THEN - 1
                WHEN saswork_idwh_fct_inmarketsalesactuals2_CART4.MARKETCODE_ID IS NOT NULL
                AND saswork_idwh_fct_inmarketsalesactuals2_CART4.MARKET_SK IS NULL THEN - 2
                ELSE saswork_idwh_fct_inmarketsalesactuals2_CART4.MARKET_SK
            END AS market_sk""",
"""COALESCE(saswork_idwh_fct_inmarketsalesactuals2_CART4.SPECIALTY_SK, -2) AS specialty_sk""",
"""COALESCE(saswork_idwh_fct_inmarketsalesactuals2_CART4.PRODUCT_SK, -2) AS product_sk""",
"""COALESCE(saswork_idwh_fct_inmarketsalesactuals2_CART4.PANEL_SK, -2) AS panel_sk"""
]


selectCols = [
(tbl("saswork_idwh_fct_inmarketsalesactuals2_CART4"), col("MARKET_SK")),
(tbl("saswork_idwh_fct_inmarketsalesactuals2_CART4"), col("SPECIALTY_SK")),
(tbl("saswork_idwh_fct_inmarketsalesactuals2_CART4"), col("PRODUCT_SK")),
(tbl("saswork_idwh_fct_inmarketsalesactuals2_CART4"), col("PANEL_SK"))
]

informatica_insertinto(
    source = (tbl("saswork_idwh_fct_inmarketsalesactuals2_CART4"), alias("saswork_idwh_fct_inmarketsalesactuals2_CART4")),
    target = tbl("saswork.idwh_fct_inmarketsalesactuals2"),
    expression = expression,
    truncate = True,
    distinct = False,
    columns = selectCols
)

expression = [
"""COALESCE(TRIM(ODS_TRANS_INMARKETSALES.PACKNAME_ID), 'A') AS PACKNAME_ID_JOIN1""",
"""COALESCE(TRIM(ODS_TRANS_INMARKETSALES.PRODUCTNAME_ID), 'A') AS PRODUCTNAME_ID_JOIN1""",
"""COALESCE(TRIM(ODS_TRANS_INMARKETSALES.STRENGTHRATE_ID), 'A') AS STRENGTHRATE_ID_JOIN1""",
"""COALESCE(TRIM(ODS_TRANS_INMARKETSALES.MOLECULENAME_ID), 'A') AS MOLECULENAME_ID_JOIN1""",
"""COALESCE(TRIM(ODS_TRANS_INMARKETSALES.NFC123CODE_ID), 'A') AS NFC123CODE_ID_JOIN1""",
"""COALESCE(TRIM(ODS_TRANS_INMARKETSALES.MANUFACTURERNAME_ID), 'A') AS MANUFACTURERNAME_ID_JOIN1""",
"""COALESCE(TRIM(ODS_TRANS_INMARKETSALES.INTERNATIONALPRODUCTNAME_ID), 'A') AS INTERNATIONALPRODUCTNAME_ID_JOIN1""",
"""COALESCE(TRIM(ODS_TRANS_INMARKETSALES.CORPORATIONNAME_ID), 'A') AS CORPORATIONNAME_ID_JOIN1""",
"""COALESCE(TRIM(ODS_TRANS_INMARKETSALES.PRODUCTATC3_CD), 'A') AS PRODUCTATC3_CD_JOIN1""",
"""COALESCE(TRIM(ODS_TRANS_INMARKETSALES.PRODUCTATC4_CD), 'A') AS PRODUCTATC4_CD_JOIN1"""
]

# Defaulting truncate = True for all intermediary tables
# For join names using main table name with _JOIN1, _JOIN2 etc

informatica_insertinto(
    source = (tbl("SASWORK.ODS_TRANS_INMARKETSALES"), alias("ODS_TRANS_INMARKETSALES")),
    truncate = True,
    expression = expression,
    expressionname = tbl("ODS_TRANS_INMARKETSALES_JOIN1")
)

expression = [
"""COALESCE(TRIM(EDW_CML_DIM_PRODUCT.PRODUCTPACK_NM), 'A') AS PRODUCTPACK_NM_JOIN2""",
"""COALESCE(TRIM(EDW_CML_DIM_PRODUCT.PRODUCT_NM), 'A') AS PRODUCT_NM_JOIN2""",
"""COALESCE(TRIM(EDW_CML_DIM_PRODUCT.PRODUCTSTRENGTH_RT), 'A') AS PRODUCTSTRENGTH_RT_JOIN2""",
"""COALESCE(TRIM(EDW_CML_DIM_PRODUCT.PRODUCTMOLECULE_NM), 'A') AS PRODUCTMOLECULE_NM_JOIN2""",
"""COALESCE(TRIM(EDW_CML_DIM_PRODUCT.NFC123_CD), 'A') AS NFC123_CD_JOIN2""",
"""COALESCE(TRIM(EDW_CML_DIM_PRODUCT.PRODUCTMANUFACTURER_NM), 'A') AS PRODUCTMANUFACTURER_NM_JOIN2""",
"""COALESCE(TRIM(EDW_CML_DIM_PRODUCT.INTERNATIONALPRODUCT_NM), 'A') AS INTERNATIONALPRODUCT_NM_JOIN2""",
"""COALESCE(TRIM(EDW_CML_DIM_PRODUCT.PRODUCTCORPORATION_NM), 'A') AS PRODUCTCORPORATION_NM_JOIN2""",
"""COALESCE(TRIM(EDW_CML_DIM_PRODUCT.PRODUCTATC3_CD), 'A') AS PRODUCTATC3_CD_JOIN2""",
"""COALESCE(TRIM(EDW_CML_DIM_PRODUCT.PRODUCTATC4_CD), 'A') AS PRODUCTATC4_CD_JOIN2"""
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
        ODS_TRANS_INMARKETSALES.PACKNAME_ID_JOIN1 = EDW_CML_DIM_PRODUCT.PRODUCTPACK_NM_JOIN2 AND
ODS_TRANS_INMARKETSALES.PRODUCTNAME_ID_JOIN1 = EDW_CML_DIM_PRODUCT.PRODUCT_NM_JOIN2 AND
ODS_TRANS_INMARKETSALES.STRENGTHRATE_ID_JOIN1 = EDW_CML_DIM_PRODUCT.PRODUCTSTRENGTH_RT_JOIN2 AND
ODS_TRANS_INMARKETSALES.MOLECULENAME_ID_JOIN1 = EDW_CML_DIM_PRODUCT.PRODUCTMOLECULE_NM_JOIN2 AND
ODS_TRANS_INMARKETSALES.NFC123CODE_ID_JOIN1 = EDW_CML_DIM_PRODUCT.NFC123_CD_JOIN2 AND
ODS_TRANS_INMARKETSALES.MANUFACTURERNAME_ID_JOIN1 = EDW_CML_DIM_PRODUCT.PRODUCTMANUFACTURER_NM_JOIN2 AND
ODS_TRANS_INMARKETSALES.INTERNATIONALPRODUCTNAME_ID_JOIN1 = EDW_CML_DIM_PRODUCT.INTERNATIONALPRODUCT_NM_JOIN2 AND
ODS_TRANS_INMARKETSALES.CORPORATIONNAME_ID_JOIN1 = EDW_CML_DIM_PRODUCT.PRODUCTCORPORATION_NM_JOIN2 AND
ODS_TRANS_INMARKETSALES.PRODUCTATC3_CD_JOIN1 = EDW_CML_DIM_PRODUCT.PRODUCTATC3_CD_JOIN2 AND
ODS_TRANS_INMARKETSALES.PRODUCTATC4_CD_JOIN1 = EDW_CML_DIM_PRODUCT.PRODUCTATC4_CD_JOIN2
    """,
    how = 'LEFT'
)

informatica_simple_join(
    left = tbl("saswork_idwh_fct_inmarketsalesactuals2_CART1"),
    right = (tbl("DWH.EDW_CML_DIM_COUNTRY"), alias("EDW_CML_DIM_COUNTRY")),
    target = tbl("IDWH_FCT_INMARKETSALESACTUALS2_CART2"),
    truncate = True,
    onCondition = """
        ODS_TRANS_INMARKETSALES.FINALDESTINATIONCOUNTRYCODE_ID = EDW_CML_DIM_COUNTRY.COUNTRYCODE_ID
    """,
    how = 'LEFT'
)

informatica_simple_join(
    left = tbl("IDWH_FCT_INMARKETSALESACTUALS2_CART2"),
    right = (tbl("DWH.EDW_CML_DIM_MATERIAL"), alias("EDW_CML_DIM_MATERIAL")),
    target = tbl("IDWH_FCT_INMARKETSALESACTUALS2_CART3"),
    truncate = True,
    onCondition = """
        ODS_TRANS_INMARKETSALES.MATERIALCODE_ID = EDW_CML_DIM_MATERIAL.MATERIALCODE_ID
    """,
    how = "left"
)

informatica_simple_join(
    left = tbl("IDWH_FCT_INMARKETSALESACTUALS2_CART3"),
    right = (tbl("DWH.EDW_DIM_PRODUCTFAMILY"), alias("EDW_DIM_PRODUCTFAMILY")),
    target = tbl("IDWH_FCT_INMARKETSALESACTUALS2_CART4"),
    truncate = True,
    onCondition = """
        ODS_TRANS_INMARKETSALES.PRODUCTFAMILYCODE_ID = EDW_DIM_PRODUCTFAMILY.PRODUCTFAMILYCODE_ID
    """,
    how = "left"
)

informatica_simple_join(
    left = tbl("IDWH_FCT_INMARKETSALESACTUALS2_CART4"),
    right = (tbl("DWH.EDW_CML_DIM_CURRENCY"), alias("EDW_CML_DIM_CURRENCY")),
    target = tbl("IDWH_FCT_INMARKETSALESACTUALS2_CART5"),
    truncate = True,
    onCondition = """
        ODS_TRANS_INMARKETSALES.LOCALCURRENCYCODE_ID = EDW_CML_DIM_CURRENCY.CURRENCYCODE_ID
    """,
    how = "left"
)

informatica_simple_join(
    left = tbl("IDWH_FCT_INMARKETSALESACTUALS2_CART5"),
    right = (tbl("DWH.EDW_CML_DIM_SOURCE"), alias("EDW_CML_DIM_SOURCE")),
    target = tbl("IDWH_FCT_INMARKETSALESACTUALS2_CART6"),
    truncate = True,
    onCondition = """
        ODS_TRANS_INMARKETSALES.SOURCECODE_ID = EDW_CML_DIM_SOURCE.SOURCECODE_ID
    """,
    how = "left"
)

informatica_simple_join(
    left = tbl("IDWH_FCT_INMARKETSALESACTUALS2_CART6"),
    right = (tbl("DWH.EDW_CML_DIM_PANEL"), alias("EDW_CML_DIM_PANEL")),
    target = tbl("IDWH_FCT_INMARKETSALESACTUALS2_CART7"),
    truncate = True,
    onCondition = """
        ODS_TRANS_INMARKETSALES.PANELCODE_ID = EDW_CML_DIM_PANEL.PANEL_CD
    """,
    how = "left"
)

informatica_simple_join(
    left = tbl("IDWH_FCT_INMARKETSALESACTUALS2_CART7"),
    right = (tbl("DWH.EDW_CML_DIM_MARKET"), alias("EDW_CML_DIM_MARKET")),
    target = tbl("IDWH_FCT_INMARKETSALESACTUALS2_CART8"),
    truncate = True,
    onCondition = """
        ODS_TRANS_INMARKETSALES.MARKETCODE_ID = EDW_CML_DIM_MARKET.MARKETCODE_ID
        and ODS_TRANS_INMARKETSALES.MOLECULENAME_ID = EDW_CML_DIM_MARKET.MOLECULENAME_ID
    """,
    how = "left"
)

informatica_simple_join(
    left = tbl("IDWH_FCT_INMARKETSALESACTUALS2_CART8"),
    right = (tbl("DWH.EDW_CML_DIM_SPECIALTY"), alias("EDW_CML_DIM_SPECIALTY")),
    target = tbl("IDWH_FCT_INMARKETSALESACTUALS2_joined"),
    truncate = True,
    onCondition = """
        ODS_TRANS_INMARKETSALES.SPECIALTY_NM = EDW_CML_DIM_SPECIALTY.SPECIALTY_NM
    """,
    how = "left"
)

expression = [
    """CASE 
    WHEN  ODS_TRANS_INMARKETSALES.MARKETCODE_ID  IS NULL THEN -1    
    WHEN  ODS_TRANS_INMARKETSALES.MARKETCODE_ID   IS NOT NULL 
    AND  EDW_CML_DIM_MARKET.MARKET_SK   IS NULL THEN -2    
    ELSE EDW_CML_DIM_MARKET.MARKET_SK 
    END as MARKET_SK""",
"""coalesce(EDW_CML_DIM_SPECIALTY.SPECIALTY_SK  ,-2) as SPECIALTY_SK""",
"""ODS_TRANS_INMARKETSALES.MONTH_ID as MONTH_SK""",
"""coalesce(EDW_CML_DIM_PRODUCT.PRODUCT_SK ,-2) as PRODUCT_SK""",
"""coalesce(EDW_CML_DIM_PANEL.PANEL_SK,-2) as PANEL_SK""",
"""ODS_TRANS_INMARKETSALES.LAUNCH_DT as LAUNCHMONTH_SK""",
"""coalesce(EDW_CML_DIM_CURRENCY.CURRENCY_SK ,-2) as LOCALCURRENCY_SK""",
"""coalesce(EDW_CML_DIM_SOURCE.SOURCECODE_SK ,-2) as SOURCE_SK""",
"""coalesce(EDW_CML_DIM_COUNTRY.COUNTRY_SK ,-2) as FINALDESTINATIONCOUNTRY_SK""",
"""coalesce(EDW_DIM_PRODUCTFAMILY.PRODUCTFAMILY_SK ,-3) as PRODUCTFAMILY_SK""",
"""coalesce(EDW_CML_DIM_MATERIAL.MATERIAL_SK ,-3) as MATERIAL_SK"""
]

informatica_insertinto(
    source = tbl("IDWH_FCT_INMARKETSALESACTUALS2_joined"),
    target = tbl("SASWORK.IDWH_FCT_INMARKETSALESACTUALS2"),
    truncate = True,
    expression = expression
)
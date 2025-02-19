update_query = '''
UPDATE saswork.idwh_fct_inmarketsalesactuals2idwh_fct_inmarketsalesactuals2
        SET
            idwh_fct_inmarketsalesactuals2.market_sk=EDW_CML_DIM_MARKET.MARKET_SK
        FROM
            dwh.edw_cml_dim_market AS EDW_CML_DIM_MARKET
        WHERE
            EDW_CML_DIM_MARKET.MOLECULENAME_ID='/'
            AND IDWH_FCT_INMARKETSALESACTUALS2.MARKETCODE_ID=EDW_CML_DIM_MARKET.MARKETCODE_ID
            AND IDWH_FCT_INMARKETSALESACTUALS2.MARKET_SK=-2
'''

informatica_simple_update(
    source = tbl("dwh.edw_cml_dim_market"),
    target = tbl("saswork.idwh_fct_inmarketsalesactuals2idwh_fct_inmarketsalesactuals2"),
    update_query = update_query
)

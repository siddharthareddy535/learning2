#sasFilePath: automation_sample/union_2inputs.sas
#conversionTime: 01/02/2025 05:58:13
#linesInFile: 230 #linesOfCode: 221 #linesOfPython: 217
#complexity: 1 #processedBlocks: 1 #passedBlocks: 1
#failedBlocks: 0 #totalErrors: 0


selectCols = [
  (tbl("IDWH_FCT_INMARKETSALESACTUALS1"), col("MARKET_SK")),
(tbl("IDWH_FCT_INMARKETSALESACTUALS1"), col("SPECIALTY_SK")),
(tbl("IDWH_FCT_INMARKETSALESACTUALS1"), col("MARKETCODEOPTPROD_SK")),
(tbl("IDWH_FCT_INMARKETSALESACTUALS1"), col("MONTH_SK")),
(tbl("IDWH_FCT_INMARKETSALESACTUALS1"), col("PRODUCT_SK")),
(tbl("IDWH_FCT_INMARKETSALESACTUALS1"), col("PANEL_SK")),
(tbl("IDWH_FCT_INMARKETSALESACTUALS1"), col("LAUNCHMONTH_SK")),
(tbl("IDWH_FCT_INMARKETSALESACTUALS1"), col("LOCALCURRENCY_SK")),
(tbl("IDWH_FCT_INMARKETSALESACTUALS1"), col("SOURCE_SK")),
(tbl("IDWH_FCT_INMARKETSALESACTUALS1"), col("FINALDESTINATIONCOUNTRY_SK")),
(tbl("IDWH_FCT_INMARKETSALESACTUALS1"), col("PRODUCTFAMILY_SK")),
(tbl("IDWH_FCT_INMARKETSALESACTUALS1"), col("MATERIAL_SK")),
(tbl("IDWH_FCT_INMARKETSALESACTUALS1"), col("PACKNAME_ID")),
(tbl("IDWH_FCT_INMARKETSALESACTUALS1"), col("PRODUCTNAME_ID")),
(tbl("IDWH_FCT_INMARKETSALESACTUALS1"), col("STRENGTHRATE_ID")),
(tbl("IDWH_FCT_INMARKETSALESACTUALS1"), col("MARKETCODE_ID")),
(tbl("IDWH_FCT_INMARKETSALESACTUALS1"), col("SPECIALTY_NM")),
(tbl("IDWH_FCT_INMARKETSALESACTUALS1"), col("MARKETCODEOPTPROD_ID")),
(tbl("IDWH_FCT_INMARKETSALESACTUALS1"), col("SOURCECODE_ID")),
(tbl("IDWH_FCT_INMARKETSALESACTUALS1"), col("FINALDESTINATIONCOUNTRYCODE_ID")),
(tbl("IDWH_FCT_INMARKETSALESACTUALS1"), col("MOLECULENAME_ID")),
(tbl("IDWH_FCT_INMARKETSALESACTUALS1"), col("NFC123CODE_ID")),
(tbl("IDWH_FCT_INMARKETSALESACTUALS1"), col("MANUFACTURERNAME_ID")),
(tbl("IDWH_FCT_INMARKETSALESACTUALS1"), col("INTERNATIONALPRODUCTNAME_ID")),
(tbl("IDWH_FCT_INMARKETSALESACTUALS1"), col("CORPORATIONNAME_ID")),
(tbl("IDWH_FCT_INMARKETSALESACTUALS1"), col("PRODUCTATC3_CD")),
(tbl("IDWH_FCT_INMARKETSALESACTUALS1"), col("PRODUCTATC4_CD")),
(tbl("IDWH_FCT_INMARKETSALESACTUALS1"), col("PANELCODE_ID")),
(tbl("IDWH_FCT_INMARKETSALESACTUALS1"), col("MATERIALCODE_ID")),
(tbl("IDWH_FCT_INMARKETSALESACTUALS1"), col("PRODUCTFAMILYCODE_ID")),
(tbl("IDWH_FCT_INMARKETSALESACTUALS1"), col("LOCALCURRENCYCODE_ID")),
(tbl("IDWH_FCT_INMARKETSALESACTUALS1"), col("CONVERSIONLCTOEUR_RT")),
(tbl("IDWH_FCT_INMARKETSALESACTUALS1"), col("CONVERSIONLCTOUSD_RT")),
(tbl("IDWH_FCT_INMARKETSALESACTUALS1"), col("RAWSALESINLC_AMT")),
(tbl("IDWH_FCT_INMARKETSALESACTUALS1"), col("RAWSALESINEURO_AMT")),
(tbl("IDWH_FCT_INMARKETSALESACTUALS1"), col("RAWSALESINDOLLAR_AMT")),
(tbl("IDWH_FCT_INMARKETSALESACTUALS1"), col("RAWDOLLARREALMTHRT_AMT")),
(tbl("IDWH_FCT_INMARKETSALESACTUALS1"), col("RAWEUROREALMTHRT_AMT")),
(tbl("IDWH_FCT_INMARKETSALESACTUALS1"), col("RAWSALESINUNITS_NBR")),
(tbl("IDWH_FCT_INMARKETSALESACTUALS1"), col("RAWSALESINSTDUNITS_NBR")),
(tbl("IDWH_FCT_INMARKETSALESACTUALS1"), col("RAWSALESINCNTUNITS_NBR")),
(tbl("IDWH_FCT_INMARKETSALESACTUALS1"), col("RXSPLIT_RT")),
(tbl("IDWH_FCT_INMARKETSALESACTUALS1"), col("ADJSALESINCNTUNITS_NBR")),
(tbl("IDWH_FCT_INMARKETSALESACTUALS1"), col("ADJSALESINUNITS_NBR")),
(tbl("IDWH_FCT_INMARKETSALESACTUALS1"), col("ADJSALESINSTDUNITS_NBR")),
(tbl("IDWH_FCT_INMARKETSALESACTUALS1"), col("ADJSALESINLC_AMT")),
(tbl("IDWH_FCT_INMARKETSALESACTUALS1"), col("ADJSALESINEURO_AMT")),
(tbl("IDWH_FCT_INMARKETSALESACTUALS1"), col("ADJSALESINDOLLAR_AMT")),
(tbl("IDWH_FCT_INMARKETSALESACTUALS1"), col("ADJSALESINDOLLARREALMTHRT_AMT")),
(tbl("IDWH_FCT_INMARKETSALESACTUALS1"), col("ADJSALESINEUROREALMTHRT_AMT")),
(tbl("IDWH_FCT_INMARKETSALESACTUALS1"), col("AVDOS_RT")),
(tbl("IDWH_FCT_INMARKETSALESACTUALS1"), col("TREATDAYS_NBR")),
(tbl("IDWH_FCT_INMARKETSALESACTUALS1"), col("PATMODTREATDAYS_NBR")),
(tbl("IDWH_FCT_INMARKETSALESACTUALS1"), col("PATMODTREATDAYSONEMONTH_NBR")),
(tbl("IDWH_FCT_INMARKETSALESACTUALS1"), col("PATMODTREATDAYSTWOMONTHS_NBR")),
(tbl("IDWH_FCT_INMARKETSALESACTUALS1"), col("PATMODTREATDAYSTHREEMONTHS_NBR")),
(tbl("IDWH_FCT_INMARKETSALESACTUALS1"), col("PATMODTREATDAYSTOTAL_NBR")),
(tbl("IDWH_FCT_INMARKETSALESACTUALS1"), col("PATMODTOTALPATIENTSCURRMTH_NBR")),
(tbl("IDWH_FCT_INMARKETSALESACTUALS1"), col("PATMODTOTALPATIENTS_NBR")),
(tbl("IDWH_FCT_INMARKETSALESACTUALS1"), col("PATMODPATIENTS_NBR")),
(tbl("IDWH_FCT_INMARKETSALESACTUALS1"), col("PATMODFACTSALESINUNITS_NBR")),
(tbl("IDWH_FCT_INMARKETSALESACTUALS1"), col("PATMODADJUNITS_NBR")),
(tbl("IDWH_FCT_INMARKETSALESACTUALS1"), col("PATMODNEWPATIENTS_NBR")),
(tbl("IDWH_FCT_INMARKETSALESACTUALS1"), col("PATMODINDUCTIONPATIENTS_NBR")),
(tbl("IDWH_FCT_INMARKETSALESACTUALS1"), col("PATMODCONTINUINGPATIENTS_NBR")),
(tbl("IDWH_FCT_INMARKETSALESACTUALS1"), col("PATMODEXITPATIENTS_NBR")),
(tbl("IDWH_FCT_INMARKETSALESACTUALS1"), col("MONTHSINCELAUNCH_NBR")),
(tbl("IDWH_FCT_INMARKETSALESACTUALS1"), col("SALESINMG")),
(tbl("IDWH_FCT_INMARKETSALESACTUALS1"), col("PACKTYPE_NBR")),
(tbl("IDWH_FCT_INMARKETSALESACTUALS1"), col("COMPLIANCEPERSISTENCE_RT")),
(tbl("IDWH_FCT_INMARKETSALESACTUALS1"), col("RESTATEDDOSAGE_QTY")),
(tbl("IDWH_FCT_INMARKETSALESACTUALS1"), col("INDUCTIONDOSAGE_QTY")),
(tbl("IDWH_FCT_INMARKETSALESACTUALS1"), col("STARTINGDOSAGE_QTY")),
(tbl("IDWH_FCT_INMARKETSALESACTUALS1"), col("COMPLIANCE_RT")),
(tbl("IDWH_FCT_INMARKETSALESACTUALS1"), col("ESCALATION_RT")),
(tbl("IDWH_FCT_INMARKETSALESACTUALS1"), col("PERSTENCE_RT")),
(tbl("IDWH_FCT_INMARKETSALESACTUALS1"), col("RAWDISPPRESCNEW_NBR")),
(tbl("IDWH_FCT_INMARKETSALESACTUALS1"), col("RAWDISPPRESCTOT_NBR")),
(tbl("IDWH_FCT_INMARKETSALESACTUALS1"), col("RAWDISPPRESCCNTUNITSNEW_NBR")),
(tbl("IDWH_FCT_INMARKETSALESACTUALS1"), col("RAWDISPPRESCCNTUNITSTOT_NBR")),
(tbl("IDWH_FCT_INMARKETSALESACTUALS1"), col("ADJDISPPRESCNEW_NBR")),
(tbl("IDWH_FCT_INMARKETSALESACTUALS1"), col("ADJDISPPRESCTOT_NBR")),
(tbl("IDWH_FCT_INMARKETSALESACTUALS1"), col("ADJDISPPRESCCNTUNITSNEW_NBR")),
(tbl("IDWH_FCT_INMARKETSALESACTUALS1"), col("ADJDISPTOTALPRESCCNTUNITSTOT_NBR")),
(tbl("IDWH_FCT_INMARKETSALESACTUALS1"), col("EXCEPTION_FL")),
(tbl("IDWH_FCT_INMARKETSALESACTUALS1"), col("PRODUCTATC3ORIG_CD")),
(tbl("IDWH_FCT_INMARKETSALESACTUALS1"), col("PRODUCTATC4ORIG_CD")),
(tbl("IDWH_FCT_INMARKETSALESACTUALS1"), col("STRENGTHMG_NBR")),
(tbl("IDWH_FCT_INMARKETSALESACTUALS1"), col("PRODUCTBRANDGENERIC_FL")),
(tbl("IDWH_FCT_INMARKETSALESACTUALS1"), col("PRODUCTSTRENGTHORIG_CD")),
(tbl("IDWH_FCT_INMARKETSALESACTUALS1"), col("PRODUCT_CODE")),
(tbl("IDWH_FCT_INMARKETSALESACTUALS1"), col("PATIENTSHAREINPUT_NBR")),
(tbl("IDWH_FCT_INMARKETSALESACTUALS1"), col("EXITPATIENT_NBR")),
(tbl("IDWH_FCT_INMARKETSALESACTUALS1"), col("CUMUNIQUEPAT_NBR")),
(tbl("IDWH_FCT_INMARKETSALESACTUALS1"), col("SALESKG_AMT")),
(tbl("IDWH_FCT_INMARKETSALESACTUALS1"), col("ETPCOMPLIANCEFACTOR_RT")),
(tbl("IDWH_FCT_INMARKETSALESACTUALS1"), col("ETPSPLIT_RT")),
(tbl("IDWH_FCT_INMARKETSALESACTUALS1"), col("ETPVOLUMESPLIT_RT")),
(tbl("IDWH_FCT_INMARKETSALESACTUALS1"), col("ETPAVDAYDOSAGE_NBR")),
(tbl("IDWH_FCT_INMARKETSALESACTUALS1"), col("ETPTREATMENTDAYS_NBR")),
(tbl("IDWH_FCT_INMARKETSALESACTUALS1"), col("ETPTREATMENTMONTH_NBR")),
(tbl("IDWH_FCT_INMARKETSALESACTUALS1"), col("ETPSALESINMG_NBR")),
(tbl("IDWH_FCT_INMARKETSALESACTUALS1"), col("ETPCOUNT_NBR"))
]



informatica_insertinto(
    source = (tbl("saswork.idwh_fct_inmarketsalesactuals1"), alias("IDWH_FCT_INMARKETSALESACTUALS1")),
    target = tbl("saswork.wsna7bw"),
    columns = selectCols,
truncate = False,
distinct = False,

)
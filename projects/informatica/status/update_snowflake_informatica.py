#sasFilePath: automation_sample/update.sas
#conversionTime: 01/02/2025 09:32:49
#linesInFile: 23 #linesOfCode: 13 #linesOfPython: 18
#complexity: 1 #processedBlocks: 2 #passedBlocks: 2
#failedBlocks: 0 #totalErrors: 0


update_query = '''
UPDATE 
'''

informatica_simple_update(
    source = tbl("dwh.edw_cml_dim_market"),
    target = tbl("saswork.idwh_fct_inmarketsalesactuals2idwh_fct_inmarketsalesactuals2"),
    update_query = update_query
)

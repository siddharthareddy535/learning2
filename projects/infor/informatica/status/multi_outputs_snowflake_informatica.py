#sasFilePath: automation_sample/multi_outputs.sas
#conversionTime: 12/27/2024 12:01:23
#linesInFile: 25 #linesOfCode: 13 #linesOfPython: 17
#complexity: 1 #processedBlocks: 2 #passedBlocks: 2
#failedBlocks: 0 #totalErrors: 0

rxsplitavdosdate = '01JAN2011'

condition1 = f'''dtPeriod > {rxsplitavdosdate}'''
condition2 = f'''dtPeriod < {rxsplitavdosdate}'''

informatica_multioutputs(
  source_table = tbl('iods.iods_den_imsmidas1'),
  output1 = tbl('work_W63FDT3V'),
  output2 = tbl('work_W63FDT3W'),
  condition1 = condition1,
  condition2 = condition2
)
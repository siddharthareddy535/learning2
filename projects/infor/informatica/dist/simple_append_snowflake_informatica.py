#sasFilePath: automation_sample/simple_append copy.sas
#conversionTime: 12/23/2024 11:59:02
#linesInFile: 14 #linesOfCode: 5 #linesOfPython: 3
#complexity: 1 #processedBlocks: 1 #passedBlocks: 1
#failedBlocks: 0 #totalErrors: 0

truncate = False

informatica_insertinto(
    source = (tbl("work.w2ow2y4g"), alias("w2ow2y4g")),
    target = tbl("iods.iods_den_imsmidas7_etp"),
    truncate = truncate
)
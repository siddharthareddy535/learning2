#sasFilePath: automation_sample/multi_outputs.sas
#conversionTime: 01/03/2025 02:49:35
#linesInFile: 25 #linesOfCode: 13 #linesOfPython: 17
#complexity: 1 #processedBlocks: 2 #passedBlocks: 2
#failedBlocks: 0 #totalErrors: 0


informatica_insertinto(
    source = (tbl("iods.iods_den_imsmidas1"), alias("iods_den_imsmidas1")),
    target = tbl("work.w63fdt3v"),
    truncate = False,
distinct = False,

)

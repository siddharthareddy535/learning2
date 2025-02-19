sortCols = ['TC_ims_ID']

informatica_insertinto(
    source = tbl("work_w18kls3m"),
    target = tbl("work_W62FC80P"),
truncate = True,
distinct = False,
sortcols = sortCols
)
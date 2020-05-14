# Algorithms

Defined here are the algorithms that are used to insert records into the database, the idea of how the parser works and ways to improve on it.

## Inserting Score Records into the database

Filtering Which Records to be Inserted into the Database.

Proposals:
- Replace the `<Year, YearIndicator>` with `<Semester>` for better Management.

Inserting:
```python3
ToInsertInput = [**data]
for Insert in ToInsertInput:
    Insert If No Conflict
    If Conflict
        Do Update on Record if 
            Record.SemesterWritten < Insert.SemesterWritten
```

Triggers:
```python3
Before Update into SubjectScore:
    Insert Into HistoricalSubjectScore SubjectScore.CurrentData
```

## All Other Records:

Inserting:
```python3 
ToInsertInput = [**data]
for Insert in ToInsertInput:
    Insert If No Conflict
    If Conflict:
        Do Ignore.
```






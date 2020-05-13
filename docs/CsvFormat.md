
# CSV Format
```
USN, Name, Attempted Subjects, [SubCode, Subname,Internals,Externals,Total,Fail/Pass]xAttemptedSubjects
```

# File Naming:

The Files Should be Named in this Order:

```
Data-(Branch)-(Batch)-(Scheme)-(Semester)[-Reval].csv
```

An Example:

For the Batch That has the SerialNumber 1CR16XX001 (Some Number), Attempting their 6th Semester, The filename Must be:

Ensure that this is followed or the application will fail to parse properly.

```
Data-CSE-2016-2015-6.csv
```

If Arrear Results are Present then:

```
Data-CSE-2016-2015-6-Arrear.csv
```

Any File not in this format will be **_ignored_**.

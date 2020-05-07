# Semester Statistics

A project meant to keep an updated record of all scores achieved.

## Database structure

```db
---Student Details
SerialNumber <->
Name
Scheme

---Subject Details
Subject Code <->
Subject Name
Subject Semester
Subject Department

---Departement Details
Department Number
Department Name
Department Code


---Subject Score
SerialNumber <->
SubjectCode <->
Year
Odd/Even
Internals
Externals

---Previous Backlogs + Attempted
Year<->
Odd/Even<->
SerialNumber
SubjectCode
Internals
Externals




```
## File Naming:

The Files Should be Named in this Order:

```
Data-(Batch)-(Scheme)-(Semester).csv
```

An Example: 

For the Batch That has the SerialNumber 1CR16XX001 (Some Number), Attempting their 6th Semester, The filename Must be:

Ensure that this is followed or the application will fail to parse properly.

```
Data-2016-2015-6.csv
```

Any File not in this format will be ***ignored***.

## Calculations Taken within Data:

Note that Per-Scheme-Wise-Plguin is used to allow for differences in changes over the Years By VTU for final Output.

### Must be Specified within the file.

Scheme = Given. This must always be specified since the scheme can vary Even in the same Batch.

Semester = Given. While the Application can determine Which Semester for Storage, this is enforced due to Naming Constraints.

### Calculations Done

- Year = Batch Year + Floor(Semester/2)
- 



## Additional Notes:

Config Parser.

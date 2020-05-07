# Semester Statistics

A project meant to keep an updated record of all scores achieved.

## Database structure

```db
---Student Details
SerialNumber <->
Name
Scheme
Department

---Subject Details
Subject Code <->
Subject Name
Subject Semester
Subject Department

---Departement Details
Department Number <->
Department Code <->
Department Name


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
Data-(Batch)-(Scheme)-(Semester)-[Arrear].csv
```

An Example:

For the Batch That has the SerialNumber 1CR16XX001 (Some Number), Attempting their 6th Semester, The filename Must be:

Ensure that this is followed or the application will fail to parse properly.

```
Data-2016-2015-6.csv
```

If Arrear Results are Present then:

```
Data-2016-2015-6-Arrear.csv
```

Any File not in this format will be **_ignored_**.

## Calculations Taken within Data:

Note that Per-Scheme-Wise-Plguin is used to allow for differences in changes over the Years By VTU for final Output.

### Must be Specified within the file.

Scheme = Given. This must always be specified since the scheme can vary Even in the same Batch.

Semester = Given. While the Application can determine Which Semester for Storage, this is enforced due to Naming Constraints.

### Calculations Done To Be Placed into the Database.

- Batch Year = Parsed from the USN(1CR**17**CS001).
- Year = Batch Year + Floor(Semester/2)
- OddEven = Semester%2 (If Even, then 0, if Odd, then 1)
- DepartmentCode = Taken From Subject (17CS12)
- DepartmentName = Hard Coded


## External Caclulations 

Add Something Here later.
FCD, Etc.
 


## Responses

- Send .docx File <-- Important, After the data done.
- Asking, X Sem, X Scheme something.
- Updating, 401 - If Updating.
- 

## Additional Notes:

Config Parser.

### FrontEnd ? In React.

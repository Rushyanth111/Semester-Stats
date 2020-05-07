# Semester Statistics

Current Version - 0.1-beta.

A project meant to keep an updated record of all scores achieved.

This was started off as a Project to maintain all existing Scores recieved from VTU.

This is a Flexible Data Project that does not require Special Functions as dictated by any college.

Please note that there will be many Changes That can happen Before 

# Database structure

## Department Details

| Property       | Description                | Type       | PK/FK? |
| -------------- | -------------------------- | ---------- | ------ |
| DepartmentCode | Code for the Department    | VARCHAR(2) | PK     |
| DepartmentName | The Name of the Department | TEXT       | -      |


## Student Details

| Property     | Description                              | Type        | PK/FK?           |
| ------------ | ---------------------------------------- | ----------- | ---------------- |
| SerialNumber | University Serial Number                 | VARCHAR(10) | PK               |
| Name         | Name of the Student                      | TEXT        | -                |
| Scheme       | The Scheme They Belong to in YYYY Format | INTEGER(4)  | -                |
| Department   | The Code of the Department               | VARCHAR(2)  | FK -> Department |


## Subject Details

| Property           | Description                            | Type       | PK/FK?           |
| ------------------ | -------------------------------------- | ---------- | ---------------- |
| SubjectCode        | Code of the Subject in Official VTU    | VARCHAR(7) | PK               |
| Subject Name       | Name of the Subject                    | TEXT       | -                |
| Subject Semester   | Semester the Subject Appears in        | INTEGER    | -                |
| Subject Department | Department that the subject Belings to | VARCHAR(2) | FK -> Department |


## Subject Score

| Property     | Description                          | Type        | PK/FK?                    |
| ------------ | ------------------------------------ | ----------- | ------------------------- |
| SerialNumber | USN of the Student                   | VARCHAR(10) | PK, FK -> Student Details |
| SubjectCode  | Subject Code.                        | VARCHAR(7)  | Pk, FK -> Subject Details |
| Year         | Year of Examination                  | INTEGER     | -                         |
| Odd/Even     | Was Conduted in ODD or EVEN Semester | BOOLEAN     | -                         |
| Internals    | Internal Marks                       | INTEGER     | -                         |
| Externals    | External Marks                       | INTEGER     | -                         |

## Backlog Subject Score


| Property     | Description                          | Type        | PK/FK?                |
| ------------ | ------------------------------------ | ----------- | --------------------- |
| Year         | Year of Examination                  | INTEGER     | PK                    |
| Odd/Even     | Was Conduted in ODD or EVEN Semester | BOOLEAN     | PK                    |
| SerialNumber | USN of the Student                   | VARCHAR(10) | FK -> Student Details |
| SubjectCode  | Subject Code                         | VARCHAR(7)  | FK -> Subject Details |
| Internals    | Internal Marks                       | INTEGER     | -                     |
| Externals    | External Marks                       | INTEGER     | -                     |

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

# Calculations

Note that Per-Scheme-Wise-Plguin (Is detailed in [External Calculations](#external-caclulations)) is used to allow for differences in changes over the Years By VTU for final Output.

## Must be Specified On the filename.

Scheme = Given. This must always be specified since the scheme can vary Even in the same Batch.

Semester = Given. While the Application can determine Which Semester for Storage, this is enforced due to Naming Constraints.

Batch = Given. Specified Within the filename.

## Calculations Done To Be Placed into the Database.

- Year = Batch Year + Floor(Semester/2)
- OddEven = Semester%2 (If Even, then 0, if Odd, then 1)
- DepartmentCode = Taken From Subject (17CS12)
- DepartmentName = Hard Coded

# External Caclulations

This Section Maintains the Various Calculations Needed for Other Statistics.

## Scheme - 18

```
To be added
```

---

## Scheme - 17

```
To be added
```

---

## Scheme - 15

```
To be added
```

---

## Scheme - 10

Note that Scheme 10 is currently ignored because of the lack of data.

---

# API

```
To be Decided
```

## Routes

```
To Be Decided.
```

# React Front End

Hosting at https://semdata.rxav.pw

# Performance

Currently, 3 full 200 Lists of Students Take up ~10seconds on a fully cold Start.

Further Performance is to be tested.

# Additional Notes:

Additional Things Needed to be implemented.

- Configuration File.
- Docx Formatter.
- PDF Formatter.
- Flexible API Syntax.
- Proper Structure.
- Documentation. <- Mostly for future Maintence.

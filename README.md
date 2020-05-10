# Semester Statistics

Current Version - 0.1-beta.

A project meant to keep an updated record of all scores achieved.

This was started off as a Project to maintain all existing Scores recieved from VTU.

This is a Flexible Data Project that does not require Special Functions as dictated by any college.

Please note that there will be many Changes That can happen Before 

# Database structure

## Department Details

| Property       | Description                | Type       | PK/FK? | Indexed |
| -------------- | -------------------------- | ---------- | ------ | ------- |
| DeparmentId    | A surrogate Key            | INT        | PK     | No      |
| DepartmentCode | Code for the Department    | VARCHAR(2) | PK     | No      |
| DepartmentName | The Name of the Department | TEXT       | -      | No      |


## Student Details

| Property         | Description                             | Type        | PK/FK?           | Indexed |
| ---------------- | --------------------------------------- | ----------- | ---------------- | ------- |
| StudentDetailsID | A Surrogate Key                         | INT         | PK               | Yes     |
| SerialNumber     | University Serial Number                | VARCHAR(10) | PK               | Yes     |
| Name             | Name of the Student                     | TEXT        | -                | No      |
| Batch            | The Batch They Belong to in YYYY Format | INTEGER(4)  | -                | No      |
| Department       | The Code of the Department              | VARCHAR(2)  | FK -> Department | No      |

## BatchSchemeInfo

| Property | Description        | Type | PK/FK? | Indexed |
| -------- | ------------------ | ---- | ------ | ------- |
| Batch    | Batch Detail YYYY  | INT  | PK, CK | No      |
| Scheme   | Scheme Number YYYY | INT  | PK, CK | No      |


## Subject Details

| Property          | Description                            | Type       | PK/FK?           | Indexed |
| ----------------- | -------------------------------------- | ---------- | ---------------- | ------- |
| SubjectDetailId   | A Surrogate Key                        | INT        | PK               | Yes     |
| SubjectCode       | Code of the Subject in Official VTU    | VARCHAR(7) | PK               | Yes     |
| SubjectName       | Name of the Subject                    | TEXT       | -                | No      |
| SubjectSemester   | Semester the Subject Appears in        | INTEGER    | -                | No      |
| SubjectDepartment | Department that the subject Belings to | VARCHAR(2) | FK -> Department | No      |


## Subject Score

| Property       | Description                          | Type        | PK/FK?                    | Indexed |
| -------------- | ------------------------------------ | ----------- | ------------------------- | ------- |
| SubjectScoreID | A Surrogate Key                      | INT         | PK                        | Yes     |
| SerialNumber   | USN of the Student                   | VARCHAR(10) | PK, FK -> Student Details | Yes     |
| SubjectCode    | Subject Code.                        | VARCHAR(7)  | Pk, FK -> Subject Details | Yes     |
| Year           | Year of Examination                  | INTEGER     | -                         | No      |
| Odd/Even       | Was Conduted in ODD or EVEN Semester | BOOLEAN     | -                         | No      |
| Internals      | Internal Marks                       | INTEGER     | -                         | No      |
| Externals      | External Marks                       | INTEGER     | -                         | No      |

## Backlog Subject Score


| Property     | Description                          | Type        | PK/FK?                | Indexed |
| ------------ | ------------------------------------ | ----------- | --------------------- | ------- |
| Year         | Year of Examination                  | INTEGER     | PK                    | No      |
| Odd/Even     | Was Conduted in ODD or EVEN Semester | BOOLEAN     | PK                    | No      |
| SerialNumber | USN of the Student                   | VARCHAR(10) | FK -> Student Details | No      |
| SubjectCode  | Subject Code                         | VARCHAR(7)  | FK -> Subject Details | No      |
| Internals    | Internal Marks                       | INTEGER     | -                     | No      |
| Externals    | External Marks                       | INTEGER     | -                     | No      |

## TeacherDetails

| Property    | Description                   | Type | PK/FK? | Indexed |
| ----------- | ----------------------------- | ---- | ------ | ------- |
| TeacherId   | An ID for the given teacher   | INT  | PK     | No      |
| TeacherName | The Name of the Given teacher | TEXT | -      | No      |

## TeacherBatchDetails

| Property     | Description                  | Type       | PK/FK?                | Indexed |
| ------------ | ---------------------------- | ---------- | --------------------- | ------- |
| TeacherId    | an ID for the given teacher. | INT        | FK -> TeacherDetails  | Yes     |
| Batch        | YYYY Batch                   | INT        | PK,FK -> BatchDetails | No      |
| Subject Code | YYYY Batch                   | VARCHAR(7) | --                    | No      |


# CSV Format
```
USN, Name, Attempted Subjects, [SubCode, Subname,Internals,Externals,Total,Fail/Pass]xAttemptedSubjects
```

# File Naming:

The Files Should be Named in this Order:

```
Data-(Branch)-(Batch)-(Scheme)-(Semester)-[Arrear].csv
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

### [POST] /student/list/

Retrieves the student list from the database given the following POST request scheme
An Example Post Request:
```jsonc
{
    "Scheme":2015, //Integer
    "Batch":2016, //Integer
    "Semester":6, //Integer
}
```

An Example Response (If given to the above.) Will be:

```jsonc
[{
    "Name":"SomeName",
    "USN":"1CX16CS017",
    "Section":"", //Currently Unavailable.
    "Marks":[ //An Array of Marks, Per Code.
        {
            "Code":"15CS61",
            "Internal":18, //Integer 
            "External":56, //Integer
            "Total":64, //Integer
            "Result":"Pass",
            "Class":"FCD",
        },
        //Similar Objects as above.
    ],
    "Overall":{
        "Total":560,
        "Result":"Pass",
    } //Only One Object.
}
// More Objects Like the one Above, Based on your request.
]
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

# Problems:

USNs that change.
Diploma? 
Arrears -- Designed, Data? Inconsistent.
Missing Data? 

-> Data: 
If USN + Code In new? 
    OldTable <= Previous

Else Insert.
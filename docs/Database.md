
# Database structure

## Department Details

| Property       | Description                | Type       | PK/FK? | Indexed |
| -------------- | -------------------------- | ---------- | ------ | ------- |
| DepartmentCode | Code for the Department    | VARCHAR(2) | PK     | No      |
| DepartmentName | The Name of the Department | TEXT       | -      | No      |


## Student Details

| Property     | Description                             | Type        | PK/FK?           | Indexed |
| ------------ | --------------------------------------- | ----------- | ---------------- | ------- |
| SerialNumber | University Serial Number                | VARCHAR(10) | PK               | Yes     |
| Name         | Name of the Student                     | TEXT        | -                | No      |
| Batch        | The Batch They Belong to in YYYY Format | INTEGER(4)  | -                | No      |
| Department   | The Code of the Department              | VARCHAR(2)  | FK -> Department | No      |

## BatchSchemeInfo

| Property | Description        | Type | PK/FK? | Indexed |
| -------- | ------------------ | ---- | ------ | ------- |
| Batch    | Batch Detail YYYY  | INT  | PK, CK | No      |
| Scheme   | Scheme Number YYYY | INT  | -      | No      |


## Subject Details

| Property          | Description                            | Type       | PK/FK?           | Indexed |
| ----------------- | -------------------------------------- | ---------- | ---------------- | ------- |
| SubjectCode       | Code of the Subject in Official VTU    | VARCHAR(7) | PK               | Yes     |
| SubjectName       | Name of the Subject                    | TEXT       | -                | No      |
| SubjectSemester   | Semester the Subject Appears in        | INTEGER    | -                | No      |
| SubjectDepartment | Department that the subject Belings to | VARCHAR(2) | FK -> Department | No      |


## Subject Score

| Property     | Description                     | Type        | PK/FK?                    | Indexed |
| ------------ | ------------------------------- | ----------- | ------------------------- | ------- |
| SerialNumber | USN of the Student              | VARCHAR(10) | PK, FK -> Student Details | Yes     |
| SubjectCode  | Subject Code.                   | VARCHAR(7)  | Pk, FK -> Subject Details | Yes     |
| Year         | Year the Subject was Written In | INTEGER     | -                         | No      |
| Year         | Odd/Even                        | BOOL        | -                         | No      |
| Internals    | Internal Marks                  | INTEGER     | -                         | No      |
| Externals    | External Marks                  | INTEGER     | -                         | No      |

## HistoricalSubject Score


| Property     | Description                     | Type        | PK/FK?                | Indexed |
| ------------ | ------------------------------- | ----------- | --------------------- | ------- |
| SerialNumber | USN of the Student              | VARCHAR(10) | FK -> Student Details | No      |
| SubjectCode  | Subject Code                    | VARCHAR(7)  | FK -> Subject Details | No      |
| Year         | Year the Subject was Written In | INTEGER     | -                     | No      |
| Year         | Odd/Even                        | BOOL        | -                     | No      |
| Internals    | Internal Marks                  | INTEGER     | -                     | No      |
| Externals    | External Marks                  | INTEGER     | -                     | No      |

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


## ParsedTable
| Property   | Description         | Type       | PK/FK?                   | Indexed |
| ---------- | ------------------- | ---------- | ------------------------ | ------- |
| Department | The Department Code | VARCHAR(3) | FK -> DepartmentDetails  | No      |
| Batch      | The Batch Parsed    | INT        | FK -> BatchSchemeDetails | No      |
| Semester   | The Semester Parsed | INT        | -                        | No      |
| Arrear     | If Reval Result     | Bool       | -                        | No      |

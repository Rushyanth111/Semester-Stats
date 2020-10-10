# Student Endpoint

!!! info

    `{usn}` reffers to the **_STRING_** representing a particular students. For example, USN `1CX16CS118`

    `{semester}` refferes to the **_INTEGER** representing a particular semester.

!!! warning "Notes to Keep Track of"

    Note: All of the Path Parameters are REQUIRED

    Note: ALL Of the Query Parameters are Optional.

## General Error Codes:

| Code | Desc            |
| ---- | --------------- |
| 404  | Batch Not Found |

## Student Get

- Endpoint: `GET /student​/{usn}`
- Function: Get a Student

Example Request:

```py
/student/1CX15IS001
```

Example Response:

```json
{
  "Usn": "1CX15IS001",
  "Name": "SOME NAME",
  "Batch": 2015,
  "Department": "IS"
}
```

## Student Get Scores

- Endpoint: `GET /student​/{usn}​/scores`
- Function: Get All Scores of a Student, And Filter by Semester if needed.
- Query Params:

| Param | Description       |
| ----- | ----------------- |
| `sem` | Integer: Semester |

Example Request:

```py
/student/1CX15IS001/scores?sem=7
```

Example Response:

```json
[
  {
    "Usn": "1CR16CS001",
    "SubjectCode": "15CS71",
    "Internals": 40,
    "Externals": 60
  },
  {
    "Usn": "1CR16CS001",
    "SubjectCode": "15CS72",
    "Internals": 1,
    "Externals": 3
  }
]
```

## Student Get Backlog

- Endpoint: `GET /student​/{usn}​/backlogs`
- Function: Get All Backlogs of a Student
- Query Params:

| Param | Description       |
| ----- | ----------------- |
| `sem` | Integer: Semester |

Example Request:

```py
/student/1CX15IS001/backlogs?sem=7
```

Example Response:

```json
[
  {
    "Usn": "1CR16CS001",
    "SubjectCode": "15CS71",
    "Internals": 40,
    "Externals": 60
  },
  {
    "Usn": "1CR16CS001",
    "SubjectCode": "15CS72",
    "Internals": 1,
    "Externals": 3
  }
]
```

## Student Get Subject Score

- Endpoint: `GET /student​/{usn}​/subject​/{subcode}`
- Function: Get Subject Score for A Student.

Example Request:

```py
/student/1CX15IS001/subject/15CX551
```

Example Response:

```json
{
  "Usn": "1CX15IS001",
  "SubjectCode": "17CS551",
  "Internals": 73,
  "Externals": 79
}
```

## Student Insert

- Endpoint: `POST /student​/`
- Function: Insert a Student into the Database
- Error Codes:

| Code | Desc                 |
| ---- | -------------------- |
| 409  | Conflict in Database |

Documentation Not Available Yet.

## Student Update

- Endpoint: `PUT /student​/{usn}`
- Function: Update a Student in the Database.
- Error Codes:

| Code | Desc                 |
| ---- | -------------------- |
| 409  | Conflict in Database |

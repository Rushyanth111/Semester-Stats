# Student Endpoint

!!! info

    `{usn}` reffers to the **_STRING_** representing a particular students. For example, USN `1CX16CS118`

    `{semester}` refferes to the **_INTEGER** representing a particular semester.

!!! warning "Notes to Keep Track of"

    Note: All of the Path Parameters are REQUIRED

    Note: ALL Of the Query Parameters are Optional.

## Student Get

- Endpoint: `GET /student​/{usn}`
- Function: Get a Student
- Query Params: None

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
  "Department": "IS",
  "Scores": [] //Empty.
}
```

## Student Get Scores

- Endpoint: `GET /student​/{usn}​/scores`
- Function: Get All Scores of a Student
- Query Params: None

Example Request:

```py
/student/1CX15IS001/scores
```

Example Response:

```json

```

## Student Get Semester Scores

- Endpoint: `GE ​/student​/{usn}​/{semester}`
- Function: Get All Scores of a Student for a particular Semester.
- Query Params: None

Example Request:

```py
/student/1CX15IS001/6
```

Example Response:

```json
[
  {
    "Usn": "1CX15IS001",
    "SubjectCode": "17CS551",
    "Internals": 10,
    "Externals": 77
  },
  {
    "Usn": "1CX15IS001",
    "SubjectCode": "17CS552",
    "Internals": 73,
    "Externals": 79
  }
]
```

## Student Get Backlog

- Endpoint: `GET /student​/{usn}​/backlogs`

!!! warning

    Do not Use Yet.

## Student Get Subject Score

- Endpoint: `GET /student​/{usn}​/subject​/{subcode}`
- Function: Get Subject Score for A Student.
- Query Params: None

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

!!! warning

    Do not Use Yet.

- Endpoint: `POST /student​/`

## Student Update

!!! warning

    Do not Use Yet.

- Endpoint: `PUT /student​/{usn}`

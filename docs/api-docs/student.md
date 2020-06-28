Handles all of the **Induvidual** student documentation.

!!! warning "API Subject to changes."
As a Small warning, all of the below API routes mentioned can be changed at any moment.

!!! abstract "API Parameters Glossary."

    {student} refers to the USN of a particular student.

    {semester} is an integer that referers to a particular semester from 1 to 8.

## GET /student/{student}/summary

This route gets you all of the Summary data that is available

Example Request:

```
/student/1XM17ME001/summary
```

An Example Response Would Be:

```json
{
  "StudentUSN": "1CR16CS024",
  "StudentName": "ANURODH  VERMA",
  "StudentBatch": 2016,
  "StudentDepartment": {
    "DepartmentCode": "CS",
    "DepartmentName": "Computer Science and Engineering"
  }
}
```

## GET /student/{student}/backlogs

This route gets you all of the backlogs for that particular student

Example Request:

```
/student/1XM17ME001/backlog
```

Example Response:

```json
[
  {
    "ScoreSerialNumber": "1CR16CS005",
    "ScoreSubjectCode": "15CS53",
    "ScoreSemester": 6,
    "ScoreInternals": 12,
    "ScoreExternals": 14
  },
  {
    "ScoreSerialNumber": "1CR16CS005",
    "ScoreSubjectCode": "15CS61",
    "ScoreSemester": 6,
    "ScoreInternals": 14,
    "ScoreExternals": 29
  },
  ...
]
```

!!! note
This route may return nothing.

## GET /student/{student}/{semester}

Fetches the the details of the student for a given semester(Includes merged Arrear Details).

Example Request:

```
/student/1XM17ME001/6
```

Example Response:

```json
[
  {
    "ScoreSerialNumber": "1CR16CS024",
    "ScoreSubjectCode": "15CS553",
    "ScoreSemester": 6,
    "ScoreInternals": 12,
    "ScoreExternals": 28
  },
  {
    "ScoreSerialNumber": "1CR16CS024",
    "ScoreSubjectCode": "15CS562",
    "ScoreSemester": 6,
    "ScoreInternals": 12,
    "ScoreExternals": 28
  },
  {
    "ScoreSerialNumber": "1CR16CS024",
    "ScoreSubjectCode": "15CS63",
    "ScoreSemester": 6,
    "ScoreInternals": 12,
    "ScoreExternals": 29
  },
  {
    "ScoreSerialNumber": "1CR16CS024",
    "ScoreSubjectCode": "15CS653",
    "ScoreSemester": 6,
    "ScoreInternals": 12,
    "ScoreExternals": 46
  },
  {
    "ScoreSerialNumber": "1CR16CS024",
    "ScoreSubjectCode": "15CSL67",
    "ScoreSemester": 6,
    "ScoreInternals": 13,
    "ScoreExternals": 46
  },
  {
    "ScoreSerialNumber": "1CR16CS024",
    "ScoreSubjectCode": "15CSL68",
    "ScoreSemester": 6,
    "ScoreInternals": 14,
    "ScoreExternals": 55
  }
]
```

This route gets the details of that student for a particular semester.

!!! note
This route may return nothing.

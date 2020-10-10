# Batch Endpoint

!!! info

    `{batch}` reffers to the **_INTEGER_** representing a particular batch of students. For example, Batch `2017` would be the people who are admitted from the year 2017 and onward.

!!! warning "Notes to Keep Track of"

    Note: All of the Path Parameters are REQUIRED

    Note: ALL Of the Query Parameters are Optional.

## Batch Get Students

- Endpoint: `GET ​/batch​/`
- Function: Get all of the Batches Available.

Example Request:

```py
/batch/
```

Example Response:

```json
[2015, 2016, 2017, 2018]
```

## Batch Get Scores

- Endpoint: `GET /batch​/{batch}​/scores`
- Function: Get the Scores of All of the Students in a batch.

- Query Params:

| Param  | Description            |
| ------ | ---------------------- |
| `dept` | 2 Digit Deparment Code |
| `sem`  | Integer: Semester      |

- Error Codes:

| Code | Desc            |
| ---- | --------------- |
| 404  | Batch Not Found |

Example Request:

```py
/batch/2017/scores?dept=CS&sem=7
```

Example Response:

```jsonc
[
  {
    "Usn": "1CR16CS001",
    "Name": "Roy Harris",
    "Batch": 2016,
    "Department": "CS",
    "Scores": [
      { "SubjectCode": "15CS71", "Internals": 40, "Externals": 60 },
      { "SubjectCode": "15CS72", "Internals": 40, "Externals": 60 }
    ]
  }
]
```

## Batch Get Detained

- Endpoint: `GET /batch​/{batch}​/detained`
- Function: Get the Detained Students _and_ their Scores.

- Query Params:

| Param    | Description                           |
| -------- | ------------------------------------- |
| `dept`   | 2 Digit Deparment Code                |
| `thresh` | Threshold for Detained, Defaults to 4 |

- Error Codes:

| Code | Desc            |
| ---- | --------------- |
| 404  | Batch Not Found |

Example Request:

```py
/batch/2017/detained?dept=CS&thresh=3
```

Example Response:

```jsonc
[
  {
    "Usn": "1CR16CS001",
    "Name": "Roy Harris",
    "Batch": 2016,
    "Department": "CS",
    "Scores": [{ "SubjectCode": "15CS71", "Internals": 1, "Externals": 2 }]
  }
]
```

## Batch Get Backlogs

- Endpoint: `GET /batch​/{batch}​/backlogs`
- Function: Get the Backlog Scores.

- Query Params:

| Param  | Description            |
| ------ | ---------------------- |
| `dept` | 2 Digit Deparment Code |
| `sem`  | Integer: Semester      |

- Error Codes:

| Code | Desc            |
| ---- | --------------- |
| 404  | Batch Not Found |

Example Request:

```py
/batch/2017/backlogs?dept=CS&sem=6
```

Example Response:

```jsonc
[
  {
    "Usn": "1CR16CS001",
    "Name": "Roy Harris",
    "Batch": 2016,
    "Department": "CS",
    "Scores": [{ "SubjectCode": "15CS71", "Internals": 1, "Externals": 2 }]
  }
]
```

## Batch Get Aggregate

- Endpoint: `GET /batch​/{batch}​/aggregate`
- Function: Get the total of all scores for a batch.
- Query Params:

| Param  | Description            |
| ------ | ---------------------- |
| `dept` | 2 Digit Deparment Code |

Example Request:

```py
/batch/2017/aggregate
```

Example Response:

```py
[
    ["USN1", 800],
    ["USN2", 450],
    ["USN3", 600],
    ...
]
```

## Batch Search

- Endpoint: `POST /batch​/{batch}​/search`

!!! warning

      Deprecated. DO NOT USE.

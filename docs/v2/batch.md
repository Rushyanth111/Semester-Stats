# Batch Endpoint

!!! info

    `{batch}` reffers to the **_INTEGER_** representing a particular batch of students. For example, Batch `2017` would be the people who are admitted from the year 2017 and onward.

!!! warning "Notes to Keep Track of"

    Note: All of the Path Parameters are REQUIRED

    Note: ALL Of the Query Parameters are Optional.

## Batch Get Students

- Endpoint: `GET ​/batch​/{batch}`
- Function: Get the Students of a Particular batch.

- Query Params:

  | Param  | Description            |
  | ------ | ---------------------- |
  | `dept` | 2 Digit Deparment Code |

Example Request:

```py
/batch/2017
```

Example Response:

```json
[
  {
    "Usn": "Some USN",
    "Name": "XVX",
    "Batch": 2017,
    "Department": "DEPTCODE",
    "Scores": [] //Note that this will be Empty.
  },
  {
    "Usn": "Some USN",
    "Name": "XVX",
    "Batch": 2017,
    "Department": "DEPTCODE",
    "Scores": [] //Note that this will be Empty.
  }
]
```

## Batch Get Scores

- Endpoint: `GET /batch​/{batch}​/scores`
- Function: Get the Scores of All of the Students in a batch.

- Query Params:

| Param  | Description            |
| ------ | ---------------------- |
| `dept` | 2 Digit Deparment Code |
| `sem`  | Integer: Semester      |

Example Request:

```py
/batch/2017/scores?dept=CS&sem=6
```

Example Response:

```py
[
  {
    "Usn": "SOMEUSN",
    "Name": "SOME NAME",
    "Batch": 2017,
    "Department": "CS",
    "Scores": [
      {
        "Usn": "SOME USN",
        "SubjectCode": "SOME CODE",
        "Internals": 50,
        "Externals": 60
      },
      ...
    ]
  },
  ...
]
```

## Batch Get Student Usns

- Endpoint: `GET batch​/{batch}​/usns`
- Function: Only Retrives Usn as a List
- Query Params:

| Param  | Description            |
| ------ | ---------------------- |
| `dept` | 2 Digit Deparment Code |

Example Request:

```py
/batch/2017/usns
```

Example Response:

```py
[
    "USN1",
    "USN2",
    "USN3",
]
```

## Batch Get Scheme

- Endpoint: `GET /batch​/{batch}​/scheme`
- Function: Get the Scheme of a Batch
- Query Params: None

Example Request:

```py
/batch/2016/scheme
```

Example Response:

```py
2015
```

## Batch Get Detained

- Endpoint: `GET /batch​/{batch}​/detained`

!!! warning

      Deprecated. DO NOT USE.

## Batch Get Backlogs

- Endpoint: `GET /batch​/{batch}​/backlogs`

!!! warning

      Deprecated. DO NOT USE.

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

## GET /batch/{department}/{batch}/{semester}/detail

Example Request:

```
/batch/CS/2017/5/detail
```

Example Response:

```json
[
  {
    "USN": "1CR17CS001",
    "17CS51": [36, 42],
    "17CS52": [37, 36],
    "17CS53": [33, 32],
    "17CS54": [34, 36],
    "17CS553": [40, 41],
    "17CS564": [36, 39],
    "17CSL57": [40, 57],
    "17CSL58": [39, 50]
  },
  {
    "USN": "1CR17CS002",
    "17CS51": [23, 37],
    "17CS52": [20, 0],
    "17CS53": [19, 28],
    "17CS54": [20, 0],
    "17CS553": [19, 28],
    "17CS564": [19, 29],
    "17CSL57": [32, 48],
    "17CSL58": [23, 38]
  },
  ...
]
```

### GET /batch/{department}/{batch}/{semester}/summary

Example Request:

```
/batch/CS/2017/5/summary
```

Example Response:

```json
{
  "15CS81": {
    "TotalAttendees": 198,
    "FCD": 0,
    "FC": 1,
    "SC": 5,
    "PassPercentage": 98.48484848484848,
    "FailPercentage": 1.5151515151515156,
    "Pass": 195,
    "Fail": 3
  },
  "15CS832": {
    "TotalAttendees": 198,
    "FCD": 0,
    "FC": 3,
    "SC": 4,
    "PassPercentage": 98.98989898989899,
    "FailPercentage": 1.0101010101010104,
    "Pass": 196,
    "Fail": 2
  },
  "15CS82": {
    "TotalAttendees": 198,
    "FCD": 3,
    "FC": 1,
    "SC": 3,
    "PassPercentage": 98.98989898989899,
    "FailPercentage": 1.0101010101010104,
    "Pass": 196,
    "Fail": 2
  },
  "15CS84": {
    "TotalAttendees": 198,
    "FCD": 8,
    "FC": 1,
    "SC": 1,
    "PassPercentage": 100.0,
    "FailPercentage": 0.0,
    "Pass": 198,
    "Fail": 0
  },
  "15CSP85": {
    "TotalAttendees": 198,
    "FCD": 9,
    "FC": 0,
    "SC": 0,
    "PassPercentage": 100.0,
    "FailPercentage": 0.0,
    "Pass": 198,
    "Fail": 0
  },
  "SubjectCodes": ["15CS81", "15CS832", "15CS82", "15CS84", "15CSP85"],
  "SubjectFailArray": [3, 2, 2, 0, 0],
  "SubjectPassArray": [195, 196, 196, 198, 198],
  "SubjectFCDArray": [0, 0, 3, 8, 9],
  "SubjectFCArray": [1, 3, 1, 1, 0],
  "SubjectSCArray": [5, 4, 3, 1, 0],
  "TotalAttendees": 198,
  "FCD": 0,
  "FC": 2,
  "SC": 7,
  "Pass": 198,
  "Fail": 0,
  "PassPercentage": 100.0,
  "FailPercentage": 0.0
}
```

### GET /batch/{department}/{batch}/list

Example Request:

```
/batch/CS/2017/5/list
```

Example Response:

```json
[
  {
    "StudentUSN": "1CR17CS001",
    "StudentName": "A VIDHYA",
    "StudentBatch": 2017,
    "StudentDepartment": "CS"
  },
  {
    "StudentUSN": "1CR17CS002",
    "StudentName": "AADITYA RANJAN",
    "StudentBatch": 2017,
    "StudentDepartment": "CS"
  },
  {
    "StudentUSN": "1CR17CS003",
    "StudentName": "AAYUSH LAL ROY",
    "StudentBatch": 2017,
    "StudentDepartment": "CS"
  },
  ...
]
```

### GET /batch/{department}/{batch}/backlogs

Example Request:

```zsh
/batch/CS/2016/backlogs
```

```json
[
  {
    "USN": "1CR16CS003",
    "15ELE15": [12, 15],
    "15MAT11": [7, 16],
    "15MAT21": [12, 2]
  },
  {
    "USN": "1CR16CS005",
    "15CS53": [12, 14],
    "15CS61": [14, 29],
    "15CS62": [12, 23],
    "15CS63": [12, 29],
    "15CS64": [12, 32],
    "15CS651": [13, 16],
    "15CS664": [13, 28],
    "15CS71": [13, 23],
    "15CS72": [13, 21],
    "15CS73": [12, 18],
    "15CS754": [15, 28]
  }
]
```

### GET batch/{department}/{batch}/{semester}/sfile

Obtain the report file for that particular semester.

Example Request:

```zsh
batch/CS/2016/6/sfile
```

No Example Response, it directly links to the download file

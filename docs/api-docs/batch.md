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
  "17CS51": {
    "TotalAttendees": 183,
    "FCD": 65,
    "FC": 72,
    "SC": 35,
    "PassPercentage": 98.90710382513662,
    "FailPercentage": 1.0928961748633839
  },
  "17CS52": {
    "TotalAttendees": 183,
    "FCD": 73,
    "FC": 46,
    "SC": 44,
    "PassPercentage": 96.17486338797814,
    "FailPercentage": 3.825136612021865
  },
  "17CS53": {
    "TotalAttendees": 183,
    "FCD": 41,
    "FC": 61,
    "SC": 54,
    "PassPercentage": 90.1639344262295,
    "FailPercentage": 9.836065573770497
  },
  "17CS553": {
    "TotalAttendees": 183,
    "FCD": 68,
    "FC": 43,
    "SC": 43,
    "PassPercentage": 92.89617486338798,
    "FailPercentage": 7.103825136612016
  },
  "17CS564": {
    "TotalAttendees": 183,
    "FCD": 78,
    "FC": 41,
    "SC": 42,
    "PassPercentage": 93.44262295081967,
    "FailPercentage": 6.557377049180332
  },
  "17CS54": {
    "TotalAttendees": 183,
    "FCD": 38,
    "FC": 55,
    "SC": 57,
    "PassPercentage": 87.97814207650273,
    "FailPercentage": 12.021857923497265
  },
  "17CSL57": {
    "TotalAttendees": 183,
    "FCD": 145,
    "FC": 17,
    "SC": 5,
    "PassPercentage": 100.0,
    "FailPercentage": 0.0
  },
  "17CSL58": {
    "TotalAttendees": 183,
    "FCD": 156,
    "FC": 4,
    "SC": 6,
    "PassPercentage": 100.0,
    "FailPercentage": 0.0
  },
  "SubjectCodes": [
    "17CS51",
    "17CS52",
    "17CS53",
    "17CS553",
    "17CS564",
    "17CS54",
    "17CSL57",
    "17CSL58"
  ],
  "TotalAttendees": 183,
  "FCD": 664,
  "FC": 339,
  "SC": 286,
  "PassPercentage": 59.56284153005465,
  "FailPercentage": 40.43715846994535
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

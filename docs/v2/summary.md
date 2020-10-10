# Summary Endpoint

!!! info

    `{dept}` reffers to the **_STRING_** representing a particular department. For example, `CS`

    `{batch}` reffers to the **_INTEGER_** representing a particular batch of students. For example, Batch `2017` would be the people who are admitted from the year 2017 and onward.

    `{sem}` reffers to the ***Integer*** for a given Semester.

!!! warning "Notes to Keep Track of"

    Note: All of the Path Parameters are REQUIRED

    Note: ALL Of the Query Parameters are Optional.

## General Error Codes;

| Code | Desc            |
| ---- | --------------- |
| 404  | Dept Not Found  |
| 404  | Batch Not Found |
| 404  | No Scores Found |

## Get Document

- Endpoint: `GET /{batch}/{dept}/{sem}`
- Function: Get the Summary Having the Summary of The Above.

- Example Request:

```py
/summary/2015/CS/6/
```

```jsonc
{
  "Appeared": 45,
  "Fcd": 42,
  "Fc": 23,
  "Sc": 56,
  "Pass": 41,
  "Fail": 56,
  "PassPercent": 49.45,
  "Subjects": {
    "15CS65": {
      "Appeared": 29,
      "Failed": 30,
      "Fcd": 41,
      "Fc": 34,
      "Sc": 51,
      "PassPercent": 54.65,
      "Pass": 53
    },
    "15CS66": {
      "Appeared": 29,
      "Failed": 30,
      "Fcd": 41,
      "Fc": 34,
      "Sc": 51,
      "PassPercent": 54.65,
      "Pass": 53
    }
  }
}
```

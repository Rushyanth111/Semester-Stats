# Document Endpoint

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

- Endpoint: `GET /{batch}/{dept}/{sem}/docx`
- Function: Get the Document Having the Summary of The Above.

- Example Request:

```py
/docs/2015/CS/6/docx
```

- Response will be a Downloadable File.

# Subject Endpoint

!!! info

    `{subject}` reffers to the **_STRING_** representing a particular subject. For example, `15CS551`

!!! warning "Notes to Keep Track of"

    Note: All of the Path Parameters are REQUIRED

    Note: ALL Of the Query Parameters are Optional.

## Subject Get

- Endpoint: `GET ​/subject​/{subcode}`
- Function:
- Query Params: None

Example Request:

```py
/subject/15CS551
```

Example Response:

```json
{
  "Code": "15CS551",
  "Name": "Some Subject",
  "Semester": 5,
  "Scheme": 2015,
  "Department": "CS"
}
```

## Subject Update

!!! warning

    Do Not Use Yet.

- Endpoint: `PUT ​/subject​/{subcode}`

## Subject Insert

!!! warning

    Do Not Use Yet.

- Endpoint: `POST ​/subject​/`

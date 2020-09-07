# Department Endpoint

!!! info

    `{dept}` reffers to the **_STRING_** representing a particular department. For example, `CS`

!!! warning "Notes to Keep Track of"

    Note: All of the Path Parameters are REQUIRED

    Note: ALL Of the Query Parameters are Optional.

## Department Get

-Endpoint: `GET /dept​/{dept}`

- Function:
- Query Params: None

Example Request:

```py
/dept/CS
```

Example Response:

```json
{
  "Code": "CS",
  "Name": "Computer Science and Enginerring."
}
```

## Department Update

!!! warning

    Do Not Use

-Endpoint: `PUT /dept​/{dept}`

## Department Add

!!! warning

    Do Not Use

-Endpoint: `POST /dept​/`

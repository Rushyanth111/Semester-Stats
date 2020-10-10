# Department Endpoint

!!! info

    `{dept}` reffers to the **_STRING_** representing a particular department. For example, `CS`

!!! warning "Notes to Keep Track of"

    Note: All of the Path Parameters are REQUIRED

    Note: ALL Of the Query Parameters are Optional.

## General Error Codes;

| Code | Desc           |
| ---- | -------------- |
| 404  | Dept Not Found |

## Department Get All

- Endpoint: `GET /dept/`
- Function: Gets all of the Available Batches.
- Query Params: None

```py
/dept/
```

Example Response:

```json
["CS", "TE", "XE", "XS", "SS"]
```

## Department Get

- Endpoint: `GET /dept​/{dept}`
- Function: Get the Details of a Single Department.
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

- Endpoint: `PUT /dept​/{dept}`
- Function: Update a Given Department.

Documentation Unavailable.

## Department Add

- Endpoint: `POST /dept​/`
- Function: Add a Given Department.

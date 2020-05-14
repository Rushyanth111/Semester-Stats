# API

## Routes
- /student
  - /student/list
  - /student/


# [POST] /student/list/

Retrieves the student list from the database given the following POST request scheme


An Example POST Request:
```javascript
{
    "Department":"CS", //string
    "Batch":2016, //Integer
    "Semester":6, //Integer
}
```

An Example Response (If given to the above.) Will be:

```javascript
[{
    "Name":"SomeName",
    "USN":"1CX16CS017",
    "Section":"", //Currently Unavailable.
    "Marks":[ //An Array of Marks, Per Code.
        {
            "Code":"15CS61",
            "Internal":18, //Integer 
            "External":56, //Integer
            "Total":64, //Integer
            "Result":"Pass",
            "Class":"FCD",
        },
        //Similar Objects as above.
    ],
    "Overall":{
        "Total":560,
        "Result":"Pass",
    } //Only One Object.
}
// More Objects Like the one Above, Based on your request.
]
```
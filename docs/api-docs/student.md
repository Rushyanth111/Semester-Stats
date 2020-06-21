# /student/

Handles all of the **Induvidual** student documentation.


!!! warning "API Subject to changes."
    As a Small warning, all of the below API routes mentioned can be changed at any moment. 

!!! abstract "API Parameters Glossary."

    {student} refers to the USN of a particular student.
    
    {semester} is an integer that referers to a particular semester from 1 to 8.


 
## /student/{student}/summary

This route gets you all of the Summary data that is available 

Example Request:

```
/student/1XM17ME001/summary
```


## /student/{student}/backlogs

This route gets you all of the backlogs for that particular student


```
/student/1XM17ME001/backlog
```

!!! note
    This route may return nothing. 


## /student/{student}/{semester}


```
/student/1XM17ME001/6
```

This route gets the details of that student for a particular semester.

!!! note
    This route may return nothing.
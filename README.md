# Semester Statistics

A project meant to keep an updated record of all scores achieved.

## Database structure

```db
---Student Details
USN <->
Name
Scheme

---Subject Details
Subject Code <->
Subject Name
Subject Semester

---Subject Score
USN <->
SubjectCode <->
Year
Odd/Even
Internals
Externals

---Previous Backlogs + Attempted
Year<->
Odd/Even<->
USN
SubjectCode
Internals
Externals




```

## Additional Notes:

Config Parser.

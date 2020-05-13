
# Calculations

Note that Per-Scheme-Wise-Plguin (Is detailed in [External Calculations](#external-caclulations)) is used to allow for differences in changes over the Years By VTU for final Output.

## Must be Specified On the filename.

Scheme = Given. This must always be specified since the scheme can vary Even in the same Batch.

Semester = Given. While the Application can determine Which Semester for Storage, this is enforced due to Naming Constraints.

Batch = Given. Specified Within the filename.

## Calculations Done To Be Placed into the Database.

- Year = Batch Year + Floor(Semester/2)
- OddEven = Semester%2 (If Even, then 0, if Odd, then 1)
- DepartmentCode = Taken From Subject (17CS12)
- DepartmentName = Hard Coded

# External Caclulations

This Section Maintains the Various Calculations Needed for Other Statistics.

## Scheme - 18

```
To be added
```

---

## Scheme - 17

```
To be added
```

---

## Scheme - 15

```
To be added
```

---

## Scheme - 10

Note that Scheme 10 is currently ignored because of the lack of data.

---

# Semester Statistics

Check the [documentation](https://rushyanth111.github.io/Semester-Stats/) for detailed Information.

This is a project designed to give all the required details of a given VTU-College.

## Assumptions:

These are some of the assumptions I will work with. They are not Subject to change much in the future. I may add some more Assumptions at a later date, but the current core assumptions will remain the same, Nothing will change, only added to.

- 2015 (CBCS) Onward Only. Anything before 2015 is automatically treated as Invalid.
  - While the database will accept the USN, note that undefined Behaviour might occur if wrong usns are Provided.
- Subject Details are Provided. This is Publically Provided. (Credits, (Minimum and Maximum) Internal Marks, etc) By the User of this API.
- Any Score Pertaining to a Subject not in the Database will be **_REJECTED_**.
- Any Score Pertaining to a Student not in the Database will be **_REJECTED_**
- Any Department Pertaining to a Score **OR** Student not in the Database will be **_REJECTED_**
- Any Student **OR** Subject Pertaining not pertaining to a Scheme will be **_REJECTED_**

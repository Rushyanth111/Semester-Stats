interface SubjectReciept {
  Code: string;

  Name: string;

  Semester: number;

  Department: string;

  MinExt: number | null;

  MinTotal: number | null;

  Credits: number | null;
}

export default SubjectReciept;

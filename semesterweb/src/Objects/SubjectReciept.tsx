interface ISubjectReciept {
  Code: string;

  Name: string;

  Semester: number;

  Department: string;

  MinExt: number | null;

  MinTotal: number | null;

  Credits: number | null;
}

class SubjectReciept implements ISubjectReciept {
  Code: string;

  Name: string;

  Semester: number;

  Department: string;

  MinExt: number | null;

  MinTotal: number | null;

  Credits: number | null;

  constructor(obj: ISubjectReciept) {
    this.Code = obj.Code;
    this.Name = obj.Name;
    this.Semester = obj.Semester;
    this.Department = obj.Department;
    this.MinExt = obj.MinExt;
    this.MinTotal = obj.MinTotal;
    this.Credits = obj.Credits;
  }

  getCode(): string {
    return this.Code;
  }

  getName(): string {
    return this.Name;
  }

  getDepartment(): string {
    return this.Department;
  }

  getSemester(): number {
    return this.Semester;
  }

  getMinimumExternalRequired(): number {
    return this.MinExt;
  }

  getMinimalTotalRequired(): number {
    return this.MinTotal;
  }

  getCredits(): number {
    return this.Credits;
  }
}

export { SubjectReciept, ISubjectReciept };

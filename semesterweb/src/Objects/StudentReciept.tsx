interface IStudentReciept {
  Usn: string;

  Name: string;

  Batch: number;

  Department: string;
}

class StudentReciept implements IStudentReciept {
  Usn: string;

  Name: string;

  Batch: number;

  Department: string;

  constructor(obj: IStudentReciept) {
    this.Usn = obj.Usn;
    this.Name = obj.Name;
    this.Batch = obj.Batch;
    this.Department = obj.Department;
  }

  getUsn(): string {
    return this.Usn;
  }

  getName(): string {
    return this.Name;
  }

  getBatch(): number {
    return this.Batch;
  }

  getDepartment(): string {
    return this.Department;
  }
}

export { IStudentReciept, StudentReciept };

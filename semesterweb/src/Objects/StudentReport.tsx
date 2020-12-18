import Report from "./Report";

interface IStudentReport {
  Usn: string;

  Name: string;
}

class StudentReport implements IStudentReport, Report<IStudentReport> {
  Usn: string;

  Name: string;

  constructor(usn: string, name: string) {
    this.Usn = usn;
    this.Name = name;
  }

  toObj(): IStudentReport {
    return {
      Usn: this.Usn,
      Name: this.Name,
    };
  }
}

export { IStudentReport, StudentReport };

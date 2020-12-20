import Report from "./Report";

interface IDepartmentReport {
  Code: string;
  Name: string;
}

class DepartmentReport implements Report<IDepartmentReport> {
  Code: string;

  Name: string;

  constructor(code: string, name: string) {
    this.Code = code;
    this.Name = name;
  }

  toObj(): IDepartmentReport {
    return {
      Code: this.Code,
      Name: this.Name,
    };
  }
}

export { IDepartmentReport, DepartmentReport };

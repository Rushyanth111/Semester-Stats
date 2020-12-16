interface IDepartmentReciept {
  Code: string;

  Name: string;
}

class DepartmentReciept implements IDepartmentReciept {
  Code: string;

  Name: string;

  constructor(obj: IDepartmentReciept) {
    this.Code = obj.Code;
    this.Name = obj.Name;
  }

  getCode(): string {
    return this.Code;
  }

  getName(): string {
    return this.Name;
  }
}

export { IDepartmentReciept, DepartmentReciept };

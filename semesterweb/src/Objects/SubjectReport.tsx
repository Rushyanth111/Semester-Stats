import Report from "./Report";

interface ISubjectReport {
  Code: string;
  Name: string;
  MinExt: number;
  MinTotal: number;
  MaxTotal: number;
  Credits: number;
}

class SubjectReports implements Report<ISubjectReport> {
  Code: string;

  Name: string;

  MinExt = 21;

  MinTotal = 40;

  MaxTotal = 100;

  Credits = 4;

  constructor(
    code: string,
    name: string,
    minExt: number = null,
    minTotal: number = null,
    maxTotal: number = null,
    credits: number = null
  ) {
    this.Code = code;
    this.Name = name;

    if (minExt) {
      this.MinExt = minExt;
    }

    if (minTotal) {
      this.MinTotal = minTotal;
    }
    if (maxTotal) {
      this.MaxTotal = maxTotal;
    }
    if (credits) {
      this.Credits = credits;
    }
  }

  toObj(): ISubjectReport {
    const Obj: ISubjectReport = {
      Code: this.Code,
      Name: this.Name,
      MinExt: this.MinExt,
      MinTotal: this.MinTotal,
      MaxTotal: this.MaxTotal,
      Credits: this.Credits,
    };

    return Obj;
  }
}

export { ISubjectReport, SubjectReports };

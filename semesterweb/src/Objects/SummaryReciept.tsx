import {
  ISubjectSummaryReciept,
  SubjectSummaryReciept,
} from "./SubjectSummaryReciept";

interface ISummaryReciept {
  Appeared: number;

  Failed: number;

  Fcd: number;

  Fc: number;

  Sc: number;

  PassPercent: number;

  Pass: number;

  Subjects: Map<string, ISubjectSummaryReciept>;
}

class SummaryReciept implements ISummaryReciept {
  Appeared: number;

  Failed: number;

  Fcd: number;

  Fc: number;

  Sc: number;

  PassPercent: number;

  Pass: number;

  Subjects: Map<string, SubjectSummaryReciept>;

  constructor(obj: ISummaryReciept) {
    this.Appeared = obj.Appeared;
    this.Failed = obj.Failed;
    this.Fcd = obj.Fcd;
    this.Fc = obj.Fc;
    this.Sc = obj.Sc;
    this.PassPercent = obj.PassPercent;
    this.Pass = obj.Pass;
    // this.Subjects
    obj.Subjects.forEach((val: ISubjectSummaryReciept, key: string) => {
      this.Subjects[key] = new SubjectSummaryReciept(val);
    });
  }

  getAppeared(): number {
    return this.Appeared;
  }

  getFailed(): number {
    return this.Failed;
  }

  getFirstClassDistinction(): number {
    return this.Fcd;
  }

  getFirstClass(): number {
    return this.Fc;
  }

  getSecondClass(): number {
    return this.Sc;
  }

  getPassPercent(): number {
    return this.PassPercent;
  }

  getPass(): number {
    return this.Pass;
  }
}

export { ISummaryReciept, SummaryReciept };

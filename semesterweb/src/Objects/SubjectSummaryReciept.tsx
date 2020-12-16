interface ISubjectSummaryReciept {
  Appeared: number;

  Failed: number;

  Fcd: number;

  Fc: number;

  Sc: number;

  PassPercent: number;

  Pass: number;
}

class SubjectSummaryReciept implements ISubjectSummaryReciept {
  Appeared: number;

  Failed: number;

  Fcd: number;

  Fc: number;

  Sc: number;

  PassPercent: number;

  Pass: number;

  constructor(obj: ISubjectSummaryReciept) {
    this.Appeared = obj.Appeared;
    this.Failed = obj.Failed;
    this.Fcd = obj.Fcd;
    this.Fc = obj.Fc;
    this.Sc = obj.Sc;
    this.PassPercent = obj.PassPercent;
    this.Pass = obj.Pass;
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

export { SubjectSummaryReciept, ISubjectSummaryReciept };

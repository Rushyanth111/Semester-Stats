interface IScoreReciept {
  Usn: string;

  SubjectCode: string;

  Internals: number;

  Externals: number;
}

class ScoreReciept implements IScoreReciept {
  Usn: string;

  SubjectCode: string;

  Internals: number;

  Externals: number;

  constructor(obj: IScoreReciept) {
    this.Usn = obj.Usn;
    this.SubjectCode = obj.SubjectCode;
    this.Internals = obj.Internals;
    this.Externals = obj.Externals;
  }

  getUsn(): string {
    return this.Usn;
  }

  getSubjectCode(): string {
    return this.SubjectCode;
  }

  getInternals(): number {
    return this.Internals;
  }

  getExternals(): number {
    return this.Externals;
  }

  getTotal(): number {
    return this.Internals + this.Externals;
  }
}

export { IScoreReciept, ScoreReciept };

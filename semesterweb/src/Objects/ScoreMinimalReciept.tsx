interface IScoreMinimalReciept {
  SubjectCode: string;

  Internals: number;

  Externals: number;
}

class ScoreMinimalReciept implements IScoreMinimalReciept {
  SubjectCode: string;

  Internals: number;

  Externals: number;

  constructor(obj: IScoreMinimalReciept) {
    this.SubjectCode = obj.SubjectCode;
    this.Internals = obj.Internals;
    this.Externals = obj.Externals;
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

export { IScoreMinimalReciept, ScoreMinimalReciept };

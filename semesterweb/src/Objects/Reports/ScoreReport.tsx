import Report from "./Report";
import { IScoreReciept } from "./ScoreReciept";

interface IScoreReport {
  Usn: string;
  SubjectCode: string;
  Internals: number;
  Externals: number;
}

class ScoreReport implements Report<IScoreReport> {
  Usn: string;

  SubjectCode: string;

  Internals: number;

  Externals: number;

  constructor(
    usn: string,
    subCode: string,
    internals: number,
    externals: number
  ) {
    this.Usn = usn;
    this.SubjectCode = subCode;
    this.Internals = internals;
    this.Externals = externals;
  }

  toObj(): IScoreReciept {
    return {
      Usn: this.Usn,
      SubjectCode: this.SubjectCode,
      Internals: this.Internals,
      Externals: this.Externals,
    };
  }
}

export { ScoreReport, IScoreReport };

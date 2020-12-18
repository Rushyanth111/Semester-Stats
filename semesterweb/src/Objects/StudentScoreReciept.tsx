import {
  IScoreMinimalReciept,
  ScoreMinimalReciept,
} from "./ScoreMinimalReciept";

interface IStudentScoreReciept {
  Usn: string;

  Name: string;

  Batch: number;

  Department: string;

  Scores: Array<IScoreMinimalReciept>;
}

class StudentScoreReciept implements IStudentScoreReciept {
  Usn: string;

  Name: string;

  Batch: number;

  Department: string;

  Scores: Array<ScoreMinimalReciept>;

  constructor(obj: IStudentScoreReciept) {
    this.Usn = obj.Usn;
    this.Name = obj.Name;
    this.Batch = obj.Batch;
    this.Department = obj.Department;
    this.Scores = obj.Scores.map(
      (ele: IScoreMinimalReciept) => new ScoreMinimalReciept(ele)
    );
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

  getScores(): Array<ScoreMinimalReciept> {
    return this.Scores;
  }
}

export { StudentScoreReciept, IStudentScoreReciept };

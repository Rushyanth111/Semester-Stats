import ScoreMinimalReciept from "./ScoreMinimalReciept";

interface StudentScoreReciept {
  Usn: string;

  Name: string;

  Batch: number;

  Department: string;

  Scores: Array<ScoreMinimalReciept>;
}

export default StudentScoreReciept;

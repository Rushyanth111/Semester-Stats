import { DepartmentReciept } from "./DepartmentReciept";
import { ScoreMinimalReciept } from "./ScoreMinimalReciept";
import { ScoreReciept } from "./ScoreReciept";
import { StudentReciept } from "./StudentReciept";
import { StudentScoreReciept } from "./StudentScoreReciept";
import { SubjectReciept } from "./SubjectReciept";
import { SubjectSummaryReciept } from "./SubjectSummaryReciept";
import { SummaryReciept } from "./SummaryReciept";

type Receipt =
  | DepartmentReciept
  | ScoreMinimalReciept
  | ScoreReciept
  | StudentReciept
  | StudentScoreReciept
  | SubjectReciept
  | SubjectSummaryReciept
  | SummaryReciept;

export default Receipt;

import SubjectSummaryReciept from "./SubjectSummaryReciept";

interface SummaryReciept {
  Appeared: number;

  Failed: number;

  Fcd: number;

  Fc: number;

  Sc: number;

  PassPercent: number;

  Pass: number;

  Subjects: Record<string, SubjectSummaryReciept>;
}

export default SummaryReciept;

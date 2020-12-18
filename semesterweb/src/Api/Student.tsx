import { get } from "./Common";

import { IScoreReciept } from "../Objects/ScoreReciept";
import { IStudentReciept } from "../Objects/StudentReciept";

async function getStudent(usn: string): Promise<IStudentReciept> {
  return get<IStudentReciept>(`${process.env.APIROOTPATH}/student/${usn}`);
}

async function getStudentScores(
  usn: string,
  sem: number
): Promise<IScoreReciept> {
  return get<IScoreReciept>(
    `${process.env.APIROOTPATH}/student/${usn}/scores`,
    { sem }
  );
}

async function getStudentBacklogs(
  usn: string,
  sem: number
): Promise<Array<IScoreReciept>> {
  return get<Array<IScoreReciept>>(
    `${process.env.APIROOTPATH}/student/${usn}/backlogs`,
    { sem }
  );
}

async function getStudentSubject(
  usn: string,
  subCode: string
): Promise<IScoreReciept> {
  return get<IScoreReciept>(
    `${process.env.APIROOTPATH}/student/${usn}/subject/${subCode}`
  );
}

export { getStudent, getStudentScores, getStudentBacklogs, getStudentSubject };

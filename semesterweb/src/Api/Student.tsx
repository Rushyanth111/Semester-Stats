import { get } from "./Common";

import { IScoreReciept, ScoreReciept } from "../Objects/ScoreReciept";
import { IStudentReciept, StudentReciept } from "../Objects/StudentReciept";

async function getStudent(usn: string): Promise<StudentReciept | null> {
  try {
    const response = await get<IStudentReciept>(
      `${process.env.APIROOTPATH}/student/${usn}`
    );
    const data = new StudentReciept(response.data);
    return data;
  } catch (error) {
    console.log(error);
    return null;
  }
}

async function getStudentScores(
  usn: string,
  sem?: number
): Promise<Array<ScoreReciept>> {
  try {
    const response = await get<Array<IScoreReciept> | null>(
      `${process.env.APIROOTPATH}/student/${usn}/scores`,
      { sem }
    );

    const data = Array.from(
      response.data,
      (val: IScoreReciept) => new ScoreReciept(val)
    );
    return data;
  } catch (error) {
    console.log(error);
    return null;
  }
}

async function getStudentBacklogs(
  usn: string,
  sem?: number
): Promise<Array<ScoreReciept>> {
  try {
    const response = await get<Array<IScoreReciept>>(
      `${process.env.APIROOTPATH}/student/${usn}/backlogs`,
      { sem }
    );

    const data = Array.from(response.data, (val) => {
      return new ScoreReciept(val);
    });

    return data;
  } catch (error) {
    console.log(error);
    return null;
  }
}

async function getStudentSubject(
  usn: string,
  subCode: string
): Promise<ScoreReciept> {
  try {
    const response = await get<IScoreReciept>(
      `${process.env.APIROOTPATH}/student/${usn}/subject/${subCode}`
    );
    const data = new ScoreReciept(response.data);
    return data;
  } catch (error) {
    console.log(error);
    return null;
  }
}

export { getStudent, getStudentScores, getStudentBacklogs, getStudentSubject };

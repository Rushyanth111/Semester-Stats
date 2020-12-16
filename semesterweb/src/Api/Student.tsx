import axios from "axios";
import { IScoreReciept } from "../Objects/ScoreReciept";
import { IStudentReciept, StudentReciept } from "../Objects/StudentReciept";

async function getStudent(usn: string): Promise<null | IStudentReciept> {
  try {
    const response = await axios.get(`/api/student/${usn}`);
    const data: IStudentReciept = new StudentReciept(await response.data);
    return data;
  } catch (e) {
    // Guessing this is a 404 or something else.
    console.log(e);
    return null;
  }
}

async function getStudentScores(
  usn: string
): Promise<null | Array<IScoreReciept>> {
  try {
    const response = await axios.get(`/api/student/${usn}/scores`);
    const data: Array<IScoreReciept> = await response.data;
    return data;
  } catch (e) {
    console.log(e);
    // Guessing this is a 404 or something else.
    return null;
  }
}

async function getStudentBacklogs(
  usn: string
): Promise<null | Array<IScoreReciept>> {
  try {
    const response = await axios.get(`/api/student/${usn}/scores/backlogs`);
    const data: Array<IScoreReciept> = await response.data;
    return data;
  } catch (e) {
    // Guessing this is a 404 or something else.
    return null;
  }
}

async function getStudentSubject(
  usn: string,
  subject: string
): Promise<null | IScoreReciept> {
  try {
    const response = await axios.get(`/api/student/${usn}/subject/${subject}`);
    const data: IScoreReciept = await response.data;
    return data;
  } catch (e) {
    // Guessing this is a 404 or something else.
    return null;
  }
}

export { getStudent, getStudentScores, getStudentBacklogs, getStudentSubject };

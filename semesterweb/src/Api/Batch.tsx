import axios from "axios";
import IStudentScoreReciept from "../Objects/StudentScoreReciept";

async function getBatch(): Promise<null | Array<number>> {
  try {
    const response = await axios.get("/api/batch");
    const data: Array<number> = await response.data;
    return data;
  } catch (e) {
    console.log(e);
    return null;
  }
}

async function getBatchScores(
  batch: number
): Promise<null | IStudentScoreReciept> {
  try {
    const response = await axios.get(`/api/batch/${batch}/scores`);
    const data: IStudentScoreReciept = await response.data;
    return data;
  } catch (e) {
    console.log(e);
    return null;
  }
}

async function getBatchBacklogs(
  batch: number
): Promise<null | IStudentScoreReciept> {
  try {
    const resposne = await axios.get(`/api/batch/${batch}/backlogs`);
    const data: IStudentScoreReciept = await resposne.data;
    return data;
  } catch (e) {
    console.log(e);
    return null;
  }
}

async function getBatchDetained(
  batch: number
): Promise<null | IStudentScoreReciept> {
  try {
    const response = await axios.get(`/api/batch/${batch}/detained`);
    const data: IStudentScoreReciept = await response.data;
    return data;
  } catch (e) {
    console.log(e);
    return null;
  }
}

async function getBatchAggregate(
  batch: number
): Promise<null | IStudentScoreReciept> {
  try {
    const response = await axios.get(`/api/batch/${batch}/aggregate`);
    const data: IStudentScoreReciept = await response.data;
    return data;
  } catch (e) {
    console.log(e);
    return null;
  }
}

export {
  getBatch,
  getBatchScores,
  getBatchBacklogs,
  getBatchDetained,
  getBatchAggregate,
};

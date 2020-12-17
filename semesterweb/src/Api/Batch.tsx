import axios from "axios";
import { IScoreMinimalReciept } from "../Objects/StudentScoreReciept";

async function getBatch(): Promise<null | Array<number>> {
  try {
    const response = await axios.get(`${process.env.APIROOTPATH}/batch`);
    const data: Array<number> = await response.data;
    return data;
  } catch (e) {
    console.log(e);
    return null;
  }
}

async function getBatchScores(
  batch: number
): Promise<null | IScoreMinimalReciept> {
  try {
    const response = await axios.get(
      `${process.env.APIROOTPATH}/batch/${batch}/scores`
    );
    const data: IScoreMinimalReciept = await response.data;
    return data;
  } catch (e) {
    console.log(e);
    return null;
  }
}

async function getBatchBacklogs(
  batch: number
): Promise<null | IScoreMinimalReciept> {
  try {
    const resposne = await axios.get(
      `${process.env.APIROOTPATH}/batch/${batch}/backlogs`
    );
    const data: IScoreMinimalReciept = await resposne.data;
    return data;
  } catch (e) {
    console.log(e);
    return null;
  }
}

async function getBatchDetained(
  batch: number
): Promise<null | IScoreMinimalReciept> {
  try {
    const response = await axios.get(
      `${process.env.APIROOTPATH}/batch/${batch}/detained`
    );
    const data: IScoreMinimalReciept = await response.data;
    return data;
  } catch (e) {
    console.log(e);
    return null;
  }
}

async function getBatchAggregate(
  batch: number
): Promise<null | IScoreMinimalReciept> {
  try {
    const response = await axios.get(
      `${process.env.APIROOTPATH}/batch/${batch}/aggregate`
    );
    const data: IScoreMinimalReciept = await response.data;
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

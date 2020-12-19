import {
  IStudentScoreReciept,
  StudentScoreReciept,
} from "../Objects/StudentScoreReciept";
import { get } from "./Common";

async function getBatch(): Promise<Array<number> | null> {
  try {
    const response = await get<Array<number>>(
      `${process.env.APIROOTPATH}/batch`
    );
    const data = Array.from(response.data);
    return data;
  } catch (error) {
    console.log(error);
    return null;
  }
}

async function getBatchScores(
  batch: number,
  dept?: string,
  sem?: number
): Promise<Array<IStudentScoreReciept> | null> {
  try {
    const response = await get<Array<IStudentScoreReciept>>(
      `${process.env.APIROOTPATH}/batch/${batch}/scores`,
      { dept, sem }
    );
    const data = Array.from(response.data, (val) => {
      return new StudentScoreReciept(val);
    });

    return data;
  } catch (error) {
    console.log(error);
    return null;
  }
}

async function getBatchBacklogs(
  batch: number,
  dept?: string
): Promise<Array<IStudentScoreReciept> | null> {
  try {
    const response = await get<Array<IStudentScoreReciept>>(
      `${process.env.APIROOTPATH}/batch/${batch}/backlogs`,
      { dept }
    );
    const data = Array.from(
      response.data,
      (val) => new StudentScoreReciept(val)
    );
    return data;
  } catch (error) {
    console.log(error);
    return null;
  }
}

async function getBatchDetained(
  batch: number,
  dept?: string,
  sem?: number
): Promise<Array<IStudentScoreReciept> | null> {
  try {
    const response = await get<Array<IStudentScoreReciept>>(
      `${process.env.APIROOTPATH}/batch/${batch}/detained`,
      { dept, sem }
    );
    const data = Array.from(
      response.data,
      (val) => new StudentScoreReciept(val)
    );
    return data;
  } catch (error) {
    console.log(error);
    return null;
  }
}

async function getBatchAggregate(
  batch: number,
  dept?: string
): Promise<Map<string, number>> {
  try {
    const response = await get<Map<string, number>>(
      `${process.env.APIROOTPATH}/batch/${batch}/aggregate`,
      { dept }
    );
    const data = new Map(response.data.entries());
    return data;
  } catch (error) {
    console.log(error);
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

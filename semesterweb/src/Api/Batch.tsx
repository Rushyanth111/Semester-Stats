import { IStudentScoreReciept } from "../Objects/StudentScoreReciept";
import { get } from "./Common";

async function getBatch(): Promise<Array<number>> {
  return get<Array<number>>(`${process.env.APIROOTPATH}/batch`);
}

async function getBatchScores(
  batch: number,
  dept?: string,
  sem?: number
): Promise<Array<IStudentScoreReciept>> {
  return get<Array<IStudentScoreReciept>>(
    `${process.env.APIROOTPATH}/batch/${batch}/scores`,
    { dept, sem }
  );
}

async function getBatchBacklogs(
  batch: number,
  dept?: string
): Promise<Array<IStudentScoreReciept>> {
  return get<Array<IStudentScoreReciept>>(
    `${process.env.APIROOTPATH}/batch/${batch}/backlogs`,
    { dept }
  );
}

async function getBatchDetained(
  batch: number,
  dept?: string,
  sem?: number
): Promise<Array<IStudentScoreReciept>> {
  return get<Array<IStudentScoreReciept>>(
    `${process.env.APIROOTPATH}/batch/${batch}/detained`,
    { dept, sem }
  );
}

async function getBatchAggregate(
  batch: number,
  dept?: string
): Promise<Map<string, number>> {
  return get<Map<string, number>>(
    `${process.env.APIROOTPATH}/batch/${batch}/aggregate`,
    { dept }
  );
}

export {
  getBatch,
  getBatchScores,
  getBatchBacklogs,
  getBatchDetained,
  getBatchAggregate,
};

import { IStudentScoreReciept } from "../Objects/StudentScoreReciept";
import { get } from "./Common";

async function getBatch(): Promise<Array<number>> {
  return get<Array<number>>(`${process.env.APIROOTPATH}/batch`);
}

async function getBatchScores(
  batch: number
): Promise<Array<IStudentScoreReciept>> {
  return get<Array<IStudentScoreReciept>>(
    `${process.env.APIROOTPATH}/batch/${batch}/scores`
  );
}

async function getBatchBacklogs(
  batch: number
): Promise<Array<IStudentScoreReciept>> {
  return get<Array<IStudentScoreReciept>>(
    `${process.env.APIROOTPATH}/batch/${batch}/backlogs`
  );
}

async function getBatchDetained(
  batch: number
): Promise<Array<IStudentScoreReciept>> {
  return get<Array<IStudentScoreReciept>>(
    `${process.env.APIROOTPATH}/batch/${batch}/detained`
  );
}

async function getBatchAggregate(batch: number): Promise<Map<string, number>> {
  return get<Map<string, number>>(
    `${process.env.APIROOTPATH}/batch/${batch}/aggregate`
  );
}

export {
  getBatch,
  getBatchScores,
  getBatchBacklogs,
  getBatchDetained,
  getBatchAggregate,
};

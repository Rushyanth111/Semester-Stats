import { ISubjectReciept } from "../Objects/SubjectReciept";
import { get } from "./Common";

async function getSubject(subCode: string): Promise<ISubjectReciept> {
  return get<ISubjectReciept>(`${process.env.APIROOTPATH}/subject/${subCode}`);
}

export default { getSubject };

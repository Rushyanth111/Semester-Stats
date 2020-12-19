import { ISubjectReciept, SubjectReciept } from "../Objects/SubjectReciept";
import { get } from "./Common";

async function getSubject(subCode: string): Promise<ISubjectReciept> {
  try {
    const response = await get<ISubjectReciept>(
      `${process.env.APIROOTPATH}/subject/${subCode}`
    );
    const data = new SubjectReciept(response.data);
    return data;
  } catch (error) {
    console.log(error);
    return null;
  }
}

export default { getSubject };

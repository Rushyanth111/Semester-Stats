import axios from "axios";
import { ISubjectReciept } from "../Objects/SubjectReciept";

async function getSubject(): Promise<null | ISubjectReciept> {
  try {
    const response = await axios.get("/api/SubjectReciept");
    const data: ISubjectReciept = await response.data;
    return data;
  } catch (e) {
    console.log(e);
    return null;
  }
}

export default { getSubject };

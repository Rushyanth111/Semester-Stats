import axios from "axios";
import { IDepartmentReciept } from "../Objects/DepartmentReciept";

async function getDepartment(dept: string): Promise<null | IDepartmentReciept> {
  try {
    const response = await axios.get(`/api/dept/${dept}`);
    const data: IDepartmentReciept = await response.data;
    return data;
  } catch (e) {
    return null;
  }
}

async function getAllDepartment(): Promise<null | Array<string>> {
  try {
    const response = await axios.get(`/api/dept`);
    const data: Array<string> = await response.data;
    return data;
  } catch (e) {
    return null;
  }
}

export { getDepartment, getAllDepartment };

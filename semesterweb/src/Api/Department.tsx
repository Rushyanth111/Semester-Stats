import {
  DepartmentReciept,
  IDepartmentReciept,
} from "../Objects/DepartmentReciept";
import { get } from "./Common";

async function getDepartment(dept: string): Promise<IDepartmentReciept> {
  try {
    const response = await get<IDepartmentReciept>(
      `${process.env.APIROOTPATH}/dept/${dept}`
    );
    const data = new DepartmentReciept(response.data);
    return data;
  } catch (error) {
    console.log(error);
    return null;
  }
}

async function getAllDepartment(): Promise<Array<string>> {
  try {
    const response = await get<Array<string>>(
      `${process.env.APIROOTPATH}/dept`
    );
    const data = Array.from(response.data);
    return data;
  } catch (error) {
    console.log(error);
    return null;
  }
}

export { getDepartment, getAllDepartment };

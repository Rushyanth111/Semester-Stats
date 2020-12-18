import { IDepartmentReciept } from "../Objects/DepartmentReciept";
import { get } from "./Common";

async function getDepartment(dept: string): Promise<IDepartmentReciept> {
  return get<IDepartmentReciept>(`${process.env.APIROOTPATH}/dept/${dept}`);
}

async function getAllDepartment(): Promise<Array<string>> {
  return get<Array<string>>(`${process.env.APIROOTPATH}/dept`);
}

export { getDepartment, getAllDepartment };

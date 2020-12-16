import { IStudentReciept } from "../Objects/StudentReciept";
import { getStudent } from "../Api/Student";

describe("getStudent", () => {
  test("getStudent", async () => {
    const data = await getStudent("1CR17CS001");
    expect(data as IStudentReciept).toBeTruthy();
  }, 1000);

  test("getStudentFail", async () => {
    const data = await getStudent("1CR15CS001");
    expect(data).toBeNull();
  }, 1000);
});

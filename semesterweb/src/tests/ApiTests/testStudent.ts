import { getStudent } from "../../Api/Student";

describe("getStudent Tests", () => {
  test("getStudent Pass", async () => {
    const data = await getStudent("1CR17CS001");
    expect(data).not.toBeNull();
  });
  test("getStudent Fail", async () => {
    const data = await getStudent("1CR15CS001");
    expect(data).toBeNull();
  });
  test("getStudent Fail Bad Input", async () => {
    const data = await getStudent("1CR15CS01");
    expect(data).toBeNull();
  });
});

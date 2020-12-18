import { getStudentBacklogs } from "../Api/Student";
import { getBatch } from "../Api/Batch";

describe("StudentTests", () => {
  test("Backlogs", async () => {
    const data = await getStudentBacklogs("1CR17CS002");
    console.log(data);
  });

  test("Student", async () => {
    const data = await getBatch();
    console.log(data);
  });
});

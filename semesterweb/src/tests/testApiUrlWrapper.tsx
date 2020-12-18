import { urlWrapper } from "../Api/URLWrapper";

describe("URL Wrapper Test", () => {
  test("Wrapper Test All Params", () => {
    const data = urlWrapper("/api", { A: "B", B: 5 });
    expect(data).toBe("/api?A=B&B=5");
  });

  test("Wrapper Several Undefined", () => {
    const data = urlWrapper("/api", {
      A: "B",
      B: "",
      C: null,
      D: undefined,
      E: 0,
    });
    expect(data).toBe("/api?A=B&E=0");
  });

  test("Wrapper No Args", () => {
    const data = urlWrapper("/api", {});
    expect(data).toBe("/api");
  });

  test("Wrapper No Undefined", () => {
    const data = urlWrapper("/api");
    expect(data).toBe("/api");
  });
});

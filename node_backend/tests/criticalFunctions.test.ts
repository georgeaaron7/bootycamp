import { add, multiply } from "../src/criticalFunctions";

describe("add function", () => {
  test("adds two numbers correctly", () => {
    expect(add(2, 3)).toBe(5);
  });
});

describe("multiply function", () => {
  test("multiplies two numbers correctly", () => {
    expect(multiply(2, 3)).toBe(6);
  });
});
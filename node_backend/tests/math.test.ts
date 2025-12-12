import { add, multiply } from '../src/math';

describe('Math functions', () => {
  test('add function should return the sum of two numbers', () => {
    expect(add(2, 3)).toBe(5);
  });

  test('multiply function should return the product of two numbers', () => {
    expect(multiply(2, 3)).toBe(6);
  });
});
const fs = require("fs");
const runner = require("../../utils/runner");

const IN = fs.readFileSync("day10.in", "utf8");

const nums = [0].concat(
  IN.split("\n")
    .map((x) => +x)
    .sort((a, b) => a - b)
);
nums.push(Math.max(...nums) + 3);

const pt1 = (nums) => {
  const differences = nums.slice(1).reduce((acc, curr, idx) => {
    const key = curr - nums[idx];
    acc[key] = acc[key] + 1 || +1;
    return acc;
  }, {});
  return differences["1"] * differences["3"];
};

const cache = {};
function pt2(nums) {
  if (nums.length === 1) return 1;
  const [n, ...rest] = nums;
  if (cache[n]) return cache[n];
  let total = 0;
  for (let i = 0; i < rest.length; i++) {
    const k = rest[i];
    if (k - n <= 3) {
      total += pt2(rest.slice(i));
    }
  }
  cache[n] = total;
  return cache[n];
}

runner(1, pt1, nums);
runner(2, pt2, nums);

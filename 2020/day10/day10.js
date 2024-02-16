const fs = require("fs");

const IN = fs.readFileSync("day10.in", "utf8");

const nums = [0].concat(
  IN.split("\n")
    .map((x) => +x)
    .sort((a, b) => a - b)
);
nums.push(Math.max(...nums) + 3);

const differences = nums.slice(1).reduce((acc, curr, idx) => {
  const key = curr - nums[idx];
  acc[key] = acc[key] + 1 || +1;
  return acc;
}, {});

console.log(differences["1"] * differences["3"]);

const cache = {};
function solve(nums) {
  if (nums.length === 1) return 1;
  const [n, ...rest] = nums;
  if (cache[n]) return cache[n];
  let total = 0;
  for (let i = 0; i < rest.length; i++) {
    const k = rest[i];
    if (k - n <= 3) {
      total += solve(rest.slice(i));
    }
  }
  cache[n] = total;
  return cache[n];
}

console.log(solve(nums));

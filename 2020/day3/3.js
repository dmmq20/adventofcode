const fs = require("fs");
const runner = require("../../utils/runner");

const IN = fs.readFileSync("3.in", "utf8");

const trees = IN.trim()
  .split("\n")
  .map((line) => line.split(""));

function solve(row, col) {
  let [dr, dc] = [row, col];
  let ans = 0;
  while (dr < trees.length) {
    if (trees[dr][dc] === "#") {
      ans++;
    }
    dr += row;
    dc = (dc + col) % trees[0].length;
  }
  return ans;
}

const slopes = [
  [1, 1],
  [1, 3],
  [1, 5],
  [1, 7],
  [2, 1],
];

const pt2 = (slopes) => slopes.reduce((acc, curr) => acc * solve(...curr), 1);

runner(1, solve, 1, 3);
runner(2, pt2, slopes);

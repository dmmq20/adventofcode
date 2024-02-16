const fs = require("fs");

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
console.log(solve(1, 3));
const slopes = [
  [1, 1],
  [1, 3],
  [1, 5],
  [1, 7],
  [2, 1],
];

console.log(slopes.reduce((acc, curr) => acc * solve(...curr), 1));

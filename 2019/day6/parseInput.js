const fs = require("fs");
const IN = fs.readFileSync("6.in", "utf8");

function parseInput(pt2 = false) {
  return IN.trim()
    .split("\n")
    .reduce((acc, curr) => {
      const [a, b] = curr.split(")");
      acc[a] ? acc[a].push(b) : (acc[a] = [b]);
      if (pt2) {
        acc[b] ? acc[b].push(a) : (acc[b] = [a]);
      }
      return acc;
    }, {});
}

module.exports = parseInput;

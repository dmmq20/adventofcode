const parseInput = require("./parseInput");

function solve(start, end) {
  if (start === end) return 0;
  visited.add(start);
  let minDist = Infinity;
  for (const nbr of graph[start]) {
    if (!visited.has(nbr)) {
      const dist = solve(nbr, end) + 1;
      minDist = Math.min(minDist, dist);
    }
  }
  return minDist;
}

// equivalent
// function solve(start, end) {
//   if (start === end) return 0;
//   visited.add(start);
//   return Math.min(
//     ...graph[start].filter((n) => !visited.has(n)).map((n) => solve(n, end) + 1)
//   );
// }

const visited = new Set();
const graph = parseInput(true);
console.log(solve("YOU", "SAN") - 2);

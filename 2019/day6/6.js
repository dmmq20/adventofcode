const fs = require("fs");

const IN = fs.readFileSync("6.in", "utf8");

const graph = IN.trim()
  .split("\n")
  .reduce((acc, curr) => {
    const [a, b] = curr.split(")");
    acc[a] ? acc[a].push(b) : (acc[a] = [b]);
    acc[b] ? acc[b].push(a) : (acc[b] = [a]);
    return acc;
  }, {});

function dfs(start, end) {
  const Q = [[start, 0]];
  const visited = new Set();
  let minDist = Infinity;

  while (Q.length > 0) {
    const [node, dist] = Q.pop();
    if (node === end) {
      minDist = Math.min(minDist, dist);
    }
    visited.add(node);
    graph[node].forEach((nbr) => {
      if (!visited.has(nbr)) {
        Q.push([nbr, dist + 1]);
      }
    });
  }

  return minDist - 2;
}

console.log(dfs("YOU", "SAN"));

// const visited = new Set();

// function solve(start, end) {
//   if (start === end) return 0;
//   visited.add(start);
//   let minDist = Infinity;
//   for (const nbr of graph[start]) {
//     if (!visited.has(nbr)) {
//       const dist = solve(nbr, end) + 1;
//       minDist = Math.min(minDist, dist);
//     }
//   }
//   return minDist;
// }

// console.log(solve("YOU", "SAN") - 2);

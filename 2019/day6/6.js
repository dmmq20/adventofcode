const runner = require("../../utils/runner");
const parseInput = require("./parseInput");

function pt1(node, graph) {
  if (!graph[node]) return 0;
  return graph[node].reduce((acc, curr) => acc + pt1(curr, graph) + 1, 0);
}

function dfs(start, end, graph) {
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

const G = parseInput();
const nodes = Object.keys(G);
const helper = (nodes) => nodes.reduce((acc, node) => acc + pt1(node, G), 0);
runner(1, helper, nodes);
runner(2, dfs, "YOU", "SAN", parseInput(true));

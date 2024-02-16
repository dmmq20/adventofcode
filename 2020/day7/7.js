const fs = require("fs");

const IN = fs.readFileSync("7.in", "utf8");
const re = /(\d? ?\w+ \w+(?= bag))/gi;

const bags = IN.trim()
  .split("\n")
  .reduce((acc, line) => {
    const [outer, ...inner] = line.match(re);
    inner.forEach((bag) => {
      if (bag !== " no other") {
        const [_, n, colour] = bag.match(/(\d+)\s+(\w+\s+\w+)$/);
        if (acc[outer]) {
          acc[outer].push([Number(n), colour]);
        } else {
          acc[outer] = [[Number(n), colour]];
        }
      }
    });
    return acc;
  }, {});

function solve1(bag) {
  if (bags[bag] === undefined) return false;
  if (bag === "shiny gold") return true;
  return bags[bag].some(([_, innerBag]) => solve1(innerBag));
}

function solve2(bag = "shiny gold") {
  if (bags[bag] === undefined) return 0;
  return bags[bag].reduce((acc, [n, bag]) => acc + n + n * solve2(bag), 0);
}

console.log(Object.keys(bags).filter((b) => solve1(b)).length - 1);
console.log(solve2());

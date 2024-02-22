const fs = require("fs");
const runner = require("../../utils/runner");

const IN = fs.readFileSync("21.in", "utf8");

const ingredients = {};
function pt1() {
  const pt1 = [];
  IN.split("\n").forEach((line) => {
    let [items, allergens] = line.split(" (contains ");
    items = items.split(" ");
    pt1.push(items);
    allergens = allergens.slice(0, -1).split(", ");
    allergens.forEach((allgn) => {
      const fltrd = items.filter((itm) =>
        ingredients[allgn] ? ingredients[allgn].has(itm) : true
      );
      ingredients[allgn] = new Set(fltrd);
    });
  });

  const done = new Set();
  while (Object.values(ingredients).some((s) => s.size > 1)) {
    for (const [k, v] of Object.entries(ingredients)) {
      if (v.size === 1 && !done.has(k)) {
        const [ingrdnt] = v.values();
        for (const [K, V] of Object.entries(ingredients)) {
          if (V.size > 1 && K !== k) {
            V.delete(ingrdnt);
          }
        }
        done.add(k);
      }
    }
  }

  const foundAllergens = Object.values(ingredients).reduce(
    (acc, curr) => acc.concat(Array.from(curr)),
    []
  );

  const ans = pt1.reduce(
    (acc, curr) => acc + curr.filter((i) => !foundAllergens.includes(i)).length,
    0
  );
  return ans;
}

function pt2() {
  const sorted = Object.keys(ingredients)
    .sort()
    .map((item) => Array.from(ingredients[item])[0]);
  return sorted.join(",");
}

runner(1, pt1);
runner(2, pt2);

async function runner(part, fn, ...args) {
  const t1 = Date.now();
  const ans = await fn(...args);
  const t2 = Date.now();
  console.log(`Part ${part}: ${ans} --- ${(t2 - t1) / 1000}ms`);
}

module.exports = runner;

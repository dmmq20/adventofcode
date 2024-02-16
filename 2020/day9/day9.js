const fs = require("fs")

const IN = fs.readFileSync("day9.in", "utf8")
const preamble = IN.trim().split("\n").map(n => +n)
const nums = preamble.slice(25)

const ans = nums.find((n, idx) => {
    const prev = preamble.slice(idx, idx+25)
    return !prev.some(k => prev.includes(n-k) && k !== n-k)
})
console.log(ans)

let [start, end, sum] = [0, 0, 0]
while (end < nums.length) {
    if (sum == ans) {
        const pt2 = nums.slice(start, end)
        console.log(Math.min(...pt2) + Math.max(...pt2))
        break
    }
    if (sum > ans) {
        sum -= nums[start]
        start++
        continue
    }
    sum += nums[end]
    end++
}

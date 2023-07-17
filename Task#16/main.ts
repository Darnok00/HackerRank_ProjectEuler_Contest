/*
Task #16
Power digit sum
Level: Easy
Points: 100
*/

const N: number = 10000;

function doubleNumber(arr: number[]) {
  let new_arr: number[] = [];
  let rest: number = 0;

  arr.forEach((digit) => {
    const act_val: number = digit * 2 + rest;
    new_arr.push(act_val % 10);
    rest = Math.floor(act_val / 10);
  });

  if (rest !== 0) {
    new_arr.push(rest);
  }

  return new_arr;
}

function createDictSums(n: number) {
  let dict: { [index: number]: number } = {};
  let arr = [1];

  for (let i = 1; i <= n; i++) {
    arr = doubleNumber(arr);
    dict[i] = arr.reduce((a, b) => a + b, 0);
  }

  return dict;
}

function processInput(input: string) {
  const lines = input.trim().split('\n');
  const t: number = Number(lines[0]);
  const dictSums = createDictSums(N);

  for (let i = 0; i < t; i++) {
    const n = Number(lines[i + 1]);
    console.log(dictSums[n]);
  }
}

function main() {
  let input = '';

  process.stdin.on('data', (data) => {
    input += data.toString();

    const lines = input.trim().split('\n');
    const t: number = Number(lines[0]);

    if (lines.length - 1 === t) {
      processInput(input);
      process.stdin.end();
    }
  });

}

main();

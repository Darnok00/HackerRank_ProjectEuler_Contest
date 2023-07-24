/*
Task #18
Maximum Path Sum I
Level: Easy
Points: 100
*/

export{}

process.stdin.resume();
process.stdin.setEncoding('utf-8');
let inputString: string = '';
let inputLines: string[] = [];
let currentLine: number = 0;

process.stdin.on('data', function (inputStdin: string): void {
  inputString += inputStdin;
});

process.stdin.on('end', function (): void {
  inputLines = inputString.split('\n');
  inputString = '';
  main();
});

function readLine(): string {
  return inputLines[currentLine++];
}

function findMax(arr: number[][], step: number, actualSum: number, actualIndex: number): number {
  if (step === (arr.length - 1)) {
    return actualSum;
  }
  const valueLeft = findMax(arr, step + 1, actualSum + arr[step + 1][actualIndex], actualIndex);
  const valueRight = findMax(arr, step + 1, actualSum + arr[step + 1][actualIndex + 1], actualIndex + 1);
  return Math.max(valueLeft, valueRight);
}

function main() {
  const T: number = Number(readLine().trim()); 

  for (let t = 0; t < T; t++) {
    const N: number = Number(readLine().trim()); 
    const arr: number[][] = [];
    for (let i = 0; i < N; i++) {
      const line = readLine().trim().split(' ').map(Number);
      arr.push(line);
    }

    const result = findMax(arr, 0, arr[0][0], 0);

    console.log(result);
  }
}

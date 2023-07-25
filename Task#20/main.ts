/*
Task #20
Factorial digit sum
Level: Easy
Points: 100
*/

export{}

process.stdin.resume();
process.stdin.setEncoding('utf-8');
let inputString: string = '';
let inputLines: string[] = [];
let currentLine: number = 0;
const N: number = 1000;

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

function multiplyLargeNumbers(a: number[], b: number): number[] {
  let newNumber: number[] = [];
  let rest = 0;
  a.forEach( (digit) => {
    newNumber.push((digit * b + rest) % 10);
    rest = Math.floor((digit * b + rest) / 10);
  })
  while (rest != 0) {
    newNumber.push(rest%10);
    rest = Math.floor(rest/10);
  }

  return newNumber;
    
  
}

function createFactorialCounterDict( n: number): { [index: number]: number } {
  let dictFact: {[index: number]: number[]}   = {};
  dictFact[0] = [1];
  for ( let i = 1; i <= N; i++){
    dictFact[i] = multiplyLargeNumbers(dictFact[i-1], i)
  }

  let dictFactCounter: {[index: number]: number} = {}
  for (const key in dictFact) {
    dictFactCounter[key] = dictFact[key].reduce((a, b) => a + b, 0);
  }

  return dictFactCounter;
}

function main() {
  const T: number = Number(readLine().trim()); 

  for (let t = 0; t < T; t++) {
    const n: number = Number(readLine().trim()); 
    
    const factCounterDict: {[index: number]: number}  = createFactorialCounterDict(N);
    const result = factCounterDict[n];
    console.log(result);
  }
}

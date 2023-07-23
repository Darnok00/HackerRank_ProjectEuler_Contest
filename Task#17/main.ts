/*
Task #17
Number to Words
Level: Easy
Points: 100
*/
export {};

const dictNumberToWords: {[index: number]: string } = {
  0: "",
  1: " One", 
  2: " Two",
  3: " Three",
  4: " Four",
  5: " Five",
  6: " Six",
  7: " Seven",
  8: " Eight",
  9: " Nine",
  10: " Ten",
  11: " Eleven",
  12: " Twelve",
  13: " Thirteen",
  14: " Fourteen",
  15: " Fifteen",
  16: " Sixteen",
  17: " Seventeen",
  18: " Eighteen",
  19: " Nineteen",
  20: " Twenty",
  30: " Thirty",
  40: " Forty",
  50: " Fifty",
  60: " Sixty",
  70: " Seventy",
  80: " Eighty",
  90: " Ninety",
  100: " Hundred",
  1000: " Thousand",
  1000000: " Million",
  1000000000: " Billion",
  1000000000000: " Trillion"
};

function createWord(n: number) {
  let big_number: number = 1;
  let word: string = ""

  while(n > 0) {
    let new_word: string = ""
    let act_n: number = n % 1000

    if (act_n > 100) {
      new_word += (dictNumberToWords[Math.floor(act_n / 100)] +  dictNumberToWords[100])
      act_n = act_n % 100
    }

    if ( Math.floor(act_n / 10) != 1 ) {
      new_word += (dictNumberToWords[Math.floor(act_n / 10) * 10] + dictNumberToWords[act_n%10])
    } else {
      new_word += dictNumberToWords[act_n]
    }

    if (big_number != 1 && new_word != "") {
      new_word += dictNumberToWords[big_number]
    }

    big_number *= 1000;
    word = new_word + word;
    n = Math.floor(n/1000);
  }

  return word.substring(1);
}

function processInput(input: string) {
  const lines = input.trim().split('\n');
  const t: number = Number(lines[0]);

  for (let i = 0; i < t; i++) {
    const n = Number(lines[i + 1]);
    console.log(createWord(n));
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

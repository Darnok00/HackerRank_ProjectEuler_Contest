/*
Task #19
Counting Sundays
Level: Easy
Points: 100
*/

export {};

process.stdin.resume();
process.stdin.setEncoding("utf-8");
let inputString: string = "";
let inputLines: string[] = [];
let currentLine: number = 0;
const startYear: number = 1900;
const numberDaysSineFirstJanuary: { [index: number]: number } = {
  [1]: 0,
  [2]: 31,
  [3]: 59,
  [4]: 90,
  [5]: 120,
  [6]: 151,
  [7]: 181,
  [8]: 212,
  [9]: 243,
  [10]: 273,
  [11]: 304,
  [12]: 334,
  [13]: 365,
};

process.stdin.on("data", function (inputStdin: string): void {
  inputString += inputStdin;
});

process.stdin.on("end", function (): void {
  inputLines = inputString.split("\n");
  inputString = "";
  main();
});

function readLine(): string {
  return inputLines[currentLine++];
}

function isLeapYear(year: number): boolean {
  if ((year % 4 == 0 && year % 100 != 0) || year % 400 == 0) {
    return true;
  } else {
    return false;
  }
}

function getDayWeek(date: number[]): number {
  const yearsSineStartDate = date[0] - startYear;
  let daysSinceStartDate =
    yearsSineStartDate * 365 + //classic years
    Math.floor((yearsSineStartDate + 3) / 4) -
    Math.floor((yearsSineStartDate + 99) / 100) +
    Math.floor((yearsSineStartDate + 299) / 400); //leap years
  daysSinceStartDate += numberDaysSineFirstJanuary[date[1]] + date[2];
  if (isLeapYear(date[0]) && date[1] > 2) {
    daysSinceStartDate += 1;
  }

  return daysSinceStartDate % 7;
}

function findSundays(
  firstCalendarDate: number[],
  secondCalendarDate: number[]
): number {
  const dayFirstDate: number = getDayWeek(firstCalendarDate);
  let actDate: number[] = firstCalendarDate;
  let actDay: number = dayFirstDate;
  let numberSundays = 0;

  if (dayFirstDate === 0 && firstCalendarDate[2] === 1) {
    numberSundays += 1;
  }

  if (
    firstCalendarDate[0] == secondCalendarDate[0] &&
    firstCalendarDate[1] == secondCalendarDate[1]
  ) {
    return numberSundays;
  }

  actDate =
    firstCalendarDate[1] === 12
      ? [firstCalendarDate[0] + 1, 1, 1]
      : [firstCalendarDate[0], firstCalendarDate[1] + 1, 1];
  actDay = getDayWeek(actDate);

  while (
    (actDate[0] != secondCalendarDate[0] ||
    actDate[1] != secondCalendarDate[1])
  ) {
    if (actDay === 0) {
      numberSundays += 1;
    }
    actDate =
    actDate[1] === 12
      ? [actDate[0] + 1, 1, 1]
      : [actDate[0], actDate[1] + 1, 1];
    actDay = getDayWeek(actDate);
  }

  if (getDayWeek([secondCalendarDate[0], secondCalendarDate[1], 1]) === 0) {
    numberSundays += 1;
  }

  return numberSundays;
}

function main() {
  const T: number = Number(readLine().trim());

  for (let t = 0; t < T; t++) {
    const firstCalendarDate: number[] = readLine()
      .trim()
      .toString()
      .split(" ")
      .map(Number);
    const secondCalendarDate: number[] = readLine()
      .trim()
      .toString()
      .split(" ")
      .map(Number);

    const result = findSundays(
      firstCalendarDate,
      secondCalendarDate
    ).toString();

    console.log(result);
  }
}
// write cpp file for max points

#include <iostream>
#include <vector>

const int startYear = 1900;
const int numberDaysSineFirstJanuary[] = {0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334, 365};

bool isLeapYear(unsigned long long int year) {
    return (year % 4 == 0 && year % 100 != 0) || year % 400 == 0;
}

unsigned long long int getDayWeek(const std::vector<unsigned long long int>& date) {
    unsigned long long int yearsSinceStartDate = date[0] - startYear;
    unsigned long long int daysSinceStartDate =
        yearsSinceStartDate * 365 + // classic years
        (yearsSinceStartDate + 3) / 4 -
        (yearsSinceStartDate + 99) / 100 +
        (yearsSinceStartDate + 299) / 400; // leap years
    daysSinceStartDate += numberDaysSineFirstJanuary[date[1] - 1] + date[2];
    if (isLeapYear(date[0]) && date[1] > 2) {
        daysSinceStartDate += 1;
    }

    return daysSinceStartDate % 7;
}

unsigned long long int findSundays(const std::vector<unsigned long long int>& firstCalendarDate, const std::vector<unsigned long long int>& secondCalendarDate) {
    unsigned long long int dayFirstDate = getDayWeek(firstCalendarDate);
    std::vector<unsigned long long int> actDate = firstCalendarDate;
    unsigned long long int actDay = dayFirstDate;
    unsigned long long int numberSundays = 0;

    if (dayFirstDate == 0 && firstCalendarDate[2] == 1) {
        numberSundays += 1;
    }

    if (firstCalendarDate[0] == secondCalendarDate[0] && firstCalendarDate[1] == secondCalendarDate[1]) {
        return numberSundays;
    }

    actDate = (firstCalendarDate[1] == 12) ? std::vector<unsigned long long int>{firstCalendarDate[0] + 1, 1, 1} : std::vector<unsigned long long int>{firstCalendarDate[0], firstCalendarDate[1] + 1, 1};
    actDay = getDayWeek(actDate);

    while (!(actDate[0] == secondCalendarDate[0] && actDate[1] == secondCalendarDate[1])) {
        if (actDay == 0) {
            numberSundays += 1;
        }
        actDate = (actDate[1] == 12) ? std::vector<unsigned long long int>{actDate[0] + 1, 1, 1} : std::vector<unsigned long long int>{actDate[0], actDate[1] + 1, 1};
        actDay = getDayWeek(actDate);
    }

    if (getDayWeek(std::vector<unsigned long long int>{secondCalendarDate[0], secondCalendarDate[1], 1}) == 0) {
        numberSundays += 1;
    }

    return numberSundays;
}

int main() {
    unsigned long long int T;
    std::cin >> T;

    for (unsigned long long int t = 0; t < T; t++) {
        std::vector<unsigned long long int> firstCalendarDate(3);
        std::vector<unsigned long long int> secondCalendarDate(3);

        for (int i = 0; i < 3; i++) {
            std::cin >> firstCalendarDate[i];
        }

        for (int i = 0; i < 3; i++) {
            std::cin >> secondCalendarDate[i];
        }

        unsigned long long int result = findSundays(firstCalendarDate, secondCalendarDate);
        std::cout << result << std::endl;
    }

    return 0;
}

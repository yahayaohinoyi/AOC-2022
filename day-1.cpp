#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int getMaximumCalories(const vector<int>& calories) {
    int max = -1;
    for (auto it = calories.begin(); it != calories.end(); ++it) {
        if (*it > max) {
            max = *it;
        }
    }
    return max;
}

int elvesWithTopThreeSnacks(vector<int> calories) {
    int i = 0;
    int res = 0;
    std::make_heap(calories.begin(), calories.end());
    while (i < 3) {
        std::pop_heap(calories.begin(), calories.end());    
        res += calories.back();
        calories.pop_back();
        i++;
    }
    return res;
}

int main() {
    std::string filename = "day-1.txt";
    std::ifstream fs(filename);
    std::string myText;
    vector<int> calories;

    int sumOfElfCalories = 0;
    while (getline(fs, myText)) {
        if (myText.empty()) {
            calories.push_back(sumOfElfCalories);
            sumOfElfCalories = 0;
        } else {
            sumOfElfCalories += std::stoi(myText);
        }
    }
    calories.push_back(sumOfElfCalories);

    int maxCalories = getMaximumCalories(calories);
    int topThree = elvesWithTopThreeSnacks(calories);
    cout << " Maximum Calories ----> " << maxCalories << endl;
    cout << " Top Three Maximum Calories ----> " << topThree << endl;
    fs.close();
    return 0;
}

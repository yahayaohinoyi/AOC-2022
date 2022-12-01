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

int main() {
    std::string filename = "day-1.txt";
    std::ifstream fs(filename);
    std::string myText;
    vector<int> calories;

    int sumOfElfCalories = 0;
    while (getline(fs, myText)) {
        if (myText.empty()) {
            calories.push_back(sumOfElfCalories);
            cout << sumOfElfCalories << "--------" << endl;
            sumOfElfCalories = 0;
        } else {
            sumOfElfCalories += std::stoi(myText);
        }
    }
    calories.push_back(sumOfElfCalories);

    int maxCalories = getMaximumCalories(calories);
    cout << " Maximum Calories ----> " << maxCalories << endl;
    fs.close();
    return 0;
}

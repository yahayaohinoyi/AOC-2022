#include <iostream>
#include <fstream>
#include <vector>
#include <sstream>
#include <map>

using namespace std;

// 0 - 1 - 2
int isWin(std::string elveSuggestion, std::string mySuggestion) {
    if (elveSuggestion == "A") {
        if (mySuggestion == "X") {
            return 1;
        } else if (mySuggestion == "Z") {
            return 0;
        }
        return 2;
    } if (elveSuggestion == "B") {
        if (mySuggestion == "X") {
            return 0;
        } else if (mySuggestion == "Y") {
            return 1;
        }
        return 2;
    } if (elveSuggestion == "C") {
        if (mySuggestion == "X") {
            return 2;
        } else if (mySuggestion == "Y") {
            return 0;
        }
        return 1;
    }
    return 0;
}

std::string matchElvesPlay(std::string elveSuggestion, std::string instruction) {
    if (elveSuggestion == "A") {
        if (instruction == "X") {
            return "Z";
        } else if (instruction == "Z") {
            return "Y";
        }
        return "X";
    } if (elveSuggestion == "B") {
        if (instruction == "X") {
            return "X";
        } else if (instruction == "Y") {
            return "Y";
        }
        return "Z";
    } if (elveSuggestion == "C") {
        if (instruction == "X") {
            return "Y";
        } else if (instruction == "Y") {
            return "Z";
        }
        return "X";
    }
    return "Y";
}

int processRound(std::string elveSuggestion, std::string mySuggestion) {
    const int WIN = 6;
    const int DRAW = 3;
    const int LOSS = 0;

    std::map<std::string, int> games = {
        {"X", 1},
        {"Y", 2},
        {"Z", 3}
    };
    if (games.find(mySuggestion) != games.end()) {
        std::string reinterpreteElfInstruction = matchElvesPlay(elveSuggestion, mySuggestion);
        int myScore = games.at(reinterpreteElfInstruction);
        int win = isWin(elveSuggestion, reinterpreteElfInstruction);
        if (win > 1) {
            return myScore + WIN;
        } else if (win > 0) {
            return myScore + DRAW;
        } else {
            return myScore + LOSS;
        }
    }
    return 0;
}

int main() {
    std::string filename = "day-2.txt";
    ifstream fs(filename);
    std::string myText;
    int result = 0;

    while(getline(fs, myText)) {
        std::istringstream iss(myText);
        string elveSuggestion, mySuggestion;
        if (!(iss >> elveSuggestion >> mySuggestion)) { break; }
        result += processRound(elveSuggestion, mySuggestion);  
    }
    cout << result << endl;
    return 0;
}
#include <iostream>
#include <cmath>
#include "KahanSum.tpp"
#include <vector>
#include <array>
#include <list>
using namespace std;

// template <typename T> //Old school equivalent: template <class T>
// long double KahanSum(vector<long double> MyContainer);


// What's happening behind the scene? 
// C++ sees function call, sees type, goes to template, 
// and replaces "template" with type found in main for those variables.

// only cpp files can be written into terminal to compile the the program of 4 files (KahanSum.cpp main.cpp KahanSum.hpp KahanSum.tpp)
// .hpp needs to have all #include <libraries> and #include "file.tpp"
// templates go into .tpp file and act like libraries.

//g++ -std=c++17 main.cpp KahanSum.cpp -o testing
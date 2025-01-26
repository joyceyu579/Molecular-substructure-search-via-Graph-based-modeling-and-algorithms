#include "KahanSum.hpp"

int main(void)
{
    
    cout << endl << "===========COMPENSATED (KAHAN) SUM===================" <<endl;
    vector<long double> test1 = {10000, 8*pow(10,-13), 8*pow(10,-13), 8*pow(10,-13), 8*pow(10,-13), 8*pow(10,-13)};
    long double test1_1 = KahanSum(test1);
    cout << "test1 (vector): " << test1_1 << endl;

    list<long double> test2 = {10000, 8*pow(10,-13), 8*pow(10,-13), 8*pow(10,-13), 8*pow(10,-13), 8*pow(10,-13)};
    long double test2_1 = KahanSum(test2);
    cout << "test2 (list): " << test2_1 << endl;

    array<long double, 6> test3 = {10000, 8*pow(10,-13), 8*pow(10,-13), 8*pow(10,-13), 8*pow(10,-13), 8*pow(10,-13)};
    long double test3_1 = KahanSum(test3);
    cout << "test3 (array): " << test3_1 << endl;
    
    vector<long double> test4(100000 , 8*pow(10,-13)); // Extreme test. Vector of size 100,000 with each element being a very small number.
    test4.push_back(1*pow(10,8)); // Extreme test. Adding bunch of small #'s to 1 big #.
    long double test4_1 = KahanSum(test4);
    cout << "test4 (extreme): " << test4_1<< endl << endl;
    
    cout << "===========REGULAR (STL) SUM===================" <<endl;
    vector<long double> test5 = {10000, 8*pow(10,-13), 8*pow(10,-13), 8*pow(10,-13), 8*pow(10,-13), 8*pow(10,-13)};
    long double test5_1 = RegularSum(test5);
    cout << "test5 (vector): " << test5_1 << endl;

    list<long double> test6 = {10000, 8*pow(10,-13), 8*pow(10,-13), 8*pow(10,-13), 8*pow(10,-13), 8*pow(10,-13)};
    long double test6_1 = RegularSum(test6);
    cout << "test6 (list): " << test6_1 << endl;

    array<long double, 6> test7 = {10000, 8*pow(10,-13), 8*pow(10,-13), 8*pow(10,-13), 8*pow(10,-13), 8*pow(10,-13)};
    long double test7_1 = RegularSum(test7);
    cout << "test7 (array): " << test7_1 << endl;

    vector<long double> test8(100000 , 8*pow(10,-13)); // Extreme test. Vector of size 100,000 with each element being a very small number.
    test8.insert(test8.begin(), 1*pow(10,8));
    // test8.push_back(1*pow(10,8)); // Extreme test. Adding bunch of small #'s to 1 big #.
    long double test8_1 = RegularSum(test8);
    cout << "test8 (extreme): " << test8_1<< endl << endl;
    
    return 0;
}

    // What's happening behind the scene? 
    // C++ sees function call, sees type, goes to template, 
    // and replaces "template" with type found in main for those variables.

    //g++ -std=c++17 main.cpp KahanSum.cpp -o testing
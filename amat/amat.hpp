#pragma once 

#include <iostream>
#include "include/Eigen/Eigen"
#include <complex>
#include <utility>
#include <iostream>
using namespace Eigen;
using namespace std;
#include <cmath>
#include <vector>
// HEADER FILE SHOULD ONLY CONTAIN DECLARATIONS AND OTHER INCLUDED LIBRARIES
class Molecule
{
private:
    vector<string> atoms_;
    vector< pair<int, int> > bonds_;
public:
    Molecule(const vector<string> & atoms, const vector<pair<int,int>> & bonds);
    Molecule(const Molecule & other); // copy constructor

    const MatrixXd get_AdjMatrix();

    int nwalks (double length, const int & atom1_index, const int & atom2_index);

    const VectorXi get_degrees();

    ~Molecule();
};

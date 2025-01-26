#include "amat.hpp"

int main(void)
{
    vector<string> MyAtoms = {"H", "O", "H"};
    vector<pair<int,int>> MyBonds = {make_pair(0,1), make_pair(1,2), /*repeat, but flip x y*/ make_pair(1,0), make_pair(2,1)};

    Molecule MyMolecule = Molecule(MyAtoms, MyBonds);
    cout << "My Adj Matrix" << endl << MyMolecule.get_AdjMatrix() << endl;
    MyMolecule.nwalks(2, MyAtoms.size()/2, MyAtoms.size()/2);
    cout <<  MyMolecule.get_degrees() << endl;
    

    vector<string> CH4_atoms = {"C", "H", "H", "H", "H"};
    vector<pair<int,int>> CH4_Bonds = {
        make_pair(0,1), make_pair(0,2), make_pair(0,3), make_pair(0,4),
        /*repeat, but flip x y*/ 
        make_pair(1,0), make_pair(2,0), make_pair(3,0), make_pair(4,0)};
    Molecule CH4 = Molecule(CH4_atoms, CH4_Bonds);
    cout << "CH4 Adj Matrix" << endl << CH4.get_AdjMatrix() << endl;
    CH4.nwalks(2, CH4_atoms.size()/2, CH4_atoms.size()/2);
    VectorXi CH4_degrees = CH4.get_degrees();
    cout << CH4_degrees << endl;

    return 0;
}

// terminal: g++ -std=c++17 -I./eigen-3.4.0 main.cpp amat.cpp -o main

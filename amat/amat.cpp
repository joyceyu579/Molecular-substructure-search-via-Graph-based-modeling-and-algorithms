#include "amat.hpp"

// adding const for paramteres where i don't change parameter inside function
// pass by reference if previously declared as attribute
// reference getters
// const before a function means that the return type is const

Molecule::Molecule(const vector<string> & atoms, const vector<pair<int,int>> & bonds)
{
    atoms_ = atoms;
    bonds_ = bonds;
}


Molecule::Molecule(const Molecule & other) // copy constructor
    :atoms_(other.atoms_), 
    bonds_(other.bonds_)
    {}


const MatrixXd Molecule::get_AdjMatrix() // make return value const. 
{
    // Method for obtaining adjacency matrix.
    MatrixXd AdjMatrix;

    // get length of atoms_
    int n = atoms_.size();

    // initialize matrix of n x n size. 
    AdjMatrix = MatrixXd::Zero(n,n); 

    // loop through bonds:
    for(int i=0; i < bonds_.size(); i++)
    {// index into adjmatrix
    AdjMatrix.coeffRef(bonds_[i].first,bonds_[i].second) = 1;
    }
    // cout << AdjMatrix << endl;

    return AdjMatrix;
}


int Molecule::nwalks (double length, const int & atom1_index, const int & atom2_index) // adding const where i don't change parameter inside function
{
    // Bounds checking:
    if(atom1_index >= atoms_.size() || atom2_index >= atoms_.size())
    {
        cout << "Please enter a valid indexes that is less than " << atoms_.size() << endl;
        return -1;
    }
    
    // Compute number of walks of the given length between the two atoms.
    int n = atoms_.size();
    MatrixXd MyWalks = MatrixXd::Identity(n, n);

    MatrixXd MyMatrix = get_AdjMatrix();

    for(int i = 0; i < length ; i++)
    {
        MyWalks *=  MyMatrix; 
    }

    cout << "My walking matrix: " << endl << MyWalks << endl;
    // cout << "Walk at row" << atom1_index << " and column" << atom2_index << " is: " << MyWalks.coeffRef(atom1_index, atom2_index) << endl;

    return MyWalks.coeffRef(atom1_index, atom2_index);
}

const VectorXi Molecule::get_degrees()
{
    // Returns Eigen vector of degree of each atom inside the molecule for the whole molecule.
    VectorXi MyDegrees(atoms_.size()) ;
    // degree of vertex = sum of row (or column) in adj matrix. "Block operations"
    MatrixXd MyMatrix = get_AdjMatrix();

    // cout << "My bonds of element at " << atoms_[0] << ": " << MyMatrix.row(0) << endl;
    // cout << "Degrees of " << atoms_[0] << ": " << " " << MyMatrix.row(0).sum() << endl;

    // cout << "My bonds of element at " << atoms_[1] << ": "<< MyMatrix.row(1) << endl;
    // cout << "Degrees of " << atoms_[1] << ": " << ": " << MyMatrix.row(1).sum() << endl;

    for(int i=0 ; i < atoms_.size() ; i++)
    {
        int degree = MyMatrix.row(i).sum();
        //cout << degree << endl;
        MyDegrees(i) = degree;
        //cout << "My bonds of element at " << atoms_[i] << ": "<< MyMatrix.row(i) << endl;
        cout << "Degrees of " << atoms_[i] << ": " << ": " << MyMatrix.row(i).sum() << endl;
    }

    return MyDegrees;
}

Molecule::~Molecule(){cout<<"In destructor."<<endl;};
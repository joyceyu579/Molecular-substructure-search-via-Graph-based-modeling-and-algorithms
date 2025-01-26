# Taking in user defined arguements for a function (2 ways): arg.syst[] and argparse
# USE ARGPARSE TO PERFORM SUBSTRUCTURE SEARCH FROM TERMINAL.

if __name__ == "__main__":
    import argparse
    from FinalProject import *

    parser = argparse.ArgumentParser(
        description="This script can be used to generate graph representations of molecules and perform a substructure search."
    )
    parser.add_argument(
        "sdf1",
        help="The sdf file representing the molecule that the user would like to perform a substructure search on and obtained from online source.",
        type=str,
    )
    parser.add_argument(
        "sdf2",
        help="The sdf file representing the substructure the user obtains from online source.",
        type=str,
    )

    args = parser.parse_args()

    molecule_sdf = args.sdf1  # egcg
    substructure_sdf = args.sdf2  # benzene

    # Use GraphMolecule class to perform substructure search:
    MyMolecule = Molecule(molecule_sdf)
    MySubstructure = Molecule(substructure_sdf)

    # Get their molecular fingerprints
    MyMolecule_fingerprint = MyMolecule.getHashedPathFingerprint()
    MySubstructure_fingerprint = MySubstructure.getHashedPathFingerprint()

    # Substructure search means all indices that benzene has 1 at should also be same indices egcg has benzene at.
    substructure_indices = []
    for char in list(enumerate(MySubstructure_fingerprint)):
        if char[1] == "1":
            substructure_indices.append(char[0])
        else:
            continue

    MyMolecule_indices = []
    for char in list(enumerate(MyMolecule_fingerprint)):
        if char[1] == "1":
            MyMolecule_indices.append(char[0])
        else:
            continue

    Substructure_match = []
    for i in substructure_indices:
        if i in MyMolecule_indices:
            Substructure_match.append(True)
        else:
            Substructure_match.append(False)

    if False in Substructure_match:
        print("substructure not found.")
    else:
        print("substructure found.")

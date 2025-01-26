"""
Tests for Final Project's Molecule object.
"""

from FinalProject import *
import pytest


def test_user_choice_nodes_edges():
    # Check output of parse_sdf used in and out of the class.
    nodes, edges = parse_sdf("sdf/AHJRHEGDXFFMBM-UHFFFAOYSA-N.sdf")
    molecule1 = Molecule(nodes=nodes, edges=edges)
    molecule2 = Molecule(sdf="sdf/AHJRHEGDXFFMBM-UHFFFAOYSA-N.sdf")
    assert molecule1.nodes == molecule2.nodes
    assert molecule1.edges == molecule2.edges

    # test for valid construction:
    with pytest.raises(InvalidConstruction):
        molecule1 = Molecule(nodes=nodes, edges=None)
    with pytest.raises(InvalidConstruction):
        molecule1 = Molecule(nodes=None, edges=edges)
    with pytest.raises(InvalidConstruction):
        molecule1 = Molecule()
    with pytest.raises(InvalidConstruction):
        molecule1 = Molecule(sdf="sdf/AHJRHEGDXFFMBM-UHFFFAOYSA-N.sdf", edges=edges)


def test_count_rings():
    molecule1 = Molecule("sdf/AHJRHEGDXFFMBM-UHFFFAOYSA-N.sdf")
    assert molecule1.count_rings[0] == 5
    molecule2 = Molecule("sdf/AAOVKJBEBIDNHE-UHFFFAOYSA-N.sdf")
    assert molecule2.count_rings[0] == 3


def test_visualize_molecule():
    molecule1 = Molecule("sdf/AHJRHEGDXFFMBM-UHFFFAOYSA-N.sdf")
    molecule2 = Molecule("sdf/AGMMTXLNIQSRCG-UHFFFAOYSA-N.sdf")
    molecule3 = Molecule("sdf/AHJGUEMIZPMAMR-WZTVWXICSA-N.sdf")
    molecule1.visualize_molecule()
    molecule2.visualize_molecule()
    molecule3.visualize_molecule()


def test_HasAromaticRings():
    molecule1 = Molecule("sdf/AHJRHEGDXFFMBM-UHFFFAOYSA-N.sdf")
    molecule2 = Molecule("carbonylS.sdf")
    assert molecule1.HasAromaticRings is True
    assert molecule2.HasAromaticRings is False


def test_getHashedPathFingerprint():
    molecule1 = Molecule("sdf/AHJRHEGDXFFMBM-UHFFFAOYSA-N.sdf")
    molecule2 = Molecule("sdf/AHJRHEGDXFFMBM-UHFFFAOYSA-N.sdf")
    molecule3 = Molecule("sdf/AAOVKJBEBIDNHE-UHFFFAOYSA-N.sdf")

    # Test if output vector length is still equal to user defined bit length
    assert len(molecule1.getHashedPathFingerprint(2048, 7, 5)) == 2048

    # Check the number of 1's you have:
    molecule1.getHashedPathFingerprint(2048, 7, 5) == 17

    # Check if SAME sdf file generate the same fingerprint
    assert molecule1.getHashedPathFingerprint(
        2048, 7, 5
    ) == molecule2.getHashedPathFingerprint(2048, 7, 5)
    # Check if DIFFERENT sdf file generate different fingerprint
    assert molecule1.getHashedPathFingerprint(
        2048, 7, 5
    ) != molecule3.getHashedPathFingerprint(2048, 7, 5)


def test_eq():
    molecule1 = Molecule("sdf/AHJRHEGDXFFMBM-UHFFFAOYSA-N.sdf")
    molecule2 = Molecule("sdf/AHJRHEGDXFFMBM-UHFFFAOYSA-N.sdf")
    molecule3 = Molecule("sdf/AAOVKJBEBIDNHE-UHFFFAOYSA-N.sdf")

    assert molecule1 == molecule2
    assert molecule1 != molecule3


def test_abstraction():
    molecule1 = Molecule("sdf/AHJRHEGDXFFMBM-UHFFFAOYSA-N.sdf")
    assert molecule1.rings == 5

    with pytest.raises(TypeError):
        molecule1.HasAromaticRings()

import networkx as nx
from networkx import convert
import matplotlib.pyplot as plt
from provided import parse_sdf
import random
from itertools import combinations

class InvalidConstruction(Exception):
    def __init__(self, error="Please enter sdf file OR nodes AND edges.") -> None:
        super().__init__(error)


class Molecule(nx.Graph):

    def __init__(self, sdf=None, nodes=None, edges=None) -> None:
        super().__init__()
        if sdf == None and nodes == None and edges == None:
            raise InvalidConstruction()
        if sdf != None and (nodes != None or edges != None):
            raise InvalidConstruction()
        if sdf != None:
            self.sdf = sdf
            self.nodes_and_edges = parse_sdf(sdf)
            self.nodess = self.nodes_and_edges[0]
            self.edgess = self.nodes_and_edges[1]
        if nodes != None and edges != None:
            self.nodess = nodes
            self.edgess = edges
        if (nodes != None and edges == None) or (nodes == None and edges != None):
            self.nodess = nodes
            self.edgess = edges
            raise InvalidConstruction()
        if self.edgess:
            format = []
            for i in self.edgess:
                format.append((i[0], i[1], {"weight": i[2]}))
            convert.to_networkx_graph(format, create_using=self)

        self._rings = self.count_rings[0]
        self._atoms_per_ring = self.count_rings[1]
        self._fingerprint = self.getHashedPathFingerprint
        self._HasAromaticRings = self.HasAromaticRings

    @property
    def count_rings(self) -> tuple[int, list[int]]:
        '''
        Counts the number of rings in a Molecule object. 
        Also lists the atoms composing each ring.
        ______
        Input paramters:
            self (Molecule)
        ______
        Returns:
            self.rings (int)
            Atoms_in_cycle (list[list[str]])
        '''
        Atoms_in_cycle = nx.cycle_basis(self)
        Num_of_cycles = len(Atoms_in_cycle)
        Num_Atoms_per_cycle = [
            len(Atoms_in_cycle[i]) for i in range(len(Atoms_in_cycle))
        ]
        self.rings = Num_of_cycles
        self.atoms_per_ring = Atoms_in_cycle
        return self.rings, Atoms_in_cycle

    def visualize_molecule(self):
        '''
        Generates visual of graph molecule using cpk coloring scheme.
        Exports visual as .png into current working directory.
        _____
        Input paramters:
            self (Molecule)
        _____
        Returns:
            fig (matplotlib.pyplot.figure)
        '''
        cpk_colors = []
        for k, v in self.nodess.items():
            if v == "C":
                cpk_colors.append("Grey")
            elif v == "N":
                cpk_colors.append("blue")
            elif v == "S":
                cpk_colors.append("yellow")
            else:
                cpk_colors.append("red")
        fig = plt.figure()
        nx.draw_networkx(self, labels=self.nodess, node_color=cpk_colors)
        plt.savefig("MyGraphedMolecule.png")
        return fig

    @property
    def HasAromaticRings(self):
        '''
        Detects Aromatic ring(s) in molecule.
        A ring is aromatic based on 4 criterias:
        Criteria 1: Cyclic structure.
        Criteria 2: Fully planar (This method assumes any detected rings/cycles is planar).
        Criteria 3: Conjugated and sp2 hybridized.
        Criteria 4: Satisfies Huckel's rule (4n+2 = # pi electrons , where n is non-negative integer)
        _____
        Input paramters:
            self (Molecule)
        _____
        Returns:
            True (Bool) if an aromatic ring is in molecule.
            False (Bool) if no aromatic ring is in molecule.
        '''
        rings, AtomsInRings = self.count_rings
        delocalized = [True] * rings
        BondsOfAllCycles = []

        # CHECK IF MOLECULE IS CYCLIC
        if rings > 0:

            # CHECK FOR ALTERNATING WEDGE WEIGHTS (1 vs. 2) AT EVERY ATOM IN THE RING:
            for cycle in range(rings):
                edges = list(zip(AtomsInRings[cycle], AtomsInRings[cycle][1:]))
                edges.append((AtomsInRings[cycle][-1], AtomsInRings[cycle][0]))
                # Get the edge weights
                Bonds = []
                for edge in edges:
                    for edgeweights in self.edgess:
                        if (
                            edge[0] == edgeweights[0]
                            and edge[1] == edgeweights[1]
                            or edge[0] == edgeweights[1]
                            and edge[1] == edgeweights[0]
                        ):
                            Bonds.append(edgeweights[2])
                BondsOfAllCycles.append(Bonds)

                # Check for double bonds at every other edge.
                for i in range(1, len(Bonds)):
                    if Bonds[i - 1] == Bonds[i]:
                        delocalized[cycle] = False
                        break
                if Bonds[0] == Bonds[-1]:
                    delocalized[cycle] = False

        if (
            True in delocalized
        ):  # If there's a ring that has alternating edge weights of 1 and 2
            # get that ring
            for i in range(rings):
                if delocalized[i] == True:
                    index = i
                    Num_DoubleBonds = BondsOfAllCycles[index].count(2)
                    pi_electrons = 2 * Num_DoubleBonds

                    # Check huckel's rule:
                    n = (pi_electrons - 2) / 4
                    if n >= 0:
                        return True
                else:
                    continue
        return False

    def _hash(self, nodes, path):
        '''
        Generates integer hash value used to generate molecular fingerprint.
        ____
        Input:
            self (Molecule)
            nodes (dict)
            path (list[tuples])
        Return:
            hash value (int)
        '''
        g = Molecule(nodes=nodes, edges=path)

        # Create hash
        key = nx.weisfeiler_lehman_subgraph_hashes(g)
        int_hash_value = 0
        for k, v in key.items():  # assuming key is a string
            for string in v:
                for char in string:
                    ascii_char_value = ord(char)
                    int_hash_value += ascii_char_value
        return int_hash_value

    def getHashedPathFingerprint(self, size=2048, pathlength=7, num_bits_per_hash=5):
        '''
        Generates molecular fingerprint.
        ____
        Input:
            self (Molecule)
            size (int) = 2048 bit vector length by default.  
            pathlength (int) = 7 by default.
            num_bits_per_hash (int) = 5 by default.
        Return:
            fingerprint (str)
        '''
        fingerprint = [0] * size  # initialize bitmap

        # Find all paths of size 1 to pathlength starting dfs at every node:
        MyPaths = []
        for i, j in combinations(list(self.nodess.keys()), 2):
            path = nx.all_simple_paths(self, i, j, pathlength)
            MyPaths.append(list(path))

        # Generate integer hash value (or seeds) for each path
        randomset = set()
        for ManyPaths in map(nx.utils.pairwise, MyPaths):
            for SomePaths in list(ManyPaths):
                for aPath in map(nx.utils.pairwise, SomePaths):

                    # Need to get weights/bonds to distinguish C-O from C=O
                    aPath = list(aPath)
                    bonds = []
                    for i in range(len(self.edgess)):
                        for j in range(len(list(aPath))):
                            if (
                                self.edgess[i][0] == list(aPath)[j][0]
                                and self.edgess[i][1] == list(aPath)[j][1]
                            ):
                                bonds.append(self.edgess[i])

                    MySeed = self._hash(aPath, bonds)
                    random.seed(MySeed)
                    randomint = random.getrandbits(num_bits_per_hash)
                    randomset.add(randomint)
                    index = MySeed % size
                    fingerprint[index] = randomint
        for i in range(len(fingerprint)):
            # Make fingerprint represent 1's where there is no 0
            if fingerprint[i] != 0:
                fingerprint[i] = 1
        # Make fingerprint into string
        fingerprint = list(map(str, fingerprint))
        fingerprint = "".join(fingerprint)
        return fingerprint

    def __eq__(self, other):
        '''
        Overloading operator (==).
        Checks if 2 Molecule objects are equal using molecular fingerprints.
        ____
        Input:
            self (Molecule)
            other (Molecule)
        Return:
            True (bool) if equal objects.
            False (bool) if non-equal objects.
        '''
        if not isinstance(other, Molecule):
            raise TypeError("Object types are not the same.")
        return self.getHashedPathFingerprint() == other.getHashedPathFingerprint()

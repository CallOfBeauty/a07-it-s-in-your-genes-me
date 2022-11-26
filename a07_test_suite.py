######################################################################
# TODO: Change the author(s) and username(s) to yourself and your partner (if any).
# Author(s): Dimitrios Ntentia
# Username(s): ntentiad
#
# Assignment: A07: It's in Your Genes
#
# Purpose: A test suite to test the a7_genes code
#
######################################################################
# Acknowledgements:
#   Original Author: Dr. Jan Pearce
#
#   Idea from: http://www.cs.uni.edu/~schafer/1140/assignments/pa9/index.htm
#
# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
####################################################################################

import sys
from a07_genes import *


def testit(did_pass):
    """
    Print the result of a unit test.

    :param did_pass: Boolean representing if the unit test passed or failed
    :return: None
    """
    # This function works correctly--it is verbatim from the text, Chapter 6

    linenum = sys._getframe(1).f_lineno                 # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)


def genomics_test_suite():
    """
    The genomics_test_suite() is designed to test the following:
      is_nucleotide(sequence)
      complement_strand()
      mRNA()
      chunk_amino_acid()
      amino_acid_chunks()
      sequence_gene()


    :return: None
    """


    # The following tests test the is_nucleotide() function
    print("Testing is_nucleotide()")
    testit(is_nucleotide("CGTAGGCAT") == True)
    testit(is_nucleotide("CGTAFLCAT") == False)
    # FIXME: Add your own tests here
    testit(is_nucleotide("QWERTY") == True)
    testit(is_nucleotide('TAG') == True)
    testit(is_nucleotide('CAB') == True)
    testit(is_nucleotide('CGTAFLCAT') == True)

    # Testing the complement_strand() function
    print("\nTesting complement_strand()")
    testit(complement_strand("CC") == "GG")
    testit(complement_strand("CA") == "GT")
    testit(complement_strand("CGTAGGCAT") == "GCATCCGTA")
    testit(complement_strand("CGTAFLCAT") == "Sequencing Error")
    # FIXME: Add your own tests here
    testit(complement_strand("ATRF") == "Sequencing Error")
    testit(complement_strand("A") == "Sequencing Error")
    testit(complement_strand("F") == True)
    testit(complement_strand("C") == False)
    testit(complement_strand("G") == True)


    # Testing the mRNA() function
    print("\nTesting mRNA()")
    testit(mRNA("GCATCCGTA") == "GCAUCCGUA")
    testit(mRNA("CCATTGGGTT") == "CCAUUGGGUU")
    testit(mRNA("AAGCACCG") == "AAGCACCG")
    # FIXME: Add your own tests here
    testit(mRNA("TTTT") == "UUUU")
    testit(mRNA("GCT") == "GCU")
    testit(mRNA("TT") == "UUUU")



    # Testing chunk_amino_acid()
    print("\nTesting chunk_amino_acid()")
    testit(chunk_amino_acid("CGUCAC") == ["CGU","CAC"])
    testit(chunk_amino_acid("CGUAGGCAUUU") == ["CGU","AGG","CAU"])      # note that the "extra two U's are discarded
    # FIXME: Add your own tests here
    testit(chunk_amino_acid("CG") == [])
    testit(chunk_amino_acid("QQQQ") == ["QQQ","Q"])
    testit(chunk_amino_acid("QQQQQQ") == ["QQQ", "QQQ"])




    # Testing amino_acid_chunks()
    print("\nTesting amino_acid_chunks()")
    testit(amino_acid_chunks('AGA') == 'R')
    testit(amino_acid_chunks('AFA') == '?')
    # FIXME: (Optional) Add your own tests here. You'll need to dig into and
    # FIXME: understand the dictionary in this function to write more of these tests
    testit(amino_acid_chunks('GAC') == 'D')
    testit(amino_acid_chunks('GACGACGAC') == 'DDD')






    # Testing sequence_gene()
    print("\nTesting sequence_gene()")
    testit(sequence_gene("T") == '')            # because input is not in a group of 3 nucleotides
    testit(sequence_gene("JAN") == '')          # because input is not a valid string of nucleotides
    testit(sequence_gene("CACGT") == 'V')       # because mRNA sequence is "GUGCA"
                                                # and ignoring the last two "extra" nucleotides,
                                                # this returns amino acid "V".
    testit(sequence_gene("CGTAGGCAT") == "ASV") # because mRNA sequence is "GCAUCCGUA"
                                                # taking the complement and then replacing the T nucleotide with U.
                                                # Grouping into triples, we  get the "ASV" amino acid sequence.

    # FIXME: (Optional) Add your own tests here. You'll need to dig into and
    # FIXME  understand the dictionary in amino_acid_chunks() to write more of these tests


def main():
    genomics_test_suite()


main()

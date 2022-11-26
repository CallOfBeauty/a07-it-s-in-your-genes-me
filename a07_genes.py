######################################################################
# TODO: Change the author(s) and username(s) to yourself and your partner (if any).
# Author(s): Dimitrios Ntentia
# Username(s): ntentiad
#
# Assignment: A07: It's in Your Genes
#
# Purpose: Determine an amino acid sequence given an input DNA sequence
#
######################################################################



# TODO   I highly suggest starting by building more test cases for each function in the test suite file.
# TODO   If you can build accurate test cases, you can be confident that you understand
# TODO   the intended functionality of each function.


def is_nucleotide(sequence):
    """
    Checks that the string sequence provided is a valid string
    consisting only of the 4 nucleotides A, C, G, and T
    Returns True if so, and False otherwise

    :param sequence:
    :return:Bool, True or False:
    """
    flag=False
    for i in sequence:
        if i=="A" or i=="C" or i=="G" or i=="T":
            flag=True
        else:
            flag=False
            break
    return flag

def complement_strand(sequence):
    """
    Returns the string which will be the second strand of the DNA sequence
    given that Ts complement As, and Cs complement Gs. If given
    a bad input, the function returns "Sequencing Error"

    :param sequence:
    :return:Boolean value, True or False:
    """

    complement = ""         # This can be used to "build" the complement
    if is_nucleotide(sequence)==True:
        for i in sequence:
            if i=="A":
                complement=complement+"T"
            elif i=="T":
                complement=complement+"A"
            elif i=="C":
                complement=complement+"G"
            elif i=="G":
                complement=complement+"C"
    else:
        complement="Sequencing Error"
    return complement



def mRNA(sequence):
    """
    Replaces each occurrence of the nucleotide T replaced with the nucleotide U.

    :param sequence:
    :return:string
    """


    mrna = ""
    for i in sequence:
        if i=="T":
            mrna+="U"
        else:
            mrna+=i
    return mrna


def chunk_amino_acid(sequence):
    """
    Uses output of mRNA(sequence) and divides it into substrings of length 3,
    ignoring any "extra DNA" at the far end returning the relevant substrings in a list.

    :param sequence:
    :return:A list
    """
    list_of_chunks = []
    item = ""

    for i in range(len(sequence)):
        if len(sequence) > 2:
            item += sequence[i]
            if (i + 1) % 3 == 0:
                list_of_chunks.append(item)
                item = ""

    return list_of_chunks


def amino_acid_chunks(three_char_seq):
    """
    Expects a three character string as a parameter and returns
    the corresponding single character AminoAcid

    :param three_char_seq: a sequence of three characters
    :return: A string representing the amino acid chunk for that sequence
    """

    # ###################################################################### #
    # #  This function is already completed correctly! No changes needed!  # #
    # ###################################################################### #

    # We haven't learned about dictionaries yet, but here is one for the extra curious.
    # You aren't expected to know what this is yet.
    translator = {"GCA": "A", "GCC": "A", "GCG": "A", "GCU": "A",
                  "AGA": "R", "AGG": "R", "CGA": "R", "CGC": "R", "CGG": "R", "CGU": "R",
                  "GAC": "D", "GAU": "D",
                  "AAC": "N", "AAU": "N",
                  "UGC": "C", "UGU": "C",
                  "GAA": "E", "GAG": "E",
                  "CAA": "Q", "CAG": "Q",
                  "GGA": "G", "GGC": "G", "GGU": "G", "GGG": "G",
                  "CAC": "H", "CAU": "H",
                  "AUA": "I", "AUC": "I", "AUU": "I",
                  "UUA": "L", "UUG": "L", "CUA": "L", "CUC": "L", "CUG": "L", "CUU": "L",
                  "AAA": "K", "AAG": "K",
                  "AUG": "M",
                  "UUC": "F", "UUU": "F",
                  "CCA": "P", "CCC": "P", "CCG": "P", "CCU": "P",
                  "AGC": "S", "AGU": "S", "UCA": "S", "UCC": "S", "UCG": "S", "UCU": "S",
                  "ACA": "T", "ACC": "T", "ACG": "T", "ACU": "T",
                  "UGG": "W",
                  "UAC": "Y", "UAU": "Y",
                  "GUA": "V", "GUC": "V", "GUG": "V", "GUU": "V",
                  "UAA": "*", "UAG": "*", "UGA": "*"
                 }

    if three_char_seq in translator.keys():
        return translator[three_char_seq]  # Given any 3 letter sequence, this returns the amino acid for that sequence
    else:
        return "?"                          # Returns a question mark if the input is invalid


def sequence_gene(sequence):
    """
    The sequence_gene() function takes a a sequence of nucleotides:
    A, C, G, and T and returns
    the corresponding amino acid sequence.

    :param sequence: a string representing a sequence of nucleotides
    :return: a string representing the amino acid sequence
    """

    # ###################################################################### #
    # #  This function is already completed correctly! No changes needed!  # #
    # ###################################################################### #

    aaseq=""                                                # Amino acid sequence
    if is_nucleotide(sequence):                             # Checks for a valid sequence
        comp_strand = complement_strand(sequence)           # Finds the complement sequence
        mrna = mRNA(comp_strand)                            # Finds the mRNA of the complement
        amino_acid_list = chunk_amino_acid(mrna)            # Chunks the mRNA sequence

        for amino_acid in amino_acid_list:                  # Loops through each chunk
            aaseq = aaseq + amino_acid_chunks(amino_acid)   # Creates the final amino acid sequence
    return aaseq                                            # Returns an empty string for any illegal input


def main():
    """
    The main() function runs the sequence_gene code, which calls all other parts of this code

    :return: None
    """

    # TODO When your code is fixed, the following line will print correctly.
    # TODO You do not need to modify the sequence_gene() function; it is correct already.
    print("The original sequence {0} returns {1}".format("CACGT", sequence_gene("CACGT")))


if __name__ == "__main__":
    main()          # call to main() function

# Accept a file with a list of DNA sequences and gives the reverse complement of each sequence
# Lines in the file must be in the following format:
#	>Sequence[0-9]+
#	[ATCG]+
from re import sub, compile
sequence_pattern = compile(r"(>Sequence\d+)\n([ATCG]+)")
read_file = input("Input File: ")

with open(read_file) as f:	# input
	sequence = f.read()
while sequence_pattern.search(sequence):
	match = sequence_pattern.search(sequence)
	dna = match[2]
	dna = "A".join([sub(r"A", r"T", base) for base in dna.split("T")])  # split on T's, flip A's in the resulting list to T's, join back with A's
	dna = "C".join([sub(r"C", r"G", base) for base in dna.split("G")])  # same as above, but with G's and C's
	sequence = sub(r"({0})\n[ATCG]+".format(match[1]), r"\1_ReverseComplement\n{0}\n".format(dna[::-1]), sequence) # replace the sequence with the reversed one
with open(read_file + "_out.txt", "w+") as f:	# output
	f.write(sequence)

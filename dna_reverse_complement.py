# Accept a file with a list of DNA sequences and gives the reverse complement of each sequence
# Lines in the file must be in the following format:
#	>Sequence[0-9]+
#	[ATCG]+
from re import sub,compile

sequence_pattern = compile(r"(>Sequence\d+)\n([ATCG]+)\b")
read_file = input("Input File: ")

with open(read_file) as f:
	sequence = f.read()
match = sequence_pattern.search(sequence) # prime the first match
while match:
	dna = match[2]
	dna = "A".join([sub(r"A", r"T", base) for base in dna.split("T")])  # split on T's, flip A's in the resulting list to T's, join back with A's
	dna = "C".join([sub(r"C", r"G", base) for base in dna.split("G")])  # same as above, but with G's and C's
	sequence = sub(r"({0})\n[ATCG]+\b".format(match[1]), r"\1_ReverseComplement\n" + dna[::-1], sequence) # rewrite the string again
	match = sequence_pattern.search(sequence)
	
with open("write_file.txt", "w+") as f:
	f.write(sequence)

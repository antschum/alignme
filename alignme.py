from Bio.Seq import Seq 


def read_dna(str file):
	
	#read sequence
	with open("dnafile_1.txt", "r") as file:
		seq = Seq(file.read().replace("\n", "").upper())

	return seq
	

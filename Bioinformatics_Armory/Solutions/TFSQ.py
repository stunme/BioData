##  FASTQ format introduction

"""
Problem
Sometimes it's necessary to convert data from FASTQ format to FASTA format. For example, you may want to perform a BLAST search using reads in FASTQ format obtained from your brand new Illumina Genome Analyzer.

Links:

A FASTQ to FASTA converter can be accessed from the Sequence conversion website

A free GUI converter developed by BlastStation is available here for download or as an add-on to Google Chrome.

There is a FASTQ to FASTA converter in the Galaxy web platform. Note that you should register in the Galaxy and upload your file prior to using this tool.

Given: FASTQ file

Return: Corresponding FASTA records

===================================================================
Sample Dataset
@SEQ_ID
GATTTGGGGTTCAAAGCAGTATCGATCAAATAGTAAATCCATTTGTTCAACTCACAGTTT
+
!*((((***+))%%%++)(%%%%).1***-+*****))**55CCF>>>>>>CCCCCCC65

Sample Output
>SEQ_ID
GATTTGGGGTTCAAAGCAGTATCGATCAAATAGTAAATCCATTTGTTCAACTCACAGTTT
"""

##  parset first two line
with open("../Datasets/TFSQ_dataset.txt",'r') as f:
    while True:
        print(f">{f.readline().strip()[1:]}")
        print(f.readline().strip())
        f.readline()
        if f.readline() =="":
            break


##  ==============================================================
# from Bio import SeqIO
# SeqIO.convert('test.fastq','fastq','test.fasta','fasta')
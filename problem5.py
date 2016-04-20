#! /user/bin/env python

'''
Problem-set-5
Johannes Menzel

'''

# P1 Q1
# On what chromasome is the region with the largest start position

from collections import defaultdict, Counter
# import imdb

laminafile = open('lamina.bed')

starts = 0
largestart = 0
chromosome = 0
bigend = 0
bigstart = 0
endchrom = 0
region_length = 0

for line in laminafile:

        if line.startswith('#'): # skips first line in file
                continue

        parseline = line.strip().split('\t') # removes junk defines colounms
        chrom = parseline[0]
        starts = int(parseline[1])
        end = int(parseline[2])

        if starts > largestart: # finds largest start
                largestart = starts
                chromosome = chrom

# P1 Q2 finds largest end region 
 
	if chrom == 'chrY': # looks for largest end value for chrmY
		if end > bigend:
			bigend = end
			bigstart = starts
			endchrom = chrom
			region_length = bigend - bigstart


print 'answer-1', chromosome
print 'answer-2', endchrom, bigstart,'-', bigend,'region length is', region_length


# P2 

file = 'SP1.fq'

line_num = 0
num_records = 0
num_C = 0
basecount = {}
recordname = ''

line_num = 0
largequal = 0
recordqual = 0
rev_comp = []

def reverse_complement(seq): # generates reverse complement
        num_rec = 0
        comps = []
        for char in seq:
                if char == 'N':
                        comps.append('N')
                if char == 'A':
                        comps.append('T')
                if char == 'T' or char == 'U':
                        comps.append('A')
                if char == 'G':
                        comps.append('C')
                if char == 'C':
                        comps.append('G')
        rev_comp = ''.join(reversed(comps))
        return rev_comp

def sum_quals(qual): # Does some weird shit I dont get
        qualsum = 0
        for char in qual:
                qualsum += ord(char)
        return qualsum


for line in open(file): # parses out feild in SP1 file

        line_type = line_num % 4
        if line_type == 0:
                name = line.strip()
        elif line_type == 1:
                seq = line.strip()
	elif line_type == 3:
		num_records += 1
                quals =  line.strip()

# Q1 which of the first 10 sequence records has the largest # of Cs 
               
		basecount = Counter(seq)
                if basecount['C'] > num_C and num_records <= 10:
                        num_C = basecount['C']
                        recordname = name

# Q2 finds largest sums of quals

		recordqual = sum_quals(quals)
		if recordqual > largequal:
			largequal = recordqual

# Q3 generate reverse complement of first 10 records

		if num_records <= 10:
			rev_comp.append(reverse_complement(seq))

        line_num += 1

print 'answer-3', recordname, 'Number of Cs', num_C
print 'answer-4', largequal
print 'answer-5', rev_comp





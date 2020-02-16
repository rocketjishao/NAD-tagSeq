#!/usr/bin/python
# -*- coding: UTF-8 -*-
# search for GAACCUGAACCU; AACCUGAACCUG; ACCUGAACCUGA; CCUGAACCUGAA; CUGAACCUGAAC; UGAACCUGAACC. 
import sys
def fun(argv):
    input_file = argv[0]
    output_file = argv[1]
    print 'input file:   %s' % (input_file)
    print 'search range: 40'
    print 'subsequence:  GAACCUGAACCU(12nt)' 
    print 'output file:  %s' % (output_file)
    records = []
    with open(input_file, 'r') as f:
        record = []
        for line in f.readlines():
            record.append(line.strip())
            if len(record) == 4:
                records.append(record)
                record = []
    match_count = 0
    with open(output_file, 'w') as f:
        for record in records:
            sequence = record[1][:40]
            if sequence.find('GAACCUGAACCU') < 0 and sequence.find('AACCUGAACCUG') < 0 and sequence.find('ACCUGAACCUGA') < 0 and sequence.find('CCUGAACCUGAA') < 0 and sequence.find('CUGAACCUGAAC') < 0 and sequence.find('UGAACCUGAACC') < 0:
                continue
            # print sequence
            match_count = match_count + 1
            for r in record:
                if r == '':
                    continue
                f.write(r + '\n')
    print 'total [%d] match [%d]' % (len(records), match_count)
if __name__ == '__main__':
    run_format  = '  python main.py input.file output.file'
    run_example = '  python main.py input.fastq output.fastq'
    print len(sys.argv)
    if len(sys.argv) != 3:
        print 'you need follow this run format'
        print run_format
        print run_example
        exit(1)
    sys.argv
    fun(sys.argv[1:])

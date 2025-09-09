# python3 split_csv.py simple_test_data.0.fwe.capacity822.csv
# python3 split_csv.py simple_test_data.1.niah60k.capacity822.csv
# python3 split_csv.py simple_test_data.2.qa.capacity774.csv
# python3 split_csv.py simple_test_data.3.ruler.capacity822.csv

import csv, os, sys
from pathlib import Path

outfile_name_cols = []
outfile_data_cols = []

outfiles = {}

if __name__ == "__main__":
    infile_name = sys.argv[1]


    outfile_name_cols = ["layer_id", "group_id"]
    outfile_data_cols = ["batch_id", "key_id", "num_blocks", "next_access_vtime", "hit_num_lru", "miss_num_lru", "hit_block_num_lru", "miss_block_num_lru"]
    
    with open(infile_name) as infile:
        infile_csv = csv.DictReader(infile, delimiter=',')
        for infile_csv_line in infile_csv:
            # Prepare output file name
            outfile_name = []
            for outfile_name_col in outfile_name_cols:
                outfile_name.append(outfile_name_col + "_" + infile_csv_line[outfile_name_col])
            outfile_name = "_".join(outfile_name) + ".csv"
            
            # Prepare output file handler
            outfile = outfiles.get(outfile_name)
            if outfile == None:
                outfile_directory = Path(os.path.basename(infile_name)).stem
                os.makedirs(outfile_directory, exist_ok=True)
                outfile = open(os.path.join(outfile_directory, outfile_name), "w", newline="")
                outfile = csv.DictWriter(outfile, outfile_data_cols, extrasaction="ignore")
                outfiles[outfile_name] = outfile
                print("Created " + os.path.join(outfile_directory, outfile_name))
                
                outfile.writeheader()
            
            # Write to output file
            if "next_access_vtime" in outfile_data_cols:
                infile_csv_line.update({"next_access_vtime": -1})
            outfile.writerow(infile_csv_line)

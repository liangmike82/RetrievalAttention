conda activate retroinfer
cd RetrievalAttention/library/retroinfer
pip install .

python -u simple_test.py --batch_size 1 --data_path mike/simple_test_data.0.fwe.json > simple_test_data.0.fwe.csv
python -u simple_test.py --batch_size 1 --data_path mike/simple_test_data.1.niah60k.json > simple_test_data.1.niah60k.csv
python -u simple_test.py --batch_size 1 --data_path mike/simple_test_data.2.qa.json > simple_test_data.2.qa.csv
python -u simple_test.py --batch_size 1 --data_path mike/simple_test_data.3.ruler.json > simple_test_data.3.ruler.csv

python3 split_csv.py simple_test_data.0.fwe.csv
python3 split_csv.py simple_test_data.1.niah60k.csv
python3 split_csv.py simple_test_data.2.qa.csv
python3 split_csv.py simple_test_data.3.ruler.csv

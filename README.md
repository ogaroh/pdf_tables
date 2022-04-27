## PDF Tables Extraction

### Folder structure
- The `replicate_tables.py` file contains the source code/script that runs the extraction & exportation
- The `source` folder contains the source PDF document
- The `tables` folder contains the extracted tables (CSV format)
- The `requirements.txt` text file contains a list of the required pip3 dependencies

### Environment setup
Python3 version - 3.8.10
Pip3 version - 22.0.4

- Run `python -m venv ./venv` to create your virtual environment
- Run `source ./venv/bin/activate` to activate the virtual environment
- Run `pip install -r requirements.txt` to install dependencies

### Executing the script
- Run `python replicate_tables.py` to run the script

### Notes
- The tables in the source PDF must have clearly defined borders for the script to work well. (Compare `data.pdf` [original source] and `data-new.pdf` [edited the tables to have clear borders]).
- All tables are exported into one Excel workbook but each table gets its own spreadsheet. You can define other export option as well 
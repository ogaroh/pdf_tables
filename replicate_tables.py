import camelot
import os

print("Extracting tables, please wait...")

# path of source pdf
source_file = "./source/data-new.pdf"

# save them in a folder - if the folder doesn't exist, create it
output_folder = "tables"
if not os.path.isdir(output_folder):
    os.mkdir(output_folder)

# extract all the tables in the PDF file
tables = camelot.read_pdf(source_file, pages="all")

#  export tables to Excel - same workbook but each table in its own worksheet
try:
    tables.export(os.path.join(output_folder, f"exported_tables.xlsx"), f='excel', compress=False)
except:
    print("Unable to convert to Excel")

# number of tables extracted
print("Total tables extracted:", tables.n)
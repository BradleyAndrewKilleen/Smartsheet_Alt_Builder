# Install the smartsheet sdk with the command: pip install smartsheet-python-sdk
import smartsheet
import logging
import os.path

# TODO: Set your API access token here, or leave as None and set as environment variable "SMARTSHEET_ACCESS_TOKEN"
access_token = "fmlnqd8eocscfclnadtmmaanh2"

_dir = os.path.dirname(os.path.abspath(__file__))
_download = os.path.dirname(os.path.abspath(__file__))
_wamWorkSheetID = "6814042909108100"
#_readyForAutomationColumnName = ""


# The API identifies columns by Id, but it's more convenient to refer to column names. Store a map here
column_map = {}


# Helper function to find cell in a row
def get_cell_by_column_name(row, column_name):
    column_id = column_map[column_name]
    return row.get_column(column_id)


# TODO: Replace the body of this function with your code
# This *example* looks for rows with a "Status" column marked "Complete" and sets the "Remaining" column to zero
#
# Return a new Row with updated cell values, else None to leave unchanged
def evaluate_row_checkbox(source_row, col_name):
    # Find the cell and value we want to evaluate
    status_cell = get_cell_by_column_name(source_row, col_name)
    status_value = status_cell.value
    #print(status_value)
    if status_value == True:
        return True

def get_column_value(source_row, col_name):
    # Find the cell and value we want to evaluate
    status_cell = get_cell_by_column_name(source_row, col_name)
    status_value = status_cell.display_value
    #print(status_value)
    return status_value

def convert_posix_to_unix_path(posix_path):
    unix_path = posix_path.replace(":","/")
    return non_posix_path







"""
        remaining_cell = get_cell_by_column_name(source_row, "Remaining")
        if remaining_cell.display_value != "0":  # Skip if already 0
            print("Need to update row #" + str(source_row.row_number))

            # Build new cell value
            new_cell = smart.models.Cell()
            new_cell.column_id = column_map["Remaining"]
            new_cell.value = 0

            # Build the row to update
            new_row = smart.models.Row()
            new_row.id = source_row.id
            new_row.cells.append(new_cell)

            return new_row
"""


#return None

print("Starting ...")

# Initialize client
smart = smartsheet.Smartsheet(access_token)
# Make sure we don't miss any error
smart.errors_as_exceptions(True)

##Brad Testing - getting entire sheet as csv, bnuild out helper function later to only get data from rows that are ready for automation
#smart.Sheets.get_sheet_as_csv("7546622595884932", _download, alternate_file_name=None)

# Log all calls
logging.basicConfig(filename='rwsheet.log', level=logging.INFO)

wamWorkSheet = smart.Sheets.get_sheet(_wamWorkSheetID)

for column in wamWorkSheet.columns:
    column_map[column.title] = column.id

rowsToProcess = []
sourcePathMap = {}
destPathMap = {}

for row in wamWorkSheet.rows:
    rowToProcess = evaluate_row_checkbox(row, "Ready_for_Automation")
    if rowToProcess is not None:
        rowsToProcess.append(rowToProcess)
        sourcePathMap[row] = get_column_value(row, "Donor_Path")
        destPathMap[row] = get_column_value(row, "Destination_Path")

if rowsToProcess


print(rowsToUpdate)


"""
# Import the sheet
result = smart.Sheets.import_xlsx_sheet(_dir + '/Sample Sheet.xlsx', header_row_index=0)

# Load entire sheet
sheet = smart.Sheets.get_sheet(result.data.id)


print("Loaded " + str(len(sheet.rows)) + " rows from sheet: " + sheet.name)

# Build column map for later reference - translates column names to column id
for column in sheet.columns:
    column_map[column.title] = column.id

# Accumulate rows needing update here
rowsToUpdate = []

for row in sheet.rows:
    rowToUpdate = evaluate_row_and_build_updates(row)
    if rowToUpdate is not None:
        rowsToUpdate.append(rowToUpdate)

# Finally, write updated cells back to Smartsheet
if rowsToUpdate:
    print("Writing " + str(len(rowsToUpdate)) + " rows back to sheet id " + str(sheet.id))
    result = smart.Sheets.update_rows(result.data.id, rowsToUpdate)
else:
    print("No updates required")
"""
#print("Done")

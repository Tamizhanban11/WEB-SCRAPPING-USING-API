# WEB-SCRAPPING-USING-API
## Overview
This project involves fetching data from an API, processing the JSON response, and saving it as an Excel file using PyExcel.

## Features
- Fetches data from an API
- Parses and processes JSON data
- Converts JSON data to Excel format
- Saves the data in an `.xlsx` file

## Technologies Used
- Python
- HTTP Client (for API requests)
- JSON (for data handling)
- PyExcel (for Excel file generation)

## Prerequisites
Ensure you have the following installed:
- Python 3.x
- Required libraries: Install using:
  ```sh
  pip install pyexcel pyexcel-xlsx
  ```

## Setup and Configuration
1. Clone this repository:
   ```sh
   git clone https://github.com/yourusername/webscraping-api-push.git
   ```
   ```sh
   cd webscraping-api-push
   ```
2. Update the script to match the required API URL and structure.

## Usage
Run the script using:
```sh
python scraper.py
```


# Assuming the JSON has a list of matches or events (modify as needed)
records = []
header = ["Key", "Value"]  # Adjust headers based on actual JSON structure

for key, value in json_data.items():
    records.append([key, str(value)])  # Convert values to strings to avoid issues

# Step 4: Save to Excel using pyexcel
sheet = [header] + records
pyexcel.save_as(array=sheet, dest_file_name="kabaddi_data.xlsx")

print("Data saved to kabaddi_data.xlsx")
```

## Troubleshooting
- **No data extracted?** Verify API response format and endpoint.
- **Permission issues?** Ensure the script has execution rights.
- **Excel file not generating?** Check `pyexcel` installation and dependencies.

## Contact
For any queries, contact: bablunivi2311@gmail.com



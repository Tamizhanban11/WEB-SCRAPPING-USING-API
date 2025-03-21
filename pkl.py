import http.client
import json
import pyexcel

# Step 1: Fetch data from the API
conn = http.client.HTTPSConnection("www.prokabaddi.com")
payload = ""
headers = {'User-Agent': "insomnia/11.0.0"}
conn.request("GET", "/datafeeds/live/json/1_147_tracker.json?=", payload, headers)

res = conn.getresponse()
data = res.read().decode("utf-8")

# Step 2: Convert JSON to dictionary
json_data = json.loads(data)

# Step 3: Extract relevant data
# Assuming the JSON has a list of matches or events (modify as needed)
records = []
header = ["Key", "Value"]  # Adjust headers based on actual JSON structure

for key, value in json_data.items():
    records.append([key, str(value)])  # Convert values to strings to avoid issues

# Step 4: Save to Excel using pyexcel
sheet = [header] + records
pyexcel.save_as(array=sheet, dest_file_name="kabaddi_data.xlsx")

print("Data saved to kabaddi_data.xlsx")

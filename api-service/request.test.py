import requests

# URL of the API endpoint
url = "http://localhost:8000/api/predicted"

# Path to the file you want to upload
file_path = "Cerulean.png"

# Open the file in binary mode and prepare the form data
files = {'file': open(file_path, 'rb')}
# Send POST request with file and form data
response = requests.post(url, files=files)

print(response)
# Close the file after uploading
files['file'].close()

# Check the response from the server
if response.status_code == 200:
    print("Upload successful")
    print(response.json())  # If the server returns JSON data
else:
    print("Upload failed", response.status_code, response.text)

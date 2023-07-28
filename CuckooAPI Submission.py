import os
import requests

REST_URL = "http://192.168.190.128:8090/tasks/create/file"
HEADERS = {"Authorization": "Bearer eTWmV4sdfas4KHHMXs7T0w"}
DIRECTORY_PATH = "/home/malware/Desktop/G601-700/"

for file_name in os.listdir(DIRECTORY_PATH):
    file_path = os.path.join(DIRECTORY_PATH, file_name)

    if os.path.isfile(file_path):
        with open(file_path, "rb") as sample:
            files = {"file": (file_name, sample)}
            r = requests.post(REST_URL, headers=HEADERS, files=files)

            if r.status_code == requests.codes.ok:
                try:
                    task_id = r.json()["task_id"]
                    if task_id is not None:
                        # Add your code for further processing or actions here
                        print("File submitted successfully:", file_name, "Task ID:", task_id)
                        # Perform additional operations using the task_id
                    else:
                        print("Error: 'task_id' not found in the response:", file_name)
                except KeyError:
                    print("Error: 'task_id' key not found in the JSON response:", file_name)
            else:
                print("Error submitting the file for analysis. Status code:", r.status_code, file_name)
    else:
        print("File not found:", file_name)

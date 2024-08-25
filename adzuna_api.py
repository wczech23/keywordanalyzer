import requests
import time
import json

# Application ID: dae149ff

# Application Key: 799c8be5793f94c88edd26c5ef7c766b

# requesting job and location information
app_id = input("Input App ID: ")
app_key = input("Input App Key: ")
job_description = input("Input Job Description: ")
country_code = input("Input Country Code (us,gb,de,ca,au,mx,fr,es): ")
region = input("Input Job City/Region: ")

with open("adzuna_doc_corpus.txt", "w", encoding='utf-8') as file:
    # generating url for api response
    # gathering description results from 200 job postings
    for i in range(1,11):
        url = f'http://api.adzuna.com:80/v1/api/jobs/{country_code}/search/{i}?app_id={app_id}&app_key={app_key}&results_per_page=20&what={job_description}&where={region}&content-type=application/json'
        response = requests.get(url)
        time.sleep(1)
        json_response = json.loads(response.content)
        if response.status_code == 200: # checking for a valid response from api call
            job_list = json_response["results"]
            for job in job_list:
                file.write(job["description"])
                file.write("\n")
        else:
            break

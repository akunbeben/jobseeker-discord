import requests
import json
from src import rupiah

def getKarir(keyword):
    keyword = keyword.replace(" ", "%20")
    url = 'https://www.karir.com/search?q={0}&sort_order=newest'.format(keyword)

    # params = {
    #     'q': keyword,
    #     'sort_order': "newest"
    # }

    response = requests.get(url, headers={
        "Accept": "application/json",
        "Content-Type": "application/json"
    })

    data = response.content

    listJobs = json.loads(data)["collection"]

    dataLength = len(listJobs)

    divider = round((dataLength / 3))

    indexStep = 0

    fullString = ["", "", ""]

    for index in range(indexStep, len(listJobs)):

        locationText = listJobs[index]["branch_location_names"][0]
        filteredString = locationText[:100]

        jobDict = {
            'jobPosition': listJobs[index]["job_position"],
            'jobSalary': listJobs[index]["salary_name_new"],
            'jobCompany': listJobs[index]["company"]["name"],
            'jobEmail': listJobs[index]["email"],
            'jobWebsite': listJobs[index]["company"]["website"],
            'jobLocation': filteredString,
            'jobExpiredDate': listJobs[index]["expires_at"],
            'jobId': listJobs[index]["id"],
        }

        strings = "Job Position: **{jobPosition}**\nJob Salary: {jobSalary}\nCompany Name: {jobCompany}\nCompany Email: {jobEmail}\nCompany Website: **<{jobWebsite}>**\nCompany Branch Location: {jobLocation}\nAvailable until: {jobExpiredDate}\nSource: <https://www.karir.com/opportunities/{jobId}/>\n------------------------------------------------------------------\n"

        indexStep += 1

        if((index + 1) <= divider):
            fullString[0] += strings.format(**jobDict)

        if(indexStep > divider):
            if(indexStep <= (divider * 2)):
                fullString[1] += strings.format(**jobDict)

        if(indexStep > (divider * 2) <= (dataLength - 1)):
            fullString[2] += strings.format(**jobDict)

    return [filtered for filtered in fullString if filtered.strip()]
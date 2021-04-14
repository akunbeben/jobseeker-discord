import requests
import json
import rupiah

def getKalibrr(keyword):
    url = 'https://www.kalibrr.id/kjs/job_board/search'

    params = {
        'limit': 10,
        'offset': 0,
        'sort_field': "activation_date",
        'sort_direction': "desc",
        'text': keyword,
        'country': "Indonesia"
    }

    response = requests.get(url, headers={
        "Accept": "application/json",
        "Content-Type": "application/json"
    }, params=params)

    data = response.content
    data = json.loads(data)["jobs"]

    total = len(data)
    divider = (total / 2)
    indexStep = 0

    outputString = ["", ""]

    salaryInString = ""
    isWfh = ""

    for index in range(indexStep, total):
        if (data[index]["maximum_salary"] == None):
            salaryInString = "Negotiatable"
        else:
            salaryInString = rupiah.format_rupiah(data[index]["base_salary"]) + " - " + rupiah.format_rupiah(data[index]["maximum_salary"])

        if (data[index]["is_work_from_home"] == False):
            isWfh = "On site"
        else:
            isWfh = "On site / Remote (Negotiatable)"

        companyCode = str(data[index]["company"]["code"])

        jobDictionary = {
            'jobName': data[index]["name"],
            'jobSalary': salaryInString,
            'companyName': data[index]["company_name"],
            'location': data[index]["google_location"]["address_components"]["city"],
            'jobType': data[index]["tenure"],
            'isWfh': isWfh,
            'jobDetail': "https://www.kalibrr.id/c/" + companyCode + "/jobs/" + str(data[index]["id"])
        }

        string = "```\n{jobName}\n\nSalary: {jobSalary}\n\nCompany Name: {companyName}\n\nLocation: {location}\n\nTenure: {jobType}\n\nRemote?: {isWfh}\n\n```**Details**: <{jobDetail}>\n\n"

        indexStep += 1

        if((index + 1) <= divider):
            outputString[0] += string.format(**jobDictionary)

        if(indexStep > (divider)):
            outputString[1] += string.format(**jobDictionary)

    return outputString
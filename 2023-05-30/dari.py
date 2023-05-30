import requests
import json

def project_details(project_id):
    headers = {
        "accept": "*/*",
        "accept-language": "en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7",
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
        "referer": "https://www.dari.ae/",
        "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzY29wZSI6WyJyZWFkIiwiY2FwdHVyZSIsInJlZ2lzdGVyIiwiZm9yZ290Iiwibm90aWZ5Il0sIm9yZ2FuaXphdGlvbiI6Imd1ZXN0LWNsaWVudGZLQnkiLCJleHAiOjE2ODU0NDI3MDAsImp0aSI6Ijk4NDA1YWJkLWQ2N2MtNDEwYi1iOWU3LWEyNDM1ZGM5NjFjZiIsImNsaWVudF9pZCI6Imd1ZXN0LWNsaWVudCJ9.fF7axMF9-F4khnwvWj4bEb113WZu5S_l-RC5L8WzfA6qHGuhYtqoj8zPIytxnbw0WYi1e-pl7lWfmwVfytx3ymwbqMFpAUjo4gRiUQdLfjjeuQK_-nMlKH-rmwHMg2XWxAxcJ2iqlR7WBXFCJ43BB_x8dG54DJmlDd3utLNgO5L-0cLm46zxup-5Z0SXKGSEyhP8F2J-d18LVd3BmC-G2Xn9iGZ7BOkf09jKG-4SxFOu_pNYFMPgmfGhXFvSqn4QJT4kvgVA_7xUvb9aC2nJ5uArpRT7fJvxBhOQ3VoLOjZw6pd60REZUTvYwcFulYCaAIUcSydPcNe_NnEQkofXjw"
    }
    url = f"https://api.dari.ae/property-service/api/v1/property/project/{project_id}"
    response = requests.get(url, headers=headers)
    data = json.loads(response.text)
    project = data['result']
    
    project_id = project['id']
    project_name = project['name']
    developer_name = project['developerName']
    developer_phn = project['developerPhoneNumber']
    district_name = project['districtEn']
    municipality = project['municipalityEn']
    percentage_of_completion = project['progressPercentage']
    property_type = project['projectPropertyType']
    project_details = {
            "Project ID": project_id,
            "Project Name": project_name,
            "Developer Name": developer_name,
            "Developer Phone": developer_phn,
            "District Name": district_name,
            "Municipality": municipality,
            "Percentage of Completion": percentage_of_completion,
            "Property Type": property_type
        }

    with open('project_details.json', 'a') as json_file:
        json.dump(project_details, json_file)
        json_file.write('\n')
    # print(f"Project ID: {project_id}")
    # print(f"Project Name: {project_name}")
    # print(f"Developer Name: {developer_name}")
    # print(f"Developer Phone: {developer_phn}")
    # print(f"District Name: {district_name}")
    # print(f"Municipality: {municipality}")
    # print(f"Percentage of Completion: {percentage_of_completion}")
    # print(f"Property Type: {property_type}")
    # print("----------------------------------------------")
    
    project_url = f"https://api.dari.ae/property-service/api/v1/property/project/{project_id}"
    print(f"Project URL: {project_url}")
    print("----------------------------------------------")

def projects_list(page=1):
    headers = {
        "accept": "*/*",
        "accept-language": "en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7",
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
        "referer": "https://www.dari.ae/",
        "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzY29wZSI6WyJyZWFkIiwiY2FwdHVyZSIsInJlZ2lzdGVyIiwiZm9yZ290Iiwibm90aWZ5Il0sIm9yZ2FuaXphdGlvbiI6Imd1ZXN0LWNsaWVudGZLQnkiLCJleHAiOjE2ODU0NDI3MDAsImp0aSI6Ijk4NDA1YWJkLWQ2N2MtNDEwYi1iOWU3LWEyNDM1ZGM5NjFjZiIsImNsaWVudF9pZCI6Imd1ZXN0LWNsaWVudCJ9.fF7axMF9-F4khnwvWj4bEb113WZu5S_l-RC5L8WzfA6qHGuhYtqoj8zPIytxnbw0WYi1e-pl7lWfmwVfytx3ymwbqMFpAUjo4gRiUQdLfjjeuQK_-nMlKH-rmwHMg2XWxAxcJ2iqlR7WBXFCJ43BB_x8dG54DJmlDd3utLNgO5L-0cLm46zxup-5Z0SXKGSEyhP8F2J-d18LVd3BmC-G2Xn9iGZ7BOkf09jKG-4SxFOu_pNYFMPgmfGhXFvSqn4QJT4kvgVA_7xUvb9aC2nJ5uArpRT7fJvxBhOQ3VoLOjZw6pd60REZUTvYwcFulYCaAIUcSydPcNe_NnEQkofXjw"
    }
    url = f"https://api.dari.ae/property-service/api/v1/property/project?page={page}&size=12"
    response = requests.get(url, headers=headers)
    data = json.loads(response.text)
    projects = data['result']['projects']
    for project in projects:
        project_id = project['id']
        project_name = project['name']
        district_name = project['districtEn']
        # print(f"Project ID: {project_id}")
        # print(f"Project Name: {project_name}")
        # print(f"District Name: {district_name}")
        # print("----------------------------------------------")
        
        project_details(project_id)

    if not projects:
        print("End of list")
        return
    projects_list(page + 1)

if __name__ == "__main__":
    projects_list()

    

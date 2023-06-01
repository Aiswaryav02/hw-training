import requests
import json

url = "https://api.dari.ae/authentication-service/oauth/token"
data = {
    'grant_type': 'client_credentials'
}
headers = {
        'Authorization': "Basic Z3Vlc3QtY2xpZW50Omd1ZXN0LXNlY3JldA==",
        # 'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryz9lkdjABnlHP6Q8x',
        "accept": "application/json, text/plain, */*",
        "accept-language": "en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7",
        "user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
        "referer":"https://www.dari.ae/",
    }
  
response = requests.post(url,data=data,headers=headers)  
print(response.status_code)
# print(response.text)
access_token = response.json().get('access_token')


def project_details(project_id):
    headers = {
        "accept": "*/*",
        "accept-language": "en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7",
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
        "referer": "https://www.dari.ae/",
        "Authorization": "Bearer "+access_token  
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
   
    
    project_url = f"https://api.dari.ae/property-service/api/v1/property/project/{project_id}"
    print(f"Project URL: {project_url}")
    print("----------------------------------------------")

def projects_list(page=1):
    headers = {
        "accept": "*/*",
        "accept-language": "en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7",
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
        "referer": "https://www.dari.ae/",
        "Authorization": "Bearer"+access_token  
         }
    url = f"https://api.dari.ae/property-service/api/v1/property/project?page={page}&size=12"
    response = requests.get(url, headers=headers)
    data = json.loads(response.text)
    projects = data['result']['projects']
    for project in projects:
        project_id = project['id']
        project_name = project['name']
        district_name = project['districtEn']
       
        project_details(project_id)

    if not projects:
        print("End of list")
        return
    projects_list(page + 1)

if __name__ == "__main__":
    projects_list()

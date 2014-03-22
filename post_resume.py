import requests
url = 'http://join.agiliq.com/api/resume/upload/?access_token=access_token'


data = {
	'first_name': 'Ashik',
    'last_name': 'Sujath',
    'projects_url': 'https://github.com/ashiksujath2',
    'code_url': 'https://github.com/ashiksujath2'
}

file = {'resume': open('ashik_resume.pdf', 'rb')}

r = requests.post(url, data=data, files=file)
print r.status_code
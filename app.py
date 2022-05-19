import requests
import time

while True:
    header = {
        "user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"
    }

    login_data = {
        'username' : 'JahanzaibBabar000',
        'password' : 'hello!earning'
    }
    with requests.Session() as s:
        url = "https://weshareabundance.com/members/#"
        url2 = "https://weshareabundance.com/members/auth/login"
        url3 = "https://weshareabundance.com/members/dashboard/loadDashboard"

        home_req = s.get(url, headers = header)

        login_req = s.post(url2, data = login_data, headers = header)
        print(login_req.content)
        
        
        dashboard_req = s.post(url3, headers = header)
        print(dashboard_req.content)
        time.sleep(12*60*60)

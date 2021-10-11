import requests
 
server_name = "http://vcm-21170.vm.duke.edu:5000/"
 
r = requests.post(server_name + "countries")
print(r.text)
 
request_json = {
                  "name": "Alex Thomason",
                  "net_id": "abt36",
                  "e-mail": "alexander.thomason@duke.edu"
}
r = requests.post(server_name + "student", json = request_json)
print(r.text)
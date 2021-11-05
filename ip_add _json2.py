ip_add = input("Enter your public ip address: ")
url = main_url + ip_add + "/latitude/"
lat = get(url).text

status = get(main_url + ip_add + '/').json
print(status)
print(lat) 
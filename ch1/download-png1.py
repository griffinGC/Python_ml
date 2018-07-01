import urllib.request

url = "http://uta.pw/shodou/img/28/214.png"
savename = "./ch1/test.png"

urllib.request.urlretrieve(url, savename)
print("save complete")
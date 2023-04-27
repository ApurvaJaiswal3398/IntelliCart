import requests

def activate(id=3, state=False, ip="http://192.168.1.12:5009"):
    if state:
        d={"status":"Cart Active", "use":"Used"}
    else:
        d={"status":"", "use":""}
    url = ip
    url += f"/activate_cart/{id}"
    return requests.post(url, data=d)


def add_product(scan=1,cid=3,ip="http://192.168.1.12:5009"):
    bcodes =["IUB635965D6","SDHV65447ER41","XGF54695469"]
    if scan == 1:d = {'barcode':bcodes[0]}
    if scan == 2:d = {'barcode':bcodes[1]}
    if scan == 3:d = {'barcode':bcodes[2]}
    d['cid'] = cid
    
    url = f'{ip}/scan'
    return requests.post(url, data=d)
import requests

filepath = 'test.png'
with open(filepath, 'rb') as fh:
    mydata = fh.read()
    response = requests.put('http://184.171.144.131/test.png',
            data=mydata,
            auth=('tester', 't3$T1nG'),
            headers={'content-type':'text/plain'},
            params={'file': filepath}
                )

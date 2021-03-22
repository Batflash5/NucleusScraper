#SERVER
import requests
from bs4 import BeautifulSoup
import json
from flask import Flask,request
import os

app = Flask(__name__)

@app.route('/post/', methods=['GET'])
def assignments():
    rollNo=request.args.get('rollno')
    password=request.args.get('password')
    print(rollNo,password)
    headers = {
        'authority': 'nucleus.amcspsgtech.in',
        'accept': 'application/json',
        'dnt': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.193 Safari/537.36',
        'content-type': 'application/json',
        'origin': 'https://nucleus.amcspsgtech.in',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://nucleus.amcspsgtech.in/login?path=%2F',
        'accept-language': 'en-IN,en;q=0.9',
    }

#     data = '{"rollNo":"{rollNo}","password":"{password}"}'

    rollpass='"rollNo":"{}","password":"{}"'.format(rollNo,password)
    data1 = '{}'.format(rollpass)
    data2="{%s}"%(data1)
    
    s=requests.Session();
    s.post('https://nucleus.amcspsgtech.in/oauth', headers=headers, data=data2)
    response=s.get("https://nucleus.amcspsgtech.in/assignments")
    content=response.content

    soup = BeautifulSoup(content, features="lxml")
    script=soup.find("script",attrs={"id":"__NEXT_DATA__"})
    assData=script.string

    js=json.loads(assData);
    
    return js

@app.route('/')
def index():
    return "<h1>Welcome to our server !!</h1>"
if __name__ == '__main__':
    app.run(threaded=True, port=5000)
from json import loads
import requests
import encryptor

URL = "https://echat.pythonanywhere.com"
#URL = 'http://127.0.0.1:5000'
e = encryptor.Encryption()
salt = e.encrypt_salt('3Chat')

def get_chat(name, password):
    u = str(URL + "/chat/read/" + name + "/" + password)
    response = requests.get(u)
    return response

def send_chat(name, password, content):
    u = str(URL + "/chat/add/" + name + "/" + password + "/" + content)
    response = requests.get(u)
    return response

def make_chat(name, password):
    u = str(URL + "/chat/make/" + name + "/" + password)
    response = requests.get(u)
    return response

print("""
    E-Chat v0.1 2019
""")
name = input('name > ')
password = input('password > ')
print('\n'* 100)

while True:
    cmd = input('> ')
    if "read" in cmd:
        resp = get_chat("test", "pass")
        resp = resp.content
        resp = resp.decode('utf-8')
        resp = e.decrypt_string(salt, resp)
        resp = loads(resp)
        ip = []
        msg = []
        time = []
        for i in resp['content']:
            ip.append(i['ip'])
            m = str(i['msg'])
            m = m.replace('_', " ")
            msg.append(m)
            time.append(i['time'])

        n = 0
        l = len(ip)
        while True:
            if n >= l:
                break
            else:
                print("\nip: " + ip[n] + "\nmessage: " + msg[n] + "\nTime: " + time[n])
                n += 1
    
    elif "write" in cmd:
        msg = input('Your Message > ')
        msg = msg.replace(' ', "_")
        send = send_chat(name, password, msg)
        send = send.content
        send = send.decode('utf-8')
        print(send)
    
    elif "make" in cmd:
        name = input('Name > ')
        password = input('Password > ')
        response = make_chat(name, password)
        response = response.content
        response = response.decode('utf-8')
        print(response)
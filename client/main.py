import socket
import psutil
import jsonpickle

def get_processes():
    process_list = []
    for proc in psutil.process_iter(['pid', 'name', 'status']):
        try:
            process_list.append({'pid': proc.info['pid'], 'name': proc.info['name'], 'status': proc.info['status']})
        except Exception:
            pass
    return process_list


IP = '127.0.0.1'
PORT = 4000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((IP, PORT))

process_list = get_processes()

data = jsonpickle.dumps(process_list)
client.sendall(data)

response = client.recv(1024)
print(f"Ответ от сервера: {response.decode('utf-8')}")
client.close()
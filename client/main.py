import socket
import psutil
import jsonpickle

def get_processes():
    process_list = []
    for proc in psutil.process_iter(['pid', 'name', 'status']):
        try:
            process_list.append({'pid': proc.info['pid'], 'name': proc.info['name'], 'status': proc.info['status']})
        except:
            continue
    return process_list


IP = '127.0.0.1'
PORT = 4000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((IP, PORT))

process_list = get_processes()

try:
    data = jsonpickle.encode(process_list)
    client.sendall(data.encode('utf-8'))
    print(f"Result: {len(process_list)} processes")

    response = client.recv(1024).decode('utf-8')
    print("Ответ сервера:", response)

except Exception:
    print("Error")
finally:
    client.close()
import socket
import jsonpickle

IP = '127.0.0.1'
PORT = 4000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((IP, PORT))
server.listen(2)
print("Сервер запущен...")


def process_client(client):
    try:
        data = client.recv(1024)
        if data:
            processes = jsonpickle.loads(data)
            print("Result:")
            for proc in processes:
                print(f"PID: {proc['pid']} | Name: {proc['name']} | Status: {proc['status']}")

            response = "Data received"
            client.sendall(response.encode('utf-8'))
    except Exception:
        print("Error")
    finally:
        client.close()

while True:
    client, addr = server.accept()
    print(f"Подключение от {addr}")
    process_client(client)

server.close()
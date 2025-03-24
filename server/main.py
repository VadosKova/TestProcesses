import socket
import jsonpickle

IP = '127.0.0.1'
PORT = 4000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((IP, PORT))
server.listen(2)
print("Сервер запущен...")

try:
    while True:
        conn, addr = server.accept()
        try:
            data = conn.recv(1000000).decode('utf-8')
            processes = jsonpickle.decode(data)

            print("PID | Name | Status")
            for proc in processes:
                print(f"{proc['pid']} | {proc['name']} | {proc['status']}")

            conn.send("OK".encode('utf-8'))
        except Exception:
            print("Error")
        finally:
            conn.close()
except KeyboardInterrupt:
    print("Server stopped")
finally:
    server.close()
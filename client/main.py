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
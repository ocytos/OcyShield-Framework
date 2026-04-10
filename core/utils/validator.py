import re
import socket

class Validator:
    @staticmethod
    def is_valid_ip(ip):
        pattern = re.compile(r"^(\d{1,3}\.){3}\d{1,3}$")
        if pattern.match(ip):
            return all(0 <= int(octet) <= 255 for octet in ip.split('.'))
        return False

    @staticmethod
    def is_valid_port(port):
        try:
            p = int(port)
            return 1 <= p <= 65535
        except ValueError:
            return False

    @staticmethod
    def get_local_ip():
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            s.connect(('8.8.8.8', 1)) 
            ip = s.getsockname()[0]
        except Exception:
            ip = '127.0.0.1'
        finally:
            s.close()
        return ip

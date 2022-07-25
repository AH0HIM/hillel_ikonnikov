import platform
import subprocess


def check_ping(ip_address: list, count: int):
    for ip_address in ip_address:
        if platform.system().lower() == "Windows":
            command = f'ping - n {count} {ip_address}'
        else:
            command = f'ping - n {count} {ip_address}'

        result = subprocess.run(command,
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE,
                                encoding='utf-8')

        if result.returncode == 0:
            print(result.stdout)
            print("OK")
        else:
            print("Something wrong")
            print(result.stdout + result.stderr)


check_ping(['www.google.com', 'facebook.com'], 7)



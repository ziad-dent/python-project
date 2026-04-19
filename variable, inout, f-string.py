print("=" * 80)
print("First Training: Variables".center(80))
print("=" * 80)

Server = input("choose your Server: ")
ip = input("Type your IP address: ")
port = int(input("Choose Your Port: "))
memory = float(input("choose your memory: "))
is_running =  True
cpu_threshold = 80.5

print("=" * 80)

print(f"Server: {Server}")
print(f"IP: {ip}")
print(f"Port: {port}")
print(f"Running: {is_running}")
print(f"CPU Threshold: {cpu_threshold}%\n")
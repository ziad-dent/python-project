print("=" * 80)
print("First Training: Variables".center(80))
print("=" * 80)


Server = input("choose your Server: ")
ip = input("Type your IP address: ")
port = int(input("Choose Your Port: "))
memory = float(input("choose your memory: "))

dict = {
"Server": Server,
"IP": ip,
"port": port,
"is_running": True,
"memory": f"{memory} GB",
"cpu_threshold": 80.5
}

print("=" * 80)

for key, value in dict.items():
    print(f"{key:15}: {value}")
print("=" * 46)
print("Password Authentication".center(46))
print("=" * 46)

print("Attempting to connect to server...".center(46))
password = 12345
attempts = 0
max_attempts = 5
connected = False
while attempts < max_attempts:
    userPassword = int(input("Type the Password: "))
    attempts += 1
    if userPassword == password:
        connected = True
        print("✅ connected successfully")
        break
    else:
        print(f"❌ Wrong Password\nAttempt {attempts}/{max_attempts}...")
if not connected:
    print("❌ Max attempts reached. Connection failed.")





print("=" * 46)
print("Variables".center(46))
print("=" * 46)

Server = input("choose your Server: ").strip()
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

print("=" * 46)

for key, value in dict.items():
    print(f"{key:15}: {value}")

print("=" * 46)
print("==>📋 OUR SERVERS<==".center(46))
print("=" * 46)

servers = ["web-01", "web-02", "db-01", "stage-01", "stage-db", "dev-01"]
for i in servers:
    print(f"{servers.index(i) + 1}. {i}")

print("=" * 46)
print("==>📋 OUR INFRASTRUCTURE<==".center(46))
print("=" * 46)

infrastructure = {
    "production": {
        "servers": ["web-01", "web-02", "db-01"],
        "region": "us-east-1",
        "active": True
    },
    "staging": {
        "servers": ["stage-01", "stage-db"],
        "region": "us-west-1",
        "active": True
    },
    "development": {
        "servers": ["dev-01"],
        "region": "us-west-2",
        "active": False
    }
}
for en, data in infrastructure.items():
    print(f"{en.upper():13}: {len(data["servers"])} servers in {data["region"]}")


print("=" * 46)
print("Depolyment Notification".center(46))
print("=" * 46)

app_info = {
"Application": "UserService",
"Version": "2.1.0",
"Environment": "production",
"Deployed by": "devops-team",
"Deployment Date": "19/4/2026",
"Success": True,
"Logs Location": "/var/log/app.log"
}
for key, value in app_info.items():
    if key == "Status":
        print(f"{key:18}: ✅ success") if value == True else print(f"{key:18}: ❌ FAILED")
    else:
        print(f"{key:18}: {value}")

print("=" * 46)
print("Server Status Check:".center(46))
print("=" * 46)

status = {
    "CPU usage": 50,
    "Memory usage": 85,
    "Disk usage": 65
}
for key, value in status.items():
    if value > 90:
        print(f"❌ {"CRITICAL":10}: {key} is critical!")
    elif value > 80:
        print(f"⚠️  {"WARNING":10}: {key} is high")
    elif value > 60:
        print(f"🟡 {"NOTICE":10}: {key} is moderate")
    else:
        print(f"✅ {"OK":10}: {key} is normal")



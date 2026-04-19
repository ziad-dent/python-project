print("=" * 46)
print("First Training: Variables".center(46))
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
print("2nd Training: List".center(46))
print("=" * 46)

servers = ["web-01", "web-02", "db-01", "stage-01", "stage-db", "dev-01"]
print("==>📋 OUR SERVERS<==".center(46))
for i in servers:
    print(f"{servers.index(i) + 1}. {i}")

print("=" * 46)
print("3rd Training: Dict".center(46))
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
print("==>📋 OUR INFRASTRUCTURE<==".center(46))
for en, data in infrastructure.items():
    print(f"{en.upper():13}: {len(data["servers"])} servers in {data["region"]}")


print("=" * 46)
print("5th Training".center(46))
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
print("Depolyment Notification".center(46))
for key, value in app_info.items():
    if key == "Status":
        print(f"{key:18}: ✅ success") if value == True else print(f"{key:18}: ❌ FAILED")
    else:
        print(f"{key:18}: {value}")

print("=" * 46)
print("6th Training".center(46))
print("=" * 46)

status = {
    "CPU usage": 50,
    "Memory usage": 85,
    "Disk usage": 65
}
print(f"Server Status Check:")
for key, value in status.items():
    if value > 90:
        print(f"❌ {"CRITICAL":10}: {key} is critical!")
    elif value > 80:
        print(f"⚠️  {"WARNING":10}: {key} is high")
    elif value > 60:
        print(f"🟡 {"NOTICE":10}: {key} is moderate")
    else:
        print(f"✅ {"OK":10}: {key} is normal")
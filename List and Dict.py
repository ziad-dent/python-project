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

import random, time, json

def collect_threat_data():
    threats = []
    for _ in range(10):
        threat = {
            "ip": f"192.168.1.{random.randint(1, 255)}",
            "threat_type": random.choice(["Malware", "Phishing", "Ransomware", "DoS", "Spyware"]),
            "severity": random.choice(["Low", "Medium", "High", "Critical"]),
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
        }
        threats.append(threat)
    return threats

def analyze_and_respond(threats):
    actions = []
    for t in threats:
        if t["severity"] == "Critical":
            action = f"IP {t['ip']} blocked immediately!"
        elif t["severity"] == "High":
            action = f"Alert sent for {t['ip']} (High threat)"
        elif t["severity"] == "Medium":
            action = f"Monitoring {t['ip']}"
        else:
            action = f"Logged low-severity threat {t['ip']}"
        actions.append({"ip": t["ip"], "action": action, "severity": t["severity"], "type": t["threat_type"], "time": t["timestamp"]})
    return actions


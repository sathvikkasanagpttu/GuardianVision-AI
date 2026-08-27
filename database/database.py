import json, os
DB_FILE = os.path.join(os.path.dirname(__file__), "../../incidents.json")

def load_incidents():
    if not os.path.exists(DB_FILE): return []
    with open(DB_FILE, encoding="utf-8") as f: return json.load(f)

def add_incident(item):
    data = load_incidents()
    data.insert(0, item)
    with open(DB_FILE, "w", encoding="utf-8") as f: json.dump(data, f, indent=2)
    return item

import yaml

with open(r"C:\Users\N.Janardhan Reddy\Downloads\docker-compose-basic-nrf.yaml") as f:
    data = yaml.safe_load(f)

for name, service in data["services"].items():
    ports = []
    seen = set()   # to track unique ports

    for env in service.get("environment", []):
        if "=" in env:
            key, val = env.split("=", 1)

            if key.endswith("_PORT") and val.isdigit():
                if val not in seen:   # keep order
                    ports.append(val)
                    seen.add(val)

    print(f"{name} -> Ports: {ports}")
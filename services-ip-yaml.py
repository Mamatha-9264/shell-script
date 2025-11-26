import yaml

with open(r"C:\Users\N.Janardhan Reddy\Downloads\docker-compose-basic-nrf.yaml") as f:
    data = yaml.safe_load(f)

for name, service in data["services"].items():
    ip = list(service.get("networks", {}).values())[0].get("ipv4_address")
    deps = service.get("depends_on", [])
    print(f"{name} -> IP: {ip}, Depends On: {deps}")

# import yaml

# yaml_path = r"C:\Users\N.Janardhan Reddy\Downloads\docker-compose-basic-nrf.yaml"

# def env_to_dict(env):
#     """Convert environment section to a dict.
#        env may be a list of "KEY=VAL" or a mapping {KEY: VAL}."""
#     result = {}
#     if isinstance(env, dict):
#         # direct mapping
#         for k, v in env.items():
#             result[str(k)] = str(v)
#     elif isinstance(env, list):
#         for item in env:
#             if isinstance(item, str) and "=" in item:
#                 k, v = item.split("=", 1) 
#                 result[k] = v
#             # skip non key=val list items
#     return result

# with open(yaml_path, "r", encoding="utf-8") as f:
#     data = yaml.safe_load(f)

# services = data.get("services", {})

# for svc_name, svc_data in services.items():
#     print(f"Service: {svc_name}")

#     # --- Environment / IP extraction ---
#     env_section = svc_data.get("environment", [])
#     env_dict = env_to_dict(env_section)

#     # collect all values for keys containing 'IP' (case-insensitive)
#     ips = []
#     for k, v in env_dict.items():
#         if "IP" in k.upper():
#             ips.append(v)

#     if ips:
#         print("  IP(s):", ", ".join(ips))
#     else:
#         print("  IP(s): None found")

#     # --- Dependencies ---
#     deps = svc_data.get("depends_on")
#     dep_list = []
#     if isinstance(deps, dict):
#         # depends_on: { serviceA: {...}, serviceB: {...} }  OR counts
#         dep_list = list(deps.keys())
#     elif isinstance(deps, list):
#         dep_list = deps

#     if dep_list:
#         print("  Depends on:", ", ".join(dep_list))
#     else:
#         print("  Depends on: None")

#     print("-" * 40)
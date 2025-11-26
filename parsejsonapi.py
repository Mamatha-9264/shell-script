# import yaml, json
# with open(r"C:\Users\N.Janardhan Reddy\OneDrive\Desktop\pythonhandson\JSON\library.json")as f:
#     data=json.load(f)
# yaml_out=yaml.dump(data, default_flow_style=False)
# print(yaml_out)   
import yaml, json
with open(r"C:\Users\N.Janardhan Reddy\Downloads\docker-compose-basic-nrf.yaml")as f:
    data=yaml.safe_load(f)
    json_out=json.dumps(data, indent=2)
    print(json_out)
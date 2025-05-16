import yaml

def get_config():
    with open("config.yaml") as f:
        cfg = yaml.safe_load(f)
        return cfg["db"]

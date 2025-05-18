import yaml
import os

def get_config():
    with open("config.yaml") as f:
        cfg = yaml.safe_load(f)
        db_cfg = cfg["db"]
        
    db_cfg['host'] = os.getenv('POSTGRES_HOST', db_cfg['host'])
    db_cfg['port'] = int(os.getenv('POSTGRES_PORT', db_cfg['port']))
    db_cfg['user'] = os.getenv('POSTGRES_USER', db_cfg['user'])
    db_cfg['password'] = os.getenv('POSTGRES_PASSWORD', db_cfg['password'])
    db_cfg['dbname'] = os.getenv('POSTGRES_DB', db_cfg['dbname'])

    return db_cfg

import yaml
import os

def get_config(test=False):
    with open("config.yaml") as f:
        cfg = yaml.safe_load(f)
        key = "test_db" if test else "db"
        db_cfg = cfg[key]
        
    db_cfg['host'] = os.getenv('POSTGRES_HOST', db_cfg['host'])
    db_cfg['port'] = int(os.getenv('POSTGRES_PORT', db_cfg['port']))
    db_cfg['user'] = os.getenv('POSTGRES_USER', db_cfg['user'])
    db_cfg['password'] = os.getenv('POSTGRES_PASSWORD', db_cfg['password'])
    db_cfg['dbname'] = os.getenv('POSTGRES_DB', db_cfg['dbname'])

    return db_cfg

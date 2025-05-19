import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="Load data and output summary by several queries")
    parser.add_argument('--init', required=True, help="Path to DB init SQL")
    parser.add_argument('--students', required=True, help="Path to students CSV")
    parser.add_argument('--rooms', required=True, help="Path to rooms CSV")
    parser.add_argument('--format', choices=['json', 'xml'], help="Output format", default="json")
    return parser.parse_args()
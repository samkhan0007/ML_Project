import argparse
import numpy as np
import pandas as pd
import os
import sys
from pathlib import Path

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

from src.logger import logging
import src.custom_exception as CustomException
from dataclasses import dataclass

DEFAULT_INPUT_CANDIDATES = [
    Path(ROOT_DIR, 'notebook', 'data', 'Stud.csv'),
    Path(ROOT_DIR, 'artifacts', 'Raw_Data.csv'),
    Path(ROOT_DIR, 'artifacts', 'raw_data.csv'),
]

@dataclass
class DataIngestionConfig():
    raw_data_path: str = os.path.join('artifacts', 'raw_data.csv')
    train_data_path: str = os.path.join('artifacts', 'train_data.csv')
    test_data_path: str = os.path.join('artifacts', 'test_data.csv')
    

def resolve_input_file(input_path: str | None = None) -> str:
    if input_path:
        candidate = Path(input_path)
        if not candidate.is_absolute():
            candidate = Path(ROOT_DIR) / candidate
        if candidate.is_file():
            return str(candidate)
        raise FileNotFoundError(f"Input file not found: {candidate}")

    for candidate in DEFAULT_INPUT_CANDIDATES:
        if candidate.is_file():
            if candidate == DEFAULT_INPUT_CANDIDATES[1] or candidate == DEFAULT_INPUT_CANDIDATES[2]:
                notebook_dir = Path(ROOT_DIR, 'notebook', 'data')
                notebook_dir.mkdir(parents=True, exist_ok=True)
                target = notebook_dir / 'Stud.csv'
                if not target.exists():
                    target.write_bytes(candidate.read_bytes())
                return str(target)
            return str(candidate)

    search_list = '\n'.join(str(p) for p in DEFAULT_INPUT_CANDIDATES)
    raise FileNotFoundError(
        "No input CSV file found. Checked:\n" + search_list +
        "\nUse --input <path> to specify a valid CSV file."
    )

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()
        
    def initiate_data_ingestion(self, source_path: str | None = None):
        logging.info("Data Ingestion method starts")
        try:
            source_path = resolve_input_file(source_path)
            df = pd.read_csv(source_path)
            logging.info("Dataset read as pandas dataframe")
            
            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path), exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path, index=False)
            logging.info("Raw data is saved")
            
            from sklearn.model_selection import train_test_split
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)
            
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)
            logging.info("Train and Test data is saved")
            
            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        except Exception as e:
            raise CustomException.CustomException(e, sys.exc_info())


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run data ingestion")
    parser.add_argument('--input', '-i', help='Path to input CSV file', default=None)
    args = parser.parse_args()

    ingestion = DataIngestion()
    train_path, test_path = ingestion.initiate_data_ingestion(args.input)
    print(f"Data ingestion completed:\n  train: {train_path}\n  test: {test_path}")

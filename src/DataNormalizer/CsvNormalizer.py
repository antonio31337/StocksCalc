import csv
from pathlib import Path

from src.DataPoints.StockDataPoint import StockDataPoint


class CsvNormalizer:
    def __init__(self, csv_file_path: Path):
        self.csv_file_path = csv_file_path

    def normalize(self) -> StockDataPoint:
        with open(self.csv_file_path, 'r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                if row[0] == 'Date':
                    continue
                yield StockDataPoint(str(row[0]), float(row[1]), float(row[2]), float(row[3]), float(row[4]),
                                     float(row[5]), int(row[6]))

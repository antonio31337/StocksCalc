from pathlib import Path

from DataNormalizer.CsvNormalizer import CsvNormalizer
from Insights.BiggestDrop import BiggestPossibleIntradayDrop, BiggestDropFromOpenToClose

if __name__ == '__main__':
    this_file_path = Path(__file__).resolve()
    # csv_path = this_file_path.parent / Path('./StocksData/NasdaqComposite/IXIC.csv')
    csv_path = this_file_path.parent / Path('./StocksData/Nasdaq100/NDX.csv')

    normalizer = CsvNormalizer(csv_path)

    insights = (BiggestPossibleIntradayDrop(normalizer), BiggestDropFromOpenToClose(normalizer))

    for insight_obj in insights:
        insight = insight_obj.get_insight()

        print(f"{insight_obj.__class__.__name__} {str(insight[0])} {str(insight[1])}")


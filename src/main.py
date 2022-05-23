from pathlib import Path

from DataNormalizer.CsvNormalizer import CsvNormalizer
from Insights.BiggestDrop import BiggestIntradayDrop, BiggestDropFromOpenToClose


def get_blue_string(string):
    return "\033[94m" + string + "\033[0m"


if __name__ == '__main__':
    this_file_path = Path(__file__).resolve()
    # csv_path = this_file_path.parent / Path('./StocksData/NasdaqComposite/IXIC.csv')
    csv_path = this_file_path.parent / Path('./StocksData/Nasdaq100/NDX.csv')
    # csv_path = this_file_path.parent / Path('./StocksData/SP500/GSPC.csv')

    normalizer = CsvNormalizer(csv_path)

    insights = (BiggestIntradayDrop(normalizer), BiggestDropFromOpenToClose(normalizer))

    for insight_obj in insights:
        insight = insight_obj.get_insight()

        print(f"{insight_obj.__class__.__name__} {str(insight[0])} {get_blue_string(str(insight[1]))}")


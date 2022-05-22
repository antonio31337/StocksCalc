from dataclasses import dataclass


@dataclass
class StockDataPoint:
    """
    Data class for stock data points.
    """
    date: str
    open: float
    high: float
    low: float
    close: float
    adj_close: float
    volume: int


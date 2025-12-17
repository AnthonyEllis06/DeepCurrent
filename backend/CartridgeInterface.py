from abc import ABC, abstractmethod
import pandas as pd

class IndicatorCartridge(ABC):
    @abstractmethod
    def name(self) -> str:
        """Return the name of the indicator."""
        pass
    @abstractmethod
    def run_analysis(self, df: pd.DataFrame, news_data: list = None) -> pd.DataFrame:
         """
        Run the indicator analysis on the provided DataFrame.
        
        STANDARD OUTPUT COLUMNS:
        To visualize features in the frontend, add these columns to your dataframe:
        - 'prediction': (float) A secondary line overlay (e.g. predicted price).
        - 'confidence': (float) 0.0 to 1.0 score indicating certainty.
        - 'signal':     (string) 'BUY', 'SELL', or 'HOLD'.
        
        Args:
            df (pd.DataFrame): RAW OHLCV DataFrame.
            news_data (list): Optional news data for context.
            
        Returns:
            pd.DataFrame: The DataFrame with new indicator columns added.
        """
        pass
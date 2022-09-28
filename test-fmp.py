from fmp_python.fmp import FMP
import pandas as pd

pd.option_context("display.max_rows", None)
pd.option_context("display.max_columns", None)

fmp = FMP(api_key='4a1561e536398a332282bbcab37a8720', output_format='pandas', write_to_file=True)
print(fmp.get_quote('AAL'))
print(fmp.get_historical_chart('5min','AAL'))
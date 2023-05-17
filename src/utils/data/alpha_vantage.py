"""
Tools for collecting, downloading, and handling data from Alpha Vantage
https://www.alphavantage.co/documentation/

TODO:
    -Write to cloud storage
    -Load from cloud storage
    -Update existing ticker histories
    -Logging
"""
import os
import re
import requests
import json
import yaml

from pandas import DataFrame

from .. import validate_path
from ..config import parse_config


###########
# GLOBALS #
###########

BASE_URL = "https://www.alphavantage.co/query?"
AV_FUNC_HEADERS = {
    'TIME_SERIES_DAILY_ADJUSTED': 'Time Series (Daily)'
}


#############
# FUNCTIONS #
#############

def get_api_key(config: dict) -> str:
    """
    Retrieves API key for Alpha Vantage

    Parameters
    ----------
    config : dict
        dict containing configuration parameters

    Returns
    -------
    str
        API key for Alpha Vantage

    Raises
    ------
    KeyError:
        Raised if the required config parameters are missing
    Exception:
        Catch-all
    """
    try:
        api_key_filepath = config['CORE_ARGS']['ENGINE_API_KEY']
        validate_path(api_key_filepath, extension='.yaml')
        with open(api_key_filepath, 'r') as file:
            api_key = yaml.safe_load(file)['API-KEY']
        file.close()
    except KeyError as error:
        print(f"{error=}, {type(error)=}")
        raise
    except Exception as error:
        print(f"Unexpected {error=}, {type(error)=}")
        raise
    return api_key


def make_api_request(av_function: str,
                     symbol: str,
                     output_size: str,
                     api_key: str
                    ) -> str:
    """
    Creates URL with the parameters for Alpha Vantage API

    Parameters
    ----------
    av_function : str
        alpha vantage data function to call
    symbol : str
        stock ticker
    output_size : str
        'compact' (last 100 data points) or 'full'
    api_key : str
        user specific key

    Returns
    -------
    str
        URL formatted to request data from the API
    """
    request_url = (f"{BASE_URL}"
                   f"function={av_function}"
                   f"&symbol={symbol}"
                   f"&outputsize={output_size}"
                   f"&apikey={api_key}"
                  )
    return request_url


def request_data(api_url:str,
                 datatype: str,
                 av_function: str
                ) -> DataFrame:
    """
    Sends request to the API for market data

    Parameters
    ----------
    api_url : str
        Complete URL for the API
    datatype : str
        file format (only json is supported for now)
    av_function : str
        Data stream from alpha vantage

    Returns
    -------
    DataFrame
        Contains returns with dates for the index

    Raises
    ------
    NotImplementedError:
        Only implemented for json
    RuntimeError:
        Raised when the API limits are hit
    """
    data_header = AV_FUNC_HEADERS[av_function]
    request = requests.get(api_url)
    if datatype == 'json':
        data = request.json()
    else:
        msg = f"File format {datatype} not implemented! Use json"
        raise NotImplementedError(msg)

    if data.get('Note'):
        msg = "API call limit reached!"
        raise RuntimeError(msg)
    if not data.get(data_header):
        msg = f"Expected {av_function} to have {data_header}!"

    data = DataFrame.from_dict(data[data_header], orient='index')
    return data


def clean_headers(market_data: DataFrame) -> DataFrame:
    """
    Removes the numeric+period+space from the beginning of the data headers

    Parameters
    ----------
    market_data : DataFrame
        time series data for an asset

    Returns
    -------
    DataFrame
        The same DataFrame but with clean headers
    """
    new_headers = [re.sub('[1-8]. ', '', col) for col in market_data.columns]
    new_headers = [re.sub(' ', '_', col) for col in new_headers]
    market_data.columns = new_headers
    return market_data

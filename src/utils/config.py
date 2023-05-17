"""
Tools for parsing configuration yaml files

TODO:
    -logging
"""
import sys
import yaml

#############
# FUNCTIONS #
#############

def parse_config(config_path: str) -> dict:
    """
    Read arguments from configuration file

    Parameters
    ----------
    config_path : str
        path to configuration file

    Returns
    -------
    dict
        dictionary containing configuration parameters

    Raises
    ------
    FileNotFoundError:
        Raised when file is not found at specified path
    yaml.reader.ReaderError:
        Raised when there is an issue parsing yaml with SafeReader
    """
    try:
        with open(config_path,
                  mode='r',
                  encoding='utf-8'
                 ) as config_file:
            config = yaml.safe_load(config_file)
        config_file.close()
    except FileNotFoundError:
        msg = f"{config_path} not found"
        raise FileNotFoundError(msg)
    except yaml.reader.ReaderError:
        msg = f"Error reading {config_path}"
        raise yaml.reader.ReaderError()
    except Exception as error:
        print(f"Unexpected {error=}, {type(error)=}")
        raise
    return config

import os

#############
# FUNCTIONS #
#############

def validate_path(path:str,
                  extension: str=None
                 ):
    """
    Ensure file exists at path and has expected extension

    Parameters
    ----------
    path : str
        filepath
    extension : str
        expected extension

    Raises
    ------
    FileNotFoundError:
       Raised if file was not found at specified path
    ValueError:
       Raised if the extension for the provided file does
       not match the expected extension
    """
    if not os.path.isfile(path):
        msg = f"{path} is not a file"
        raise FileNotFoundError(msg)
    ext = os.path.splitext(path)[-1]
    if extension and (ext != extension):
        msg = f"Expected file extension {extension} got {ext}"
        raise ValueError(msg)

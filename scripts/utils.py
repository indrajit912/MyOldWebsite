# Some utility functions
#
# Author: Indrajit Ghosh
#
# Date: Nov 15, 2023
#

import base64

def convert_zip_to_base64(file_path):
    """
    Convert a ZIP file to a base64-encoded data URL.

    Parameters:
    - file_path (str): The path to the ZIP file.

    Returns:
    str: The base64-encoded data URL for the ZIP file.
    """
    with open(file_path, "rb") as file:
        zip_data = file.read()
        base64_data = base64.b64encode(zip_data).decode('utf-8')
        return f"data:application/zip;base64,{base64_data}"



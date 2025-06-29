'''
Conversion logic for processing the numeric strings.
'''
def convert(former, latter):
    """
    Converts the two parts of a numeric string and checks their validity.
    Parameters:
    former (str): The first two characters of the numeric string.
    latter (str): The last two characters of the numeric string.
    Returns:
    str: A string indicating the result of the conversion:
         - "AMBIGUOUS" if both parts are between 1 and 12 inclusive.
         - "MMYY" if only the first part is between 1 and 12.
         - "YYMM" if only the second part is between 1 and 12.
         - "NA" if neither part meets the condition.
    """
    try:
        f = int(former)
        l = int(latter)
    except ValueError:
        return "NA"  # Return NA if conversion fails
    if 1 <= f <= 12 and 1 <= l <= 12:
        return "AMBIGUOUS"
    elif 1 <= f <= 12:
        return "MMYY"
    elif 1 <= l <= 12:
        return "YYMM"
    else:
        return "NA"
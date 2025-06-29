'''
Module containing the conversion logic for the numeric string.
'''
def convert_logic(former, latter):
    """Converts the former and latter numeric strings based on specified rules.
    Args:
        former (str): The first two characters of the numeric string.
        latter (str): The last two characters of the numeric string.
    Returns:
        str: The result based on the conversion logic.
    """
    # Treat "00" as invalid input for either part
    if former == "00" or latter == "00":
        return "NA"
    # Check if the inputs are valid numeric strings
    if not former.isdigit() or not latter.isdigit():
        return "NA"
    former_int = int(former)
    latter_int = int(latter)
    if 1 <= former_int <= 12 and 1 <= latter_int <= 12:
        return "AMBIGUOUS"
    elif not (1 <= former_int <= 12) and not (1 <= latter_int <= 12):
        return "NA"
    elif 1 <= former_int <= 12:
        return f"MMYY"
    elif 1 <= latter_int <= 12:
        return f"YYMM"
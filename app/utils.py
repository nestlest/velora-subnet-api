from datetime import datetime
from dateutil import parser

def normalize_datetime(input_date: str) -> str:
    try:
        # Use dateutil.parser to parse the input date
        parsed_date = parser.parse(input_date)
        # Format the date to the desired format
        normalized_date = parsed_date.strftime("%Y-%m-%d %H:%M:%S")
        return normalized_date
    except (ValueError, TypeError) as e:
        return f"Error parsing date: {e}"
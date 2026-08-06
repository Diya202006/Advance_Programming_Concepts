import re
from datetime import datetime
 
def extract_dates(text):
    patterns = [
        (r'\b\d{2}/\d{2}/\d{4}\b', "%d/%m/%Y"),         
        (r'\b\d{2}-\d{2}-\d{4}\b', "%m-%d-%Y"),           
        (r'\b\d{4}\.\d{2}\.\d{2}\b', "%Y.%m.%d"),        
        (r'\b[A-Za-z]+ \d{1,2}, \d{4}\b', "%B %d, %Y")   
    ]

    converted_dates = []

    for pattern, date_format in patterns:
        matches = re.findall(pattern, text)

        for date in matches:
            try:
                formatted = datetime.strptime(date, date_format)
                converted_dates.append(formatted.strftime("%Y-%m-%d"))
            except:
                pass

    return converted_dates
 
text = input("Enter a block of text:\n")

dates = extract_dates(text)

if dates:
    print("\nExtracted Dates (YYYY-MM-DD):")
    for date in dates:
        print(date)
else:
    print("No valid dates found.")
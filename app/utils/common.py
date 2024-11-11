import hashlib
import re, os
from app.utils.timestamp import *
import datetime

# URL and Path
STR_DOWNLOADS_FOLDER_PATH = os.path.join(os.path.expanduser('~'), 'Downloads')
STR_DOWNLOADS_TIMESTAMP_FOLDER_PATH = f"{STR_DOWNLOADS_FOLDER_PATH}\\{STR_DATESTAMP}"
DB_PATH = r'D:\Users\user\OneDrive - Chunghwa Telecom Co., Ltd\Work\99_共享檔案\三駐點\存控\存控.db'

def fn_log(str_log:str, str_filename:str = "") -> None:
    # Get the current date and time
    current_time = datetime.datetime.now()
    # Format the timestamp as a readable string
    timestamp = current_time.strftime("%Y-%m-%d %H:%M:%S")
    # Define the log message with the timestamp
    log_message = f"{timestamp} - {str_log}\n"
    # Open the log file in append mode ('a')
    if str_filename == "":
        str_filename = f"{STR_DATESTAMP}_log.txt"
    with open(f"{STR_DOWNLOADS_TIMESTAMP_FOLDER_PATH}\\{str_filename}", 'a') as log_file:
        # Write the log message to the file
        log_file.write(log_message)
    print(log_message)

def sanitize_string(value):
    # Remove non-printable and non-ASCII characters, except for common Chinese characters and punctuation
    if isinstance(value, str):
        return re.sub(r'[^\x20-\x7E\u4E00-\u9FFF\u3000-\u303F]', '', value)
    return value

def convert_roc_to_western(roc_date: str = "") -> str:
    if roc_date == "":
        return ""
    # Step 1: Eliminate all non-numeric characters except "/" and "-"
    cleaned_date = re.sub(r'[^\d/-]', '', roc_date)
    # Step 2: Extract the first 3 characters (ROC year) and convert to Western year
    roc_year = int(cleaned_date[:3])
    western_year = str(roc_year + 1911)
    # Step 3: Combine Western year with the remaining part of the ROC date string
    western_date = western_year + cleaned_date[3:]
    return western_date

def create_sha256_hash(data):
    # Create a SHA-256 hash object
    sha256_hash = hashlib.sha256()
    
    # Encode the input data to bytes (if it's a string) and update the hash object
    sha256_hash.update(data.encode('utf-8'))
    
    # Get the hexadecimal representation of the hash
    return sha256_hash.hexdigest()

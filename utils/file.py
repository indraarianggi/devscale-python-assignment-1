import os
from datetime import datetime
import pandas as pd

from constant import FILE_PATH

def load_csv():
    try:
        df = pd.read_csv(FILE_PATH, delimiter=",")
        return df.values.tolist()
    except FileNotFoundError:
        # Create empty CSV with headers if file doesn't exist
        df = pd.DataFrame(columns=["Name", "Occupation", "Bounty", "Poster", "Group", "Ship", "Jolly Roger"])
        df.to_csv(FILE_PATH, index=False)
        return df.values.tolist()
    

def add_to_csv(new_data):
    df = pd.read_csv(FILE_PATH)
    new_df = pd.DataFrame([new_data])
    df = pd.concat([df, new_df], ignore_index=True)
    df.to_csv(FILE_PATH, index=False)
    return df


def save_uploaded_file(uploaded_file, file_name, saved_path):
    # Generate unique filename using timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_extension = os.path.splitext(uploaded_file.name)[1]
    new_filename = f"{file_name}_{timestamp}{file_extension}"

    # Create directory if not exist
    os.makedirs(saved_path, exist_ok=True)
    
    # Save file to filesystem
    file_path = os.path.join(saved_path, new_filename)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    return file_path

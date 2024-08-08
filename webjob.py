import pandas as pd
import logging
from datetime import datetime
import os

# Configure logging
logging.basicConfig(
    # filename='D:\\Samples\\Python\\test webjob\\webjob.log',
    filename='/home/LogFiles/webjob.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def get_next_value(file_path):
    print('--- Fetching Value ---')

    if os.path.exists(file_path):
        try:
            # Load the existing CSV file
            df = pd.read_csv(file_path)
            logging.info('Loaded existing CSV file successfully.')
            
            if df.empty:
                return 1  # Start with 1 if the file is empty
            
            # Get the last value and increment it
            last_value = df['Value'].max()
            next_value = last_value + 1
            logging.info('Next value calculated: %d', next_value)
            return next_value
        
        except Exception as e:
            logging.error('Error reading CSV file: %s', e)
            return 1  # Fallback to 1 in case of any error
    
    else:
        logging.info('CSV file does not exist. Starting with value: 1')
        return 1

def insert_record(file_path):
    print('--- Inserting Record ---')

    try:
        # Determine the next value
        value = get_next_value(file_path)
        
        # Create a new DataFrame with the new record
        new_record = pd.DataFrame({'Timestamp': [datetime.now()], 'Value': [value]})
        
        if os.path.exists(file_path):
            # Load the existing CSV file
            df = pd.read_csv(file_path)
            logging.info('Loaded existing CSV file successfully.')
            # Append the new record
            df = pd.concat([df, new_record], ignore_index=True)
        else:
            # If the file does not exist, create a new DataFrame
            df = new_record
            logging.info('CSV  file not found. Created new file with columns: Timestamp, Value.')
        
        # Save the updated DataFrame back to Excel
        df.to_csv(file_path, index=False)
        logging.info('Saved updated CSV file successfully with value: %d', value)
    
    except Exception as e:
        logging.error('Error processing record: %s', e)

if __name__ == "__main__":
    print('--- WebJob Execution Started ---')
    # file_path = 'D:\\Samples\\Python\\test webjob\\data.csv'
    file_path = '/home/site/wwwroot/data.csv'
    insert_record(file_path)
    print('--- WebJob Execution Ended ---')

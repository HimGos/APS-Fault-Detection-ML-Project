import pymongo
import pandas as pd
import json

from sensor.config import mongo_client

DATA_FILE_PATH = "/config/workspace/aps_failure_training_set1.csv"
DATABASE_NAME = "aps"
COLLECTION_NAME = "sensor"


if __name__ == "__main__":
    df = pd.read_csv(DATA_FILE_PATH)
    print(f"Rows and columns: {df.shape}")

    # Convert Dataframe to json format so that we can dump these record in mongodb
    df.reset_index(drop=True, inplace=True)

    json_record = list(json.loads(df.T.to_json()).values())     #This single line of code can convert whole data into json
    print(json_record[0])

    # insert convereted json record to mongodb
    mongo_client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)
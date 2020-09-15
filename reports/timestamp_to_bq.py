from connectors._BigQuery import BigQuery
from datetime import datetime


path_to_bq = "../json_files/rta-moscow20.json"
bq = BigQuery(path_to_bq)
time_var = datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M:%S")
bq.insert_json("TimeTest", "TimeTest", [{"timestamp_var": time_var}])


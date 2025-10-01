# gretel AI implementation for synthetic data generation sample code:
import pandas as pd
from gretel_client import configure_session
from gretel_trainer.relational import RelationalData

# configuring api keys:
configure_session(api_key="your_api_key", cache="yes", validate=True)

# creating data requirements:
csv_dir = "csv/"
tables = [("patients", "Patient ID"), ("lab_results", "Lab Result ID"), ("treatments", "Treatment ID")]
foreign_keys = [("lab_results.Patient ID", "patients.Patient ID"), ("treatments.Patient ID", "patients.Patient ID")]

# relational data generation:
relational_data = RelationalData()
for table, pk in tables:
    relational_data.add_table(name=table, primary_key=pk, data=pd.read_csv(f"{csv_dir}/{table}.csv"))
for fk, ref in foreign_keys:
    relational_data.add_foreign_key(foreign_key=fk, referencing=ref)



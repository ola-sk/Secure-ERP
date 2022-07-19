""" Customer Relationship Management (CRM) module

Data table structure:
    - id (string)
    - name (string)
    - email (string)
    - subscribed (int): Is subscribed to the newsletter? 1: yes, 0: no
"""

from model import data_manager, util


CUSTOMER_DATAFILE = "./model/crm/crm.csv"
CUSTOMER_TABLE_HEADERS = ["id", "name", "email", "subscribed"]
CUSTOMER_TABLE_INDEXES = {"id": 0, "name": 1, "email": 2, "subscribed": 3}
SUBSCRIPTION_STATUSES = {"subscribed": "1", "not subscribed": "0"}


def read_customer_data(path, header):
    customer_table = data_manager.read_table_from_file(path)
    customer_table.insert(0, header)
    return customer_table

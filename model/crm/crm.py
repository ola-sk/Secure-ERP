""" Customer Relationship Management (CRM) module

Data table structure:
    - id (string)
    - name (string)
    - email (string)
    - subscribed (int): Is subscribed to the newsletter? 1: yes, 0: no
"""

from model import data_manager, util


DATAFILE = "./model/crm/crm.csv"
HEADERS = ["id", "name", "email", "subscribed"]
customer_table = data_manager.read_table_from_file(DATAFILE)
customer_table.insert(0, HEADERS)

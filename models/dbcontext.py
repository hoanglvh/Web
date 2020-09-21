from pyodbc import connect

class DbContext:
    def __init__(self):
        cn = "Driver={SQL Server};Database=BikeStore;Server=MAYTINH-0TVGJVH;Trusted_connection=yes"
        self.db = connect(cn)
    def __del__(self):
        self.db.close()
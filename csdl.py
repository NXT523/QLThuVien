import pyodbc

def get_connection():
    DATABASE_CONFIG = {
    'driver': '{ODBC Driver 17 for SQL Server}',
    'server': 'DESKTOP-FRMKLC0\\SQLEXPRESS',#đặt tên máy tính của bạn
    'database': 'QLThuVien',
    'trusted_connection': 'yes'
    }

    connection_string = (
    f"DRIVER={DATABASE_CONFIG['driver']};"
    f"SERVER={DATABASE_CONFIG['server']};"
    f"DATABASE={DATABASE_CONFIG['database']};"
    f"Trusted_Connection={DATABASE_CONFIG['trusted_connection']};"
    f"charset=utf8;"
    )
    return pyodbc.connect(connection_string)

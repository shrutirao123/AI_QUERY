import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",         
        database="retail_db" 
    )

def run_query(query):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute(query)
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    return results

def get_tables():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SHOW TABLES")
    rows = [r[0] for r in cursor.fetchall()]
    cursor.close()
    conn.close()
    return rows

def get_table_schema(table_name):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(f"DESCRIBE `{table_name}`")
    cols = cursor.fetchall()
    cursor.close()
    conn.close()

    schema_text = f"Table: {table_name}\nColumns:\n"
    for c in cols:
        schema_text += f"- {c[0]} ({c[1]})\n"

    # Special case: if table involves company_id → also add company_masters
    if table_name in ["purchase_documents", "sales_documents"]:
        schema_text += "\nTable: company_masters\nColumns:\n"
        schema_text += "- id (INT)\n"
        schema_text += "- name (VARCHAR)\n"

    return schema_text

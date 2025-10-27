import subprocess
import re

def extract_sql(text):
    """
    Extract only the first SQL SELECT statement.
    """
    matches = re.findall(r"(select.*?)(;|$)", text, re.I | re.S)
    if matches:
        sql = matches[0][0].strip()
        return sql.rstrip(";")
    return ""

def nl_to_sql(user_question, table_name, schema):
    prompt = f"""
You are a MySQL expert. Convert the following question into a valid SQL query.

Available Tables and Schemas:
{schema}

Target Table:
{table_name}

Question: {user_question}

Rules:
- Only use column names exactly as they appear in the schema. Do not invent new names.
- Do not create unnecessary aliases (like q or p) unless explicitly mentioned in schema.
- Only return a single SELECT query.
- For date filtering, use STR_TO_DATE if the column is varchar.
- Do not use DROP, UPDATE, DELETE, INSERT, CREATE.
- Add LIMIT 100 if no LIMIT is specified.
"""

    # Special rule only for purchase_documents & sales_documents
    if table_name in ["purchase_documents", "sales_documents"]:
        prompt += """
- If company_id exists in this table, join with company_masters ON <table>.company_id = company_masters.id
- Fetch company_masters.name as company_name
"""

    result = subprocess.run(
        ["ollama", "run", "llama3"],
        input=prompt.encode("utf-8"),
        capture_output=True
    )

    raw = result.stdout.decode("utf-8").strip()
    return extract_sql(raw)

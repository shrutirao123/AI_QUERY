from flask import Flask, request, render_template, redirect, url_for, session, flash , send_file
from db import run_query, get_tables, get_table_schema
from ollama_utils import nl_to_sql
import pandas as pd
import io
from datetime import datetime


app = Flask(__name__)
app.secret_key = "supersecret"  

TABLE_DISPLAY_NAMES = {
    "retail_sales_dataset": "🛒 Retail Sales Data",
    "purchase_data_exe": "💳 Purchase Data",
    "purchase_documents": "🛍️ Purchase Documents DIPL",
    "sales_documents": "💰 Sales Documents DIPL"

}

@app.route("/")
def home():
    tables = [t for t in get_tables() if t != "company_masters"] 
    selected = session.get("table", "retail_sales_dataset")  
    return render_template(
        "index.html",
        tables=tables,
        selected_table=selected,
        table_display=TABLE_DISPLAY_NAMES
    )


@app.route("/set_table", methods=["POST"])
def set_table():
    table = request.form.get("table_name")
    if table:
        session["table"] = table
        flash(f"✅ Table selected: {table}")
    return redirect(url_for("home"))

@app.route("/ask", methods=["POST"])
def ask():
    q = request.form.get("question")
    table = session.get("table", "retail_sales_dataset")

    if not q:
        return render_template(
            "index.html",
            error="Please enter a question",
            tables=get_tables(),
            selected_table=table,
            history=session.get("history", []),
            table_display=TABLE_DISPLAY_NAMES
        )

    schema = get_table_schema(table)
    sql = nl_to_sql(q, table, schema)

    try:
        rows = run_query(sql)

        session["last_rows"] = rows  

        if "history" not in session:
            session["history"] = []
        session["history"].insert(0, q)  
        session["history"] = session["history"][:5]  

        return render_template(
            "index.html",
            query=q, sql=sql, rows=rows,
            tables=get_tables(),
            selected_table=table,
            history=session["history"],
            table_display=TABLE_DISPLAY_NAMES
        )
    except Exception as e:
        return render_template(
            "index.html",
            query=q, sql=sql, error=str(e),
            tables=get_tables(),
            selected_table=table,
            history=session.get("history", []),
            table_display=TABLE_DISPLAY_NAMES
        )


@app.route("/export", methods=["POST"])
def export():
    rows = session.get("last_rows", [])
    if not rows:
        flash("⚠️ No data available to export!")
        return redirect(url_for("home"))

    df = pd.DataFrame(rows)
    output = io.BytesIO()
    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
        df.to_excel(writer, index=False, sheet_name="Results")

    output.seek(0)

    filename = f"results_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx"

    return send_file(
        output,
        as_attachment=True,
        download_name=filename,
        mimetype="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
    
@app.route("/clear_history", methods=["POST"])
def clear_history():
    session["history"] = []
    flash("🗑️ History cleared successfully!")
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)

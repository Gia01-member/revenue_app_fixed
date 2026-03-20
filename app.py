from flask import Flask, render_template, request

app = Flask(__name__)

@app.template_filter("currency")
def currency_filter(value):
    try:
        return f"¥{value:,.0f}"
    except:
        return "¥0"

def safe_div(a,b):
    return a/b if b else 0

@app.route("/", methods=["GET","POST"])
def index():
    inputs = {
        "traffic": 20000,
        "lead": 500,
        "mql": 200,
        "sql": 100,
        "opportunity": 30,
        "customer": 9,
        "unit_price": 50000,
        "ad_cost": 200000,
        "cost": 200000,
        "ltv": 80000,
    }

    if request.method == "POST":
        for k in inputs:
            inputs[k] = int(request.form.get(k, inputs[k]))

    traffic = inputs["traffic"]
    lead = inputs["lead"]
    mql = inputs["mql"]
    sql = inputs["sql"]
    opportunity = inputs["opportunity"]
    customer = inputs["customer"]

    lead_cvr = safe_div(lead, traffic)
    mql_rate = safe_div(mql, lead)
    sql_rate = safe_div(sql, mql)
    close_rate = safe_div(customer, opportunity)
    final_cvr = safe_div(customer, traffic)

    metrics = {
        "lead_cvr": lead_cvr,
        "mql_rate": mql_rate,
        "sql_rate": sql_rate,
        "close_rate": close_rate,
        "final_cvr": final_cvr,
        "revenue": customer * inputs["unit_price"],
        "cac": safe_div(inputs["ad_cost"], customer),
        "ltv": inputs["ltv"],
        "ltv_cac": safe_div(inputs["ltv"], safe_div(inputs["ad_cost"], customer)),
        "roas": safe_div(customer * inputs["unit_price"], inputs["ad_cost"]),
        "roi": safe_div((customer * inputs["unit_price"] - inputs["cost"]), inputs["cost"]),
        "ai_comment": {
            "title": "ボトルネック改善が必要です",
            "body": "最も低いCVを改善してください",
            "next_action": "施策を見直してください",
            "summary": "全体最適を意識してください"
        }
    }

    return render_template("index.html", inputs=inputs, metrics=metrics)

if __name__ == "__main__":
    app.run()

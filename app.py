from flask import Flask, render_template, request
from brain.intent_parser import parse_intent
from brain.rule_finder import find_best_rule
from brain.calculator import calculate_price
from brain.learner import save_learning

app = Flask(
    __name__,
    template_folder="ui/templates",
    static_folder="ui/static"
)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None

    if request.method == "POST":
        service = request.form.get("service")
        area = request.form.get("area")
        debris = request.form.get("debris") == "on"

        intent = parse_intent(service, area, debris)

        rule = find_best_rule(intent)

        if rule:
            calculated_price = calculate_price(intent, rule)

            result = {
                "service": service,
                "source_price": rule.get("base_price"),
                "calculated_price": calculated_price,
                "source": rule.get("source"),
                "confidence": rule.get("confidence", 0.7)
            }

            save_learning(intent, rule, calculated_price)

        else:
            result = {
                "service": service,
                "source_price": "Not found",
                "calculated_price": "Manual review required",
                "source": "N/A",
                "confidence": 0
            }

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)

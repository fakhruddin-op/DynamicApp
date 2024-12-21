from flask import Flask, render_template
import pandas as pd

# Initialize Flask app
app = Flask(__name__)

# Data for Table 1
table_1_data = {
    "Index #": [f"A{i}" for i in range(1, 21)],
    "Value": [41, 18, 21, 63, 2, 53, 5, 57, 60, 93, 28, 3, 90, 39, 80, 88, 49, 60, 26, 28]
}
table_1 = pd.DataFrame(table_1_data)

# Calculate Table 2
alpha = table_1.loc[4, "Value"] + table_1.loc[19, "Value"]  # A5 + A20
beta = table_1.loc[14, "Value"] / table_1.loc[6, "Value"]   # A15 / A7
charlie = table_1.loc[12, "Value"] * table_1.loc[11, "Value"]  # A13 * A12

table_2_data = {
    "Category": ["Alpha", "Beta", "Charlie"],
    "Value": [int(alpha), int(beta), int(charlie)]
}
table_2 = pd.DataFrame(table_2_data)

# Route to display tables
@app.route("/")
def home():
    return render_template("index.html", table_1=table_1, table_2=table_2)

# Run the app
if __name__ == "__main__":
    app.run(debug=True)

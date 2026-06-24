from flask import Flask, render_template_string
import json

app = Flask(__name__)

website_data = {
    "title": "Future AI Solutions",
    "hero": "Building Intelligent Software",
    "services": [
        "AI Development",
        "Machine Learning",
        "Automation",
        "Data Analytics"
    ]
}

template = """
<!DOCTYPE html>
<html>
<head>
    <title>{{ title }}</title>

    <style>
        body{
            font-family:Arial;
            margin:0;
            background:#111;
            color:white;
        }

        header{
            padding:80px;
            text-align:center;
            background:#222;
        }

        .services{
            padding:40px;
        }

        .card{
            background:#333;
            padding:20px;
            margin:10px;
            border-radius:10px;
        }
    </style>

</head>

<body>

<header>
    <h1>{{ hero }}</h1>
</header>

<div class="services">

    <h2>Services</h2>

    {% for service in services %}
        <div class="card">
            {{ service }}
        </div>
    {% endfor %}

</div>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(
        template,
        title=website_data["title"],
        hero=website_data["hero"],
        services=website_data["services"]
    )

if __name__ == "__main__":
    app.run(debug=True)
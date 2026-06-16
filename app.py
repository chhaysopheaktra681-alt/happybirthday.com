from flask import Flask, render_template, request

app = Flask(__name__)

# Color palette maps for each tier choice
COLOR_MAP = {
    # Top tier
    "pink":    {"a": "#ad1457", "b": "#e91e8c", "c": "#f8bbd9", "fr": "#f8bbd9"},
    "purple":  {"a": "#6a1b9a", "b": "#ab47bc", "c": "#e1bee7", "fr": "#e1bee7"},
    "red":     {"a": "#b71c1c", "b": "#ef5350", "c": "#ffcdd2", "fr": "#ffcdd2"},
    "teal":    {"a": "#006064", "b": "#26c6da", "c": "#b2ebf2", "fr": "#b2ebf2"},
    "gold":    {"a": "#f57f17", "b": "#ffca28", "c": "#fff9c4", "fr": "#fff9c4"},
    # Mid tier
    "blue":    {"a": "#0d47a1", "b": "#1976d2", "c": "#bbdefb", "fr": "#bbdefb"},
    "green":   {"a": "#1b5e20", "b": "#43a047", "c": "#c8e6c9", "fr": "#c8e6c9"},
    "indigo":  {"a": "#1a237e", "b": "#5c6bc0", "c": "#c5cae9", "fr": "#c5cae9"},
    "cyan":    {"a": "#006064", "b": "#00acc1", "c": "#b2ebf2", "fr": "#b2ebf2"},
    "rose":    {"a": "#880e4f", "b": "#e91e8c", "c": "#fce4ec", "fr": "#fce4ec"},
    # Bottom tier
    "orange":  {"a": "#bf360c", "b": "#f4511e", "c": "#ffccbc", "fr": "#ffccbc"},
    "amber":   {"a": "#e65100", "b": "#ffa000", "c": "#fff8e1", "fr": "#fff8e1"},
    "brown":   {"a": "#3e2723", "b": "#795548", "c": "#d7ccc8", "fr": "#d7ccc8"},
    "lime":    {"a": "#827717", "b": "#c0ca33", "c": "#f9fbe7", "fr": "#f9fbe7"},
    "magenta": {"a": "#880e4f", "b": "#e91e8c", "c": "#fce4ec", "fr": "#fce4ec"},
}


@app.route("/", methods=["GET"])
def form():
    return render_template("front/form.html")


@app.route("/cake", methods=["POST"])
def cake():
    name   = request.form.get("name", "Friend")
    age    = request.form.get("age", "?")
    gender = request.form.get("gender", "")

    color_top = request.form.get("color_top", "pink")
    color_mid = request.form.get("color_mid", "blue")
    color_bot = request.form.get("color_bot", "orange")

    top = COLOR_MAP.get(color_top, COLOR_MAP["pink"])
    mid = COLOR_MAP.get(color_mid, COLOR_MAP["blue"])
    bot = COLOR_MAP.get(color_bot, COLOR_MAP["orange"])

    return render_template(
        "front/cake.html",
        name=name,
        age=age,
        gender=gender,
        # Top tier colors
        color_top_a=top["a"],
        color_top_b=top["b"],
        color_top_c=top["c"],
        color_top_fr=top["fr"],
        # Mid tier colors
        color_mid_a=mid["a"],
        color_mid_b=mid["b"],
        color_mid_c=mid["c"],
        color_mid_fr=mid["fr"],
        # Bottom tier colors
        color_bot_a=bot["a"],
        color_bot_b=bot["b"],
        color_bot_c=bot["c"],
        color_bot_fr=bot["fr"],
    )


if __name__ == "__main__":
    app.run(debug=True)
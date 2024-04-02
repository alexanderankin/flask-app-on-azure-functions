import time

from flask import Flask, Response

# Always use relative import for custom module
from .package.module import MODULE_VALUE

app = Flask(__name__)

# @app.route("/")
# def index():
#     return (
#         "Try /hello/Chris for parameterized Flask route.\n"
#         "Try /module for module import guidance"
#     )

# @app.route("/hello/<name>", methods=['GET'])
# def hello(name: str):
#     return f"hello {name}"

# @app.route("/module")
# def module():
#     return f"loaded from FlaskApp.package.module = {MODULE_VALUE}"


def generate_numbers():
    """Generator function to yield numbers 1 to 10 with a 1-second delay."""
    for number in range(1, 11):
        yield f"data: {number}\n\n"
        time.sleep(1)

@app.route('/')
def index():
    """Serve the SSE stream."""
    return Response(generate_numbers(), content_type='text/event-stream')




if __name__ == "__main__":
    app.run()
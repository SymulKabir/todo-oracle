from flask import Flask, jsonify
from src.routes.main import home_route
from src.routes.api.main import api_route


app = Flask(
    __name__, 
    template_folder="src/templates",
    static_folder="src/static"
    )

app.register_blueprint(home_route)
app.register_blueprint(api_route, url_prefix="/api")



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9000, debug=True)

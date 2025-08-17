from flask import Flask, jsonify, request
from flask_cors import CORS
from api_interaction import electionMapGetter  # import your function

app = Flask(__name__)
CORS(app)  # allows frontend calls from other origins

@app.get("/elections")
def get_elections():
    zip_code = (request.args.get("zip") or "").strip()
    state    = (request.args.get("state") or "").strip()

    if not zip_code or not state:
        return jsonify({
            "error": "Missing required query params 'zip' and/or 'state'.",
            "received": request.args.to_dict(flat=True)
        }), 400

    location = f"{state} {zip_code}"  # or pass separately
    try:
        # CALL YOUR FUNCTION HERE
        results = electionMapGetter(location)  # or electionMapGetter(zip_code, state)
        return jsonify(results), 200
    except Exception as e:
        import traceback; traceback.print_exc()
        return jsonify({"error": str(e)}), 500
    

if __name__ == "__main__":
    app.run(debug=True, port=5000)
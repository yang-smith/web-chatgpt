from flask import jsonify, request
from app.utils.openai_utils import create_chat_completion
from app.api import api_bp

@api_bp.route("/api/chart", methods=["GET"])
# @login_required
def chart():
    try:
        content = request.args.get("content", "")
        response = create_chat_completion(content, "gpt-3.5-turbo")
        message = response['choices'][0]['message']['content']
        return jsonify(message=message)
    except Exception as err:
        return jsonify(error=str(err)), 404

@api_bp.route("/api/chartBeta", methods=["GET"])
def chartBeta():
    try:
        content = request.args.get("content", "")
        response = create_chat_completion(content, "gpt-4-0314")
        message = response['choices'][0]['message']['content']
        return jsonify(message=message)
    except Exception as err:
        return jsonify(error=str(err)), 404

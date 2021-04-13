from app import app
from flask import Flask, jsonify

@app.errorhandler(Exception)
def general_error(e):
    print('b')
    return {"errors": str(e), "messages": "Something went wrong"}
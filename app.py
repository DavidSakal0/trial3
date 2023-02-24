from flask import Flask, render_template, request, redirect, url_for


app = Flask (__name__)


@app. route("/restaurant", methods=["GET"])
def soccerfield():
    return render_template("restaurant.html")

import os

from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash
import pyodbc

# Configure application
app = Flask(__name__)
#Conexion de la base datoa SQLSERVER
cnxn_str=("Driver={SQL Server Native Client 11.0};"
          "Server=JUAN-4HUETE;"
          "Database=Colonial;"
          "UID=sa;"
          "PWD=ju160402;")
cnxn=pyodbc.connect(cnxn_str)
@app.route("/")
def hello_word():
    return render_template("lading.html")
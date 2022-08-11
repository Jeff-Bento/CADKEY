from flask import Blueprint
from flask import Flask, render_template, session, redirect


home_bp = Blueprint('home',__name__, template_folder='./templates',static_folder='./static', static_url_path='./static')


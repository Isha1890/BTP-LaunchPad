"""
Main Flask application for BTPLaunchpad backend.

This is the entry point for the Flask backend server. It initializes
the Flask app, configures the database, sets up CORS, and registers
the API routes.
"""

import os
from flask import Flask, jsonify
from flask_cors import CORS
from config import config
from models import db, Product
from routes import api

def create_app(config_name=None):
    """
    Application factory function to create and configure the Flask app.
    
    Args:
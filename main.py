import logging
import os
import threading
from flask import Flask, render_template_string
from bot import create_application
import config

# Create Flask app for webhook server
app = Flask(__name__)

@app.route('/')
def home():
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Nova Assistant Bot</title>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link href="https://cdn.replit.com/agent/bootstrap-agent-dark-theme.min.css" rel="stylesheet">
        <style>
            body {
                padding: 20px;
                min-height: 100vh;
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
            }
            .bot-card {
                max-width: 600px;
                width: 100%;
                padding: 20px;
            }
            .bot-logo {
                height: 80px;
                width: 80px;
                background-color: var(--bs-info);
                border-radius: 50%;
                display: flex;
                align-items: center;
                justify-content: center;
                margin: 0 auto 20px;
            }
        </style>
    </head>
    <body data-bs-theme="dark">
        <div class="container">
            <div class="card bot-card shadow-lg">

import config
from flask import Flask,render_template
from web3 import Web3

w3 = Web3(Web3.HTTPProvider(config.INFURA_URL))
app = Flask(__name__)


@app.route("/")
def index():
    return "<p>Ethereum Blockchain analyser</p>"

@app.route("/address/<addr>")
def address(addr):
    return render_template("address.html",addr=addr)

@app.route("/tx/<hash>")
def transaction(hash):
    return render_template("transaction.html",hash=hash)

@app.route("/block/<blocknr>")
def block(blocknr):
    return render_template("block.html",blocknr=blocknr)
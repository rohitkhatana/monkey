from flask import Flask, redirect, url_for
from flask import jsonify
from aliyunsdkcore.client import AcsClient
import json

from conformity.conformity import Conformity

app = Flask(__name__)

@app.route('/')
def home():
    return redirect(url_for('conformity'))

@app.route('/conformity')
def conformity():
    result = Conformity().perform()
    return jsonify(result)


if __name__ == '__main__':
    app.run()

import datetime
import hashlib
import json
from flask import Flask, jsonify

# Building Blockchain

class Blockchain:

    def __init__(self):
        self.chain = []
        self.create_block(proof = 1, previous_hash = '0')

# Mining our Blockchain

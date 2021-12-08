# -*- coding: utf-8 -*-
import csv
import os
import sys
from typing import List

sys.path.append(os.path.abspath(os.getcwd()))

from flask import Flask, jsonify
from flask.globals import request

app = Flask(__name__)

def path_databases(filename):
    return os.path.join(os.getcwd(), "data/" + filename)


@app.route("/", methods=["GET"])
def get_cards():
  cards = [];
  with open(path_databases('cards.csv'), newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
      cards.append(row)
  return jsonify({"data": cards}), 200


@app.route("/user", methods=["GET"])
def get_users():
  users = [];
  identify = str(request.args.get('id', default='', type=str))
  
  with open(path_databases('users.csv'), newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
      users.append(row)
  try:
    user = list(filter(lambda user: user["id"] == identify, users))[0]
    return jsonify({"data": user}), 200
  except:
    return jsonify({"data": "error"}), 405


@app.route("/", methods=["POST"])
def create_cards():
  data = request.get_json()
  cards = [];
  with open(path_databases('cards.csv'), newline='',  encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
      cards.append(row)
    csvfile.close()
  size = len(cards) + 1
  data = {**data, "id": str(size)}
  cards.append(data)
  with open(path_databases('cards.csv'), 'w', encoding='utf-8') as csvfile:
    file = csv.writer(csvfile)
    file.writerow(["id", "text", "date_create", "date_modified", "tags", "category"])
    for card in cards:
      file.writerow([card["id"], card["text"], card["date_create"], card["date_modified"], card["tags"], card["category"]])
    csvfile.close()
  return jsonify({"data":cards}), 200


@app.route("/", methods=["PUT"])
def update_cards():
  data = request.get_json()
  identify = str(request.args.get('id', default='', type=str))
  cards = [];
  with open(path_databases('cards.csv'), newline='',  encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
      cards.append(row)
  csvfile.close()
  for i, card in enumerate(cards):
    if card["id"] == identify:
      cards[i] = {**data, "id": identify}
      break
  with open(path_databases('cards.csv'), 'w', encoding='utf-8') as csvfile:
    file = csv.writer(csvfile)
    file.writerow(["id", "text", "date_create", "date_modified", "tags", "category"])
    for card in cards:
      file.writerow([card["id"], card["text"], card["date_create"], card["date_modified"], card["tags"], card["category"]])
    csvfile.close()
  return jsonify({"data":cards}), 200


@app.route("/", methods=["DELETE"])
def delete_cards():
  identify = str(request.args.get('id', default='', type=str))
  cards = [];
  with open(path_databases('cards.csv'), newline='',  encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
      cards.append(row)
  csvfile.close()
  for i, card in enumerate(cards):
    if card["id"] == identify:
      cards.remove(card)
      break
  with open(path_databases('cards.csv'), 'w', encoding='utf-8') as csvfile:
    file = csv.writer(csvfile)
    file.writerow(["id", "text", "date_create", "date_modified", "tags", "category"])
    for card in cards:
      file.writerow([card["id"], card["text"], card["date_create"], card["date_modified"], card["tags"], card["category"]])
    csvfile.close()
  return jsonify({"data":cards}), 200


@app.route("/detail", methods=["GET"])
def get_card_detail():
  cards = [];
  identify = str(request.args.get('id', default='', type=str))
  
  with open(path_databases('cards.csv'), newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
      cards.append(row)
  try:
    card = list(filter(lambda card: card["id"] == identify, cards))[0]
    return jsonify({"data": card}), 200
  except:
    return jsonify({"data": "error"}), 405


@app.after_request
def after_request(response):
    response.headers.set('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,Token,Avista-Token')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response


if __name__ == "__main__":
  app.run(debug=True, port=3000)

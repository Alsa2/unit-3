import sqlite3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from secure_password import encrypt_password, check_password

red = "\33[0;31m"
green = "\33[0;32m"
end = "\33[0m"

class WalletHandler():
    def __init__(self):
        self.connection = sqlite3.connect("Quizzes/Quizz-48/bitcoin_exchange.db")
        self.cursor = self.connection.cursor()
    
    def search(self, query):
        result = self.cursor.execute(query).fetchall()
        return result

    def run_save(self, query):
        self.cursor.execute(query)
        self.connection.commit()

    def close(self):
        self.connection.close()
    
    def get_ids(self):
        ids = self.search("SELECT id FROM ledger")
        return ids

handler = WalletHandler()
ids = handler.get_ids()
for id in ids:
    # id is the id of the transaction
    # get the transaction
    transaction = handler.search(f"SELECT * FROM ledger WHERE id={id[0]}")
    print(transaction)
    x = transaction[0]
    # get sender_id of the transaction
    sender_id = transaction[0][1]
    # get receiver_id of the transaction
    receiver_id = transaction[0][2]
    # get amount of the transaction
    amount = transaction[0][3]
    # get the hash of the transaction
    hash = transaction[0][4]

    unhashed = f"id {x},sender_id {sender_id},receiver_id {receiver_id},amount {amount}"
    if check_password(hash, unhashed):
        print(f"{green}Tx(id={x})Signature Matches{end}")
    else:
        print(f"{red}Tx(id={x})Error Signature{end}")


        




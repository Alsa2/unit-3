# Quizz 48
## Python code
```python
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker
from secure_password import check_password


red = "\33[0;31m"
green = "\33[0;32m"
end = "\33[0m"

Base = declarative_base()

class Ledger(Base):
    __tablename__ = 'ledger'
    id = Column(Integer, primary_key=True)
    sender_id = Column(Integer, nullable=False)
    receiver_id = Column(Integer, nullable=False)
    amount = Column(Integer, nullable=False)
    signature = Column(String, nullable=False)

    def __repr__(self):
        return f"id {self.id},sender_id {self.sender_id},receiver_id {self.receiver_id},amount {self.amount},hash={self.signature}"

engine = create_engine("sqlite:///Quizzes/Quizz-48/bitcoin_exchange.db")
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
rows = session.query(Ledger).all()
print(rows)
for row in rows:
    x = row.id
    sender_id = row.sender_id
    receiver_id = row.receiver_id
    amount = row.amount
    hash = row.signature
    unhashed = f"id {x},sender_id {sender_id},receiver_id {receiver_id},amount {amount}"
    if check_password(hash, unhashed):
        print(f"{green}Tx(id={x})Signature Matches{end}")
    else:
        print(f"{red}Tx(id={x})Error Signature{end}")
```
## Proof
![Proof](Images/quizz48-proof.png)
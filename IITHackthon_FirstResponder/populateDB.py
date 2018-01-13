#!/usr/bin/python

from werkzeug.security import generate_password_hash
from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError
import pandas as pd

def main():
    collection = MongoClient('127.0.0.1',27017)["IIThack"]["users"]
    df = pd.read_csv("userdata.csv")
    for index, row in df.iterrows():
        print row
        user = row['Username']
        image_url =row["Image_url"]
        Address =row['Address']
        Address_1 =row['Address_1']
        Address_2 =row['Address_2']
        active="true"
        validity="01/12/2016"
        email =row["Email"]
        email_1 =row["Email_1"]
        relationship_1=row['Relationship_1']
        relationship_2=row['Relationship_2']

        email_2 =row["Email_2"]
        phone=row["Mobile"]
        phone_1=row["Phone_1"]
        phone_2=row["Phone_2"]       
        name=row["Name"]
        name_1=row["Name_1"]
        name_2=row["Name_2"]
        pass_hash = generate_password_hash(row['Password'], method='pbkdf2:sha256')

    # Connect to the DB
    # collection = MongoClient('127.0.0.1',27017)["foreseeing"]["users"]

    # # Ask for data to store
    # user = "abhishek"
    # password = "abhishek"
    # role="manager"
    # domain="Neurologits"
    # name="Abhishek Bhardwaj"

    # email="abhishekbhardwaj13506@gmail.com"
    # validity="01/12/2016"
    # active="true"

    # pass_hash = generate_password_hash(password, method='pbkdf2:sha256')
    # phone=""
    # # Insert the user in the DB
        try:
            collection.insert({"Address":Address,"Address_1":Address_1,"Address_2":Address_2,"_id": user, "relationship_2":relationship_2,"relationship_1":relationship_1,"password": pass_hash,"email_2":email_2,"email_1":email_1,
                "name":name,"name_1":name_1,"name_2":name_2,"email":email,'phone':phone,'phone_1':phone_1,'phone_2':phone_2,'image_url':image_url})
            print "User created."
        except DuplicateKeyError:
            print "User already present in DB."


if __name__ == '__main__':
    main()

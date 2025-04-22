# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, USER, PASS):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections.
        # This is hard-wired to use the aac database, the 
        # animals collection, and the aac user.
        # Definitions of the connection string variables are
        # unique to the individual Apporto environment.
        #
        # You must edit the connection variables below to reflect
        # your own instance of MongoDB!
        #
        # Connection Variables
        
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 33060
        DB = 'AAC'
        COL = 'animals'
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]
        print("Connected successfully.")

# Complete this create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            created = self.database.animals.insert_one(data)  # data should be dictionary            
            return True;
        else:
            raise Exception("Nothing to save, because data parameter is empty")
        return False;

# Create method to implement the R in CRUD.
    def read(self, data):
        if data is not None:
            readResult = self.database.animals.find(data)  # data should be dictionary            
            results = list(readResult) #convert cursor results to list
            print("Success");
            return results;
        else:
            raise Exception("Nothing to read, because data parameter is empty.")
            
# Update method to implement the U in CRUD.
    def update(self, data, update_data):
        if data is not None and update_data is not None:
            try:
                # read before update
                docs = self.read(data)
                
                if len(docs) > 1 :
                
                    result = self.database.animals.udpdate_many(data, {"$set": update_data})
                elif len(docs) == 1:
                    
                
                    result = self.database.animals.update_one(data, {"$set": update_data})
                else:
                    return {"message": "No matching documents found to update."}
                
                if result.matched_count > 0:
                    return {"Success": True, "modified_count": result.modified_count}
                else:
                    return {"message": "No matching documents found to update."}
            except Exception as e:
                raise Exception(f"Error updating data: {str(e)}")
        else:
            raise Exception("Query or update_data is empty.")
            
# Delete method to implement the D in CRUD
    def delete(self, data):
        if data is not None:
            try:
                # Delete the matching document(s)
                result = self.database.animals.delete_one(data)
                
                if result.deleted_count > 0:
                    return {"success": True, "deleted_count": result.deleted_count}
                else:
                    return {"message": "No matching documents found to delete."}
            except Exception as e:
                raise Exception(f"Error deleting data: {str(e)}")
        else:
            raise Exception("Query is empty.")
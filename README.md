# CRUD MongoDB Module written in Python

## G. Salvare
This open-source program provides read and write CRUD functionality to G. Salvare database. 

## Motivation
##This specific program was created for G. Salvare but can be modified for any database connecting to Mongo DB. G. Salvare is an international rescue-animal training company. This program helps provide data to a nonprofit near Austin, Texas who will partner with G. Salvare to help categorize and identify available dogs to place successfully into training.

## Getting Started
To get a local copy up and running, follow these example steps below.
Please note: Credentials seen are for example usage. Though they are expired, they are not permitting for usage in any way.

## Installation
The tools you will need include: 
•	VirtualLab (Apporto) *Note: This was previously configured via [Redacted]
•	Linux Terminal *Note: This was previously configured via [Redacted]
•	MongoDB *Note: Previously configured via SNHU
o	To install: https://www.mongodb.com/docs/manual/installation/
	Once Mongo DB is installed, follow steps from the documentation to start the MongoDB shell
	To see all databases type:
•	show dbs
	Here you should see a database called “admin”. To use the admin database (this will ensure you have privileges to create a new user) type:
•	use admin
	To create the user type:
![image](https://github.com/user-attachments/assets/e254f857-792d-40c4-87d3-6f6ac9a7ac10)

 
NOTE: This above example uses example values. The role will enable read & write permissions, this value SHOULD NOT be changed. The user, pwd, and db can be any values. Also be sure to double check the command formatting.
•	Jupyter Notebook
o	https://jupyter.org/install
•	Spyder IDE
o	https://docs.spyder-ide.org/current/installation.html


## Purpose of CRUD Python Module
The purpose of the CRUD Python module is to provide an easy way to interact with MongoDB using Python code to perform basic Create, Read, Update and Delete (CRUD) operations on a collection in the database. This example uses the “animals” collection. These operations help to manage the data in an efficient way.

### Create: Adds a new document to the specified collection
### Read: Retrieves or “gets” a document or list of documents based upon filtering
### Update: Modifies a document based on specified filter
### Delete: Removes document(s) from the database collection

## Using the CRUD Module
In order to utilize the CRUD Module, an instance of MongoDB should be run with the Python “pymongo” driver. 
Once the module is set up, the user can create an instance of the CRUD class (in this example, the class name is AnimalShelter.py). See section below for more details.
More Details On Usage for Create and Read
To start, open Spyder IDE and create a new Python file. For example, the file name could be something like:
 
Note: The filename must end with .py

Insert the following text under Code Example into the file. 
Note: Be sure to change the following variables to the variables you will use for your database:

```
USER = ‘yourUsername’
PASS = ‘yourPassword’
HOST = 'nv-desktop-services.apporto.com'
PORT = 12345   **enter desired port **
DB = 'AAC'
COL = 'animals'
```

You can also check your individual mongo environmental variables using the following command:
```
printenv grep | -i mongo
```


Code Example (this will act as the CRUD module)
```
# -*- coding: utf-8 -*-
"""
# This script will help read and write documents from Mongo DB
"""

from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, USER, PASS):
        # Initializing the MongoClient. This helps to access the MongoDB databases and collections.
        # This is hard-wired to use the aac database, the animals collection, and the specified user.
# Note: USER and PASS are parameters above. These will likely be from your environment 
# variables.
        # Definitions of the connection string variables are
        # unique to the individual Apporto environment.
        #
        # You must edit the connection variables below to reflect
        # your own instance of MongoDB!
        #
        # Connection Variables
        
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 12345
        DB = 'AAC'
        COL = 'animals'
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]
        print("Connected successfully.")

# Create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            self.database.animals.insert_one(data)  # data should be dictionary            
            return True;
        else:
            raise Exception("Nothing to save, because data parameter is empty")
        return False;

# Method to implement the R in CRUD.
    def read(self, data):
        if data is not None:
            readResult = self.database.animals.find(data)  # data should be dictionary            
            return readResult;
        else:
            raise Exception("Nothing to read, because data parameter is empty.")
```
***********STOP CODING HERE**************
Test your script for read and write. Ensure they are working correctly. See more details below.
Once you have confirmed the functionality of both, add the following code for update and delete
*******ADD THIS CODE FOR UPDATE & DELETE TO THE CRUD MODULE AFTER CONFIRMING FUNCTIONALITY FOR CREATE AND READ***********************

### Update method to implement the U in CRUD.
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
            
### Delete method to implement the D in CRUD
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

***************************END OF CODE***********************

### NOTE
In the update function, read before writing (or updating is called to ensure if an object has been recently updated, we are first retrieving the updated object and the performing an update. If this code is utilized for large scale projects, consider adding threading. This aspect will not be discussed here as it is out of scope.         

## Tests for Create and Read
To create a python testing script in Jupyter Notebook:

1.	Open Jupyter Notebook, this will start a kernel instance browser session.
2.	Create a new Python3 (ipkernel) file in the same folder where you saved your .py file from above. If not, you will need to specify the filepath to the CRUD module you created with the .py file later on when specifying imports.
 ![image](https://github.com/user-attachments/assets/258bc7c6-da02-4c30-afd5-3aef2aa8a56c)

3.	Click File -> Save as… -> Documents/Assignment4/testScriptfile (Note: No need to put a file extension here, only use the name. By default this file will be saved as a .ipynb file)
![image](https://github.com/user-attachments/assets/7f63e383-e2ea-4bf4-bb3a-62fd8b9f3c4e)

 
	After clicking save, you will see in the browser the filename extension such as:
![image](https://github.com/user-attachments/assets/d7f92e4b-b0de-4ff6-8ad1-b06b398b459a)

   
Tests for UPDATE & DELETE can be found in the Proof of Functionality Section
Note: If you update and object attribute, you may need to update your script to perform deletes or other updates.
####	TDLR (for testing script):

Copy and paste the following text:
```
from animalShelterModule import AnimalShelter

CRUD = AnimalShelter("userName", "password")

created = CRUD.create({"animal_type": "Dog"})

print (created)

readResult = CRUD.read({"animal_type": "Dog"})

#convert cursor to a list
readResultList = list(readResult)

print(readResultList)

#loop through documents and print results
for r in readResultList:
    print(r)
```
********************************************************************************************************************************************************
Example test script with explanations

#importing the CRUD MODULE and the class name from the module. 
# here the class name is Animal Shelter.

 ![image](https://github.com/user-attachments/assets/5bdd9ccf-ae55-46a2-8904-0f11b7d4fccf)


The import will follow the structure:
From <filename> import <className>
```
from animalShelterModule import AnimalShelter
```
#Instantiate the CRUD object with the required arguments. Note self is not required as it is #part of the user session. 

```
CRUD = AnimalShelter("username", "password")
```

#write to the database, note this will return True if successful, false otherwise
```
created = CRUD.create({"animal_type": "Dog"})
#Prints the object that was written
print (created)
```

### Read from the database
#### Note this will return an empty list []  if no results are a match
#### If this search term is broad, many results may be returned
```
readResult = CRUD.read({"animal_type": "Dog"})
```
#### Note: Mongo DB will return results using Mongo Cursor
##### This will help convert results to view an empty list easily
```
# convert cursor to a list
readResultList = list(readResult)
```
# print the result
```
print(readResultList)
```

# loop through documents and print results
```
for r in readResultList:
    print(r)
```
####	To run the script, click “Run”. If file changes are made to the .py file (from Code Example above), you will need to restart the kernel for the browser to pick up the changes. This can be done by clicking the button that looks like the fast forward symbol as shown below.

![image](https://github.com/user-attachments/assets/64001f74-c48b-4edc-8bb4-fc098f289596)

 
####	If configured properly, the output should show:

 ![image](https://github.com/user-attachments/assets/1efc73de-ccb3-4071-b435-e3ad27543f28)

## Proof of Functionality
1.	MongoDB import execution

 ![image](https://github.com/user-attachments/assets/9d8e9bbe-e245-4e9f-bc91-b9acc9a44389)

2.	User authentication execution

 ![image](https://github.com/user-attachments/assets/6e5bc08b-fa5e-4006-b05a-9ef438484d7d)

3.	CRUD functionality test execution
a.	CREATE & READ

 ![image](https://github.com/user-attachments/assets/425766ff-ae74-48bc-969f-eb0b8632c8cb)

b.	UPDATE

 ![image](https://github.com/user-attachments/assets/783eeb7c-d286-41b8-aa42-850ef5a85b83)

Note: 

![image](https://github.com/user-attachments/assets/47f69490-d0ac-47ec-9d08-e17e9584529e)

 
c.	DELETE

![image](https://github.com/user-attachments/assets/aec0406a-7cd2-4d1e-9a71-cca740328237)

 
Note:


![image](https://github.com/user-attachments/assets/c597e5c9-0996-4a95-a046-1a1a07f18ffc)



###	Additional Screenshots showing functionality (Happy Path):
	 

 ![image](https://github.com/user-attachments/assets/59b039c2-2fec-4af4-a5af-9f3e6c16f0e1)

 ![image](https://github.com/user-attachments/assets/5fbb6fca-51e6-4fee-b1a3-a27202595e35)


###	Additional Screenshots showing functionality (Unhappy Path):
1.	Read (A.k.a. Search) For Document Not Existing, Connects to database, but output is empty list

  ![image](https://github.com/user-attachments/assets/510e178b-1db3-4587-b3f1-49303ea5f03d)


2.	Create Document with invalid syntax
Note: Connected to Database, but create does not return true

 ![image](https://github.com/user-attachments/assets/c0bae049-41c2-4485-9254-f1d6adf3cae3)

3.	Update document that doesn’t exist returns message for no matching document
 

![image](https://github.com/user-attachments/assets/5fff70da-2e8b-48e7-bfce-c05fafb43981)

4.	Update document with incorrect data field on read before writing

 ![image](https://github.com/user-attachments/assets/cafa1366-d7df-4214-8308-565a2da77a5b)

5.	Delete document doesn’t exist returns no matching document message

 ![image](https://github.com/user-attachments/assets/43f77c59-5e8c-44d0-9b25-8241f7a5654e)

6.	Wrong username

 ![image](https://github.com/user-attachments/assets/608ed0ee-f29a-4746-a17f-81fa6538edde)

7.	Wrong Password

 ![image](https://github.com/user-attachments/assets/32012f65-9150-420b-9542-afb662ffa3c4)

	
## Frontend Usage
1.	Grazioso Salvare logo links to SNHU homepage

 ![image](https://github.com/user-attachments/assets/9f80ebca-3520-4166-a6de-856e14bd3113)


 ![image](https://github.com/user-attachments/assets/db8cdda3-2b1f-481b-a063-0fe94e0384b7)

2.	Present unique identifier in header to credit dashboard creator

 ![image](https://github.com/user-attachments/assets/27d26093-b0f5-435b-b451-3927b45cd245)

3.	Filter options to filter results for desired dog rescue type (include additional filter for reset)

 ![image](https://github.com/user-attachments/assets/43d4a1d3-abe2-4805-80e9-4bcdf9fb92f9)

a.	Water

![image](https://github.com/user-attachments/assets/36d66a72-2a57-4b87-89c5-b6f508f124d9)

 
(**Note there a few dog types for water rescue training, but the only types present in the database which are ‘Intact Female’ and meet the desired age requirements are Labrador Retriever Mix)
b.	Mountain

 ![image](https://github.com/user-attachments/assets/0d597bda-699f-4a91-89b9-2c310832f6b4)

c.	Disaster

 ![image](https://github.com/user-attachments/assets/f37982b7-a28b-41f3-b306-06a96a2c5c0b)

d.	Reset filters

 ![image](https://github.com/user-attachments/assets/e4856ae9-8ad7-45b8-b7a9-c62f4c1f98b9)

4.	Data table responds to dynamic filters
(example -> filter for ‘black’)

 ![image](https://github.com/user-attachments/assets/1db22717-abd2-4429-9d62-f4718b1b17ab)

5.	Geolocation chart

 ![image](https://github.com/user-attachments/assets/b5a1343f-ef68-49e4-8db6-fa9f291309bf)

6.	Pie chart that responds to dynamic filters and filter rescue buttons
For example, all dog data (*Note dog breed counts < 100 categorized as other for easy viewing)

 ![image](https://github.com/user-attachments/assets/c7739797-aa28-47ec-afd4-94ae503eb26b)


Filter For Water Type Rescue (Note: The breeds here are by count because the database values for the filters are less than 100 results)

![image](https://github.com/user-attachments/assets/3a434d26-b44a-4350-b7ac-4c6d6b52bf28)

 
Filter For Mountain Type Rescue (Note: The breeds here are by count because the database values for the filters are less than 100 results)

 ![image](https://github.com/user-attachments/assets/1afee7e9-e05c-47f0-999d-0cfc8f4b470f)

Filter For Disaster Type Rescue (Note: The breeds here are by count because the database values for the filters are less than 100 results)

 ![image](https://github.com/user-attachments/assets/726a57d5-79a0-4e46-b65a-b90ca5492425)


### Contact: Laurie Sylvester

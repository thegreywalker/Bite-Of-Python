import urllib
import pyrebase

firebaseConfig = { 
    'apiKey': "AIzaSyAG0kJHmzlwkucxCLbwMHvF5auDNOvoLmw",
    'authDomain': "testdatabase-b9158.firebaseapp.com",
    'databaseURL': "https://testdatabase-b9158-default-rtdb.firebaseio.com",
    'projectId': "testdatabase-b9158",
    'storageBucket': "testdatabase-b9158.appspot.com",
    'messagingSenderId': "93699768754",
    'appId': "1:93699768754:web:fbae7f9f938b1261a1a4ab",
    'measurementId': "G-94VG9L1ZW1"
    }

firebase = pyrebase.initialize_app(firebaseConfig)

db = firebase.database()
# auth = firebase.auth()
# storage = firebase.storage()


""" 
Authentication/
Login
"""
# email = input("Enter Your Email: ")
# password = input("Enter Your Password: ")
# try:
#     auth.sign_in_with_email_and_password(email,password)
#     print("Logged In Succesfully.")
# except:
#     print("Invalid User or password, Try Again!")


"""
SignUp using HTTP requests 
"""

# email = input("Enter Your email: ")
# password = input("Enter Your Password: ")
# confirm_pass = input("Confirm Your Password: ")
# if password == confirm_pass:
#     try:
#         auth.create_user_with_email_and_password(email,password)
#         print("Succesfully Created a User, Congratulations!")
#     except:
#         print("User alraedy Exists")
# else:
#     print("The Password and Confirm Password field doesen't match.")



"""
Storage: 
"""

# filename = input("Enter the name o the file you want to upload: ")
# coludfilename = input("Enter the name of the file on the cloud: ")
# storage.child(coludfilename).put(filename)

""" 
Get the URL of the file uploaded in storage:
"""
# print(storage.child(coludfilename).get_url(None))


"""
Download a file from Storage:  
"""

# cloudfilename = input("Enter the name of the file you want to Download: ")
# storage.child(cloudfilename).download("","downloaded.jpeg")



"""
Download a file from Storage and reading it from external cmd rather than downloading
it to current directory  
"""

# cloudfilename = input("Enter the name of the file you want to Download: ")
# url = storage.child(cloudfilename).get_url(None)
# f = urllib.request.urlopen(url).read()
# print(f)




"""
Database 
"""

# data = {'Age' : 33, 'Address' : "New York", 'Employed' : True, 'Name' : "Bishal Ghosh"}
# # If you want to just add a data under some random generated key under your mentioned header then give this command.
# db.child("People").child("Bishal ID").set(data)
# # If you want to Create your own header under which the data will be stored and not some random generated key under your mentioned header then give this command.
# db.child("People").child("Bishal ID").set(data)
# print("Congratulations! the Data has been Pushed")

data = {'Age' : 25, 'Adress' : "Payradanga", 'Employed' : False, 'Name' : "Subho Sarkar"}
db.child("People").child("Subho ID").set(data)
print("Congratulations! the Data has been Pushed")

























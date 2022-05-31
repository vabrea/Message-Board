import requests
from pprint import pprint

URL = "http://127.0.0.1:5000/users"
USER_TEMPLATE = {
    "first_name": "Jon",
    "last_name": "Doe",
    "hobbies": "Playing basketball"
}

def get_user(pk):
    url = "%s/%s" % (URL, pk)
    response = requests.get(url)
    if response.status_code == 200:
        pprint(response.json())
    else:
        print("Something went wrong with retrieving the data")


def update_user(pk, first_name, last_name, hobbies):
    url = "%s/%s" % (URL,  pk)
    user_data = USER_TEMPLATE
    user_data.get(first_name)
    user_data.get(last_name)
    user_data.get(hobbies) 
    response = requests.put(url, json=user_data)
    if response.status_code == 204:
        print("User successfully updated")
    else:
        print("Something went wrong whilte trying to update a user.")

if __name__ == "__main__":
    print ("UPDATE A USER")
    print("___________________")
    target_id = input("Please enter a user ID: ")
    user = get_user(target_id)
    fname = input("First name: ")
    lname = input("Last name: ")
    hobbies = input("Hobbies: ")
    update_user(target_id, fname, lname, hobbies)
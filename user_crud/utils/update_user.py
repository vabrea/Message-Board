import requests


URL = "http://127.0.0.1:5000/users/"
USER_TEMPLATE = {
    "id": "0",
    "first_name": "Jon",
    "last_name": "Doe",
    "hobbies": "Playing basketball"
}

def update_user(id,first_name, last_name, hobbies):
    user_data = USER_TEMPLATE
    user_data.get(id)
    user_data.get(first_name)
    user_data.get(last_name)
    user_data.get(hobbies) 
    response = requests.put(URL, json=user_data)
    if response.status_code == 204:
        print("User successfully updated")
    else:
        print("Something went wrong whilte trying to update a user.")

if __name__ == "__main__":
    print ("UPDATE A USER")
    print("___________________")
    target_id = input("Please enter a user ID: ")
    fname = input("First name: ")
    lname = input("Last name: ")
    hobbies = input("Hobbies: ")
    update_user(fname, lname, hobbies)
import requests
from pprint import pprint

URL = "http://127.0.0.1:5000/users"



def get_user(pk):
    url = "%s/%s" % (URL, pk)
    response = requests.get(url)
    if response.status_code == 200:
        pprint(response.json())
    else:
        print("Something went wrong with retrieving the data")



def delete_user(pk):
    url = "%s/%s" % (URL, pk)
    response = requests.delete(url)
    if response.status_code == 204:
        pprint("User successfully deleted")
    else:
        print("Something went wrong trying to delete target user")


if __name__ == "__main__":
    print("DELETE USER")
    print("-" * 50)
    user_id = input("type in the targer user ID: ")
    print("Delete the user shown below?")
    get_user(user_id)
    option = input ("[Y/n] : ")
    if option == "Y" or option == "y":
        delete_user(user_id)
    else:
        print("User not deleted.")

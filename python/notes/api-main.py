import requests

if __name__ == '__main__':
    response = requests.get("https://gitlab.com/api/v4/users/nanuchi/projects")

    # print(response.text) # print(response) just http code
    # print(response.json)    # this will be a list
    my_projects = response.json()

    for project in my_projects:
        print("Project Name: {n}\n\tProject Url: {u}".format(n=project['name'],u=project['web_url']))







# One class per file. Filename == same as class name.
# in main.py -> from user import User

class User:
    def __init__(self, email, name, password, current_job_title):
        self.email = email
        self.name = name
        self.password = password
        self.current_job_title = current_job_title

    def change_password(self,new_password):
        self.password = new_password

    def change_job_title(self, new_title):
        self.current_job_title = new_title

    def get_user_info(self):
        print("User {u} currenty works as a {t}. You can reach them at {e}".format(u=self.name, t=self.current_job_title, e=self.email))


if __name__ == '__main__':
    new_user = User("nn@nn.com","person anme", "pwd1", "job1")

    new_user.get_user_info()
    new_user.change_job_title("devops master")
    new_user.get_user_info()
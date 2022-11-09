class Email:
    def __init__(self, email=None):
        self.__email = email

    @property
    def validate(self):
        if not self.__email:
            return "Email is empty, please set it"
        else:
            return f"Your email is: {self.__email}"

    @validate.setter
    def validate(self, email):
        for index in range(len(email)):
            if email[index] not in "!#$%^&*()+=''/?><,][}{|":
                if email[email.find("@") + 1].isalnum() and email[email.find("@") + 1].isalnum():
                    if email.count("@") == 1:
                        if email[0] not in "-_." and email[-1] not in "-_.":
                            if email[email.find(".")] != email[email.find(".") + 1] \
                                    and email[email.find("_")] != email[email.find("_") + 1] \
                                    and email[email.find("-")] != email[email.find("-") + 1]:
                                self.__email = email
                                print("Valid email")
                                break
                            else:
                                print("Invalid email")
                                break
                        else:
                            print("Invalid email")
                            break
                    else:
                        print("Invalid email")
                        break
                else:
                    print("Invalid email")
                    break
            else:
                print("Invalid email")
                break


mail = Email()
mail.validate = "v-lad_dsd@gmail.com"  # valid

mail.validate = "v-lad_dsd@gmail..com"
mail.validate = "_v-lad_dsd@gmail.com"
mail.validate = "_v-lad_dsd@gma@il.com"
mail.validate = "v-la^d_dsd@gma@il.com"
mail.validate = "vla d_dsd@gma@il.com"
mail.validate = "vlad_dsd@gma@il.com-"
mail.validate = "vlad__dsd@gma@il.com-"
mail.validate = "v-lad_dsd@gma@il.c*om"



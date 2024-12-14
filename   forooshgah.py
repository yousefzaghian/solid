import random
class User:
    def __init__(self, user_name, password, f = None):
        self.user_name = user_name
        self.password = password
        f = open("logins.txt", "w")
        self.f = f
        if self.user_name or self.password not in self.f:
            self.anwser = input("Do you want to register in the site?\n")
            if self.anwser == "yes":
                self.register()
            elif self.anwser == "no":
                print("Ok.no problem.you can add a product to your shopping cart and exploring in the site now.")
        elif self.user_name and self.password in self.f:
            print("Congratulations.You can buy a product or you can manage your shopping cart.")

    def register(self):
        while 1:
            try:
                name = input("name : ")
                last_name = input("last name : ")
                email = input("email : ")
                user_name = input("user_name : ")
                password = input("password : ")
                repeat_password = input("repeat password : ")
                address = f"address : {random.randint(10000, 13567852)}"
                if password == repeat_password:
                    break
                else:
                    print("the two of this must be the same.")

            except ValueError:
                print("please enter your information truely.")
        self.name = name
        self.last_name = last_name
        self.email = email
        self.user_name1 = user_name
        self.password1 = password
        self.repeat_password = repeat_password
        self.address = address
        self.f.write(f"name : {self.name}")
        self.f.write(f"last name : {self.last_name}")
        self.f.write(f"email : {self.email}")
        self.f.write(f"user name : {self.user_name1}")
        self.f.write(f"password : {self.password}")
        self.f.write(f"address : {self.address}")

        print("your register has become completed.")


class Product:
    def __init__(self, g = None):
        self.user_name = input("user name : ")
        self.password = input("password : ")
        g = open("products.txt", "w")
        self.g = g
        if self.user_name == "Admin" and self.password == "password":
            self.a = input("What do you want to do?\nplease choose from this options:\n1.add product\n2.edit product\n3.delete product\n")
            if self.a == "1":
                self.add_product()
            elif self.a == "2":
                self.edit_product()
            elif self.a == "3":
                self.__del__()
        else:
            print("you can't change the product. Only admin can do that.")


    def add_product(self):
        while 1:
            try:
                product_name = input("Enter the name of product : ")
                price = input("Enter the price of product : ")
                description = input("description : ")
                break
            except:
                print("the information of product is not true.\nplease try again")
        
        self.product_name = product_name
        self.price = price
        self.description = description

        self.g.write(f"product name : {self.product_name}\n")
        self.g.write(f"price : {self.price}\n")
        self.g.write(f"description : {self.description}")

        
        print(f"the product with this name has added to site now. ---> {self.product_name}")

    
    def edit_product(self):
        self.second_anwser = input("What do you want to edit?\nplease choose from this options:\n1.product name\n2.product price\n3.product description\n")
        if self.second_anwser == "1":
            self.product_name = input("Enter a new name for this product : ")
            print(f"the product name has changed to {self.product_name}")
        elif self.second_anwser == "2":
            self.product_price = input("Enter a new price for this product : ")
            print(f"the product price has changed to {self.product_price}")

        elif self.second_anwser == "3":
            self.product_description = input("Enter a new description for this product : ")
            print(f"the description of this product has changed.")

        self.g.write(f"product name : {self.product_name}\n")
        self.g.write(f"price : {self.price}\n")
        self.g.write(f"description : {self.description}")

    def __del__(self):
        print("the product has deleted.")

user = User("ali", "pass")
product = Product()   
    



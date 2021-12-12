""" A ShoeController Module """

from masonite.controllers import Controller
from masonite.request import Request
from app.Shoe import Shoe

class ShoeController(Controller):
    """Class Docstring Description
    """

    def __init__(self, request: Request):
        self.request = request

    def show(self):
        id = self.request.param("id")
        return Shoe.where("id", id).get()

    def index(self):
        return Shoe.all()

    

    def create(self):
        image = self.request.input("image")
        title = self.request.input("title")
        description = self.request.input("description")
        price = self.request.input("price")
        size = self.request.input("size")
        purchased = self.request.input("purchased")
        shoe = Shoe.create({"image": image, "title": title, "description": description, "price": price,"size": size, "purchased": purchased})
        return shoe


    def update(self):
        image = self.request.input("image")
        title = self.request.input("title")
        description = self.request.input("description")
        price = self.request.input("price")
        size = self.request.input("size")
        purchased = self.request.input("purchased")
        id = self.request.param("id")
        Shoe.where("id", id).update({"image": image, "title": title, "description": description, "price": price,"size": size, "purchased": purchased})
        return Shoe.where("id", id).get()



    def destroy(self):
        id = self.request.param("id")
        shoe = Shoe.where("id", id).get()
        Shoe.where("id", id).delete()
        return shoe
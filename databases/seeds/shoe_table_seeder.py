"""ShoeTableSeeder Seeder."""

from masoniteorm.seeds import Seeder

from app.Shoe import Shoe


class ShoeTableSeeder(Seeder):
    def run(self):
        Shoe.create({"image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQMKze8XC4c_vFaep5kS_eFb6vJa4QzAHuOEA&usqp=CAU", "title": "New pumps", "description": "Red heels for the weekend", "price": 75.00, "size": 6})
        Shoe.create({"image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRpccRjTJ8gxo-3IuNipIEz5Ogmms4StoEYRA&usqp=CAU", "title": "New pumps", "description": "Black heels", "price": 65.00, "size": 6})
        Shoe.create({"image": "https://www.thetrendspotter.net/wp-content/uploads/2017/12/Cone-heel-1.jpg", "title": "New pumps", "description": "Cone Heel", "price": 75.00, "size": 6})
        Shoe.create({"image": "https://www.thetrendspotter.net/wp-content/uploads/2018/01/Decorative-Heel.jpg", "title": "New pumps", "description": "Decorative Heel", "price": 75.00, "size": 6})
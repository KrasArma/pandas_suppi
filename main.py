# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

import pandas as pd
import math
json = [
   {
      "order_id": 11973,
      "warehouse_name": "Мордор",
      "highway_cost": -70,
      "products": [
         {
            "product": "ломтик июльского неба",
            "price": 450,
            "quantity": 1
         },
         {
            "product": "билет в Израиль",
            "price": 1000,
            "quantity": 3
         },
         {
            "product": "статуэтка Ленина",
            "price": 200,
            "quantity": 3
         }
      ]
   },
   {
      "order_id": 62239,
      "warehouse_name": "хутор близ Диканьки",
      "highway_cost": -15,
      "products": [
         {
            "product": "билет в Израиль",
            "price": 1000,
            "quantity": 1
         }
      ]
   },
   {
      "order_id": 85794,
      "warehouse_name": "отель Лето",
      "highway_cost": -50,
      "products": [
         {
            "product": "зеленая пластинка",
            "price": 10,
            "quantity": 2
         }
      ]
   },
   {
      "order_id": 33684,
      "warehouse_name": "Мордор",
      "highway_cost": -30,
      "products": [
         {
            "product": "билет в Израиль",
            "price": 1000,
            "quantity": 2
         },
         {
            "product": "зеленая пластинка",
            "price": 10,
            "quantity": 1
         }
      ]
   },
   {
      "order_id": 25824,
      "warehouse_name": "отель Лето",
      "highway_cost": -75,
      "products": [
         {
            "product": "автограф Стаса Барецкого",
            "price": 600,
            "quantity": 1
         },
         {
            "product": "статуэтка Ленина",
            "price": 200,
            "quantity": 1
         },
         {
            "product": "плюмбус",
            "price": 250,
            "quantity": 1
         }
      ]
   },
   {
      "order_id": 87044,
      "warehouse_name": "остров невезения",
      "highway_cost": -15,
      "products": [
         {
            "product": "плюмбус",
            "price": 250,
            "quantity": 3
         }
      ]
   },
   {
      "order_id": 58598,
      "warehouse_name": "гиперборея",
      "highway_cost": -160,
      "products": [
         {
            "product": "плюмбус",
            "price": 250,
            "quantity": 3
         },
         {
            "product": "статуэтка Ленина",
            "price": 200,
            "quantity": 3
         },
         {
            "product": "статуэтка Ленина",
            "price": 200,
            "quantity": 2
         }
      ]
   },
   {
      "order_id": 5430,
      "warehouse_name": "гиперборея",
      "highway_cost": -80,
      "products": [
         {
            "product": "ломтик июльского неба",
            "price": 450,
            "quantity": 1
         },
         {
            "product": "плюмбус",
            "price": 250,
            "quantity": 3
         }
      ]
   },
   {
      "order_id": 60502,
      "warehouse_name": "отель Лето",
      "highway_cost": -75,
      "products": [
         {
            "product": "автограф Стаса Барецкого",
            "price": 600,
            "quantity": 3
         }
      ]
   },
   {
      "order_id": 96473,
      "warehouse_name": "Мордор",
      "highway_cost": -20,
      "products": [
         {
            "product": "зеленая пластинка",
            "price": 10,
            "quantity": 2
         }
      ]
   },
   {
      "order_id": 64013,
      "warehouse_name": "хутор близ Диканьки",
      "highway_cost": -105,
      "products": [
         {
            "product": "плюмбус",
            "price": 250,
            "quantity": 2
         },
         {
            "product": "плюмбус",
            "price": 250,
            "quantity": 2
         },
         {
            "product": "зеленая пластинка",
            "price": 10,
            "quantity": 3
         }
      ]
   },
   {
      "order_id": 59105,
      "warehouse_name": "отель Лето",
      "highway_cost": -25,
      "products": [
         {
            "product": "статуэтка Ленина",
            "price": 200,
            "quantity": 1
         }
      ]
   },
   {
      "order_id": 85535,
      "warehouse_name": "отель Лето",
      "highway_cost": -25,
      "products": [
         {
            "product": "статуэтка Ленина",
            "price": 200,
            "quantity": 1
         }
      ]
   },
   {
      "order_id": 24928,
      "warehouse_name": "хутор близ Диканьки",
      "highway_cost": -60,
      "products": [
         {
            "product": "подписка на suppi-блог",
            "price": 150,
            "quantity": 2
         },
         {
            "product": "статуэтка Ленина",
            "price": 200,
            "quantity": 1
         },
         {
            "product": "статуэтка Ленина",
            "price": 200,
            "quantity": 1
         }
      ]
   },
   {
      "order_id": 2751,
      "warehouse_name": "гиперборея",
      "highway_cost": -80,
      "products": [
         {
            "product": "зеленая пластинка",
            "price": 10,
            "quantity": 3
         },
         {
            "product": "зеленая пластинка",
            "price": 10,
            "quantity": 1
         }
      ]
   },
   {
      "order_id": 35995,
      "warehouse_name": "гиперборея",
      "highway_cost": -20,
      "products": [
         {
            "product": "ломтик июльского неба",
            "price": 450,
            "quantity": 1
         }
      ]
   },
   {
      "order_id": 80252,
      "warehouse_name": "остров невезения",
      "highway_cost": -35,
      "products": [
         {
            "product": "статуэтка Ленина",
            "price": 200,
            "quantity": 3
         },
         {
            "product": "статуэтка Ленина",
            "price": 200,
            "quantity": 2
         },
         {
            "product": "ломтик июльского неба",
            "price": 450,
            "quantity": 2
         }
      ]
   },
   {
      "order_id": 27443,
      "warehouse_name": "Мордор",
      "highway_cost": -10,
      "products": [
         {
            "product": "статуэтка Ленина",
            "price": 200,
            "quantity": 1
         }
      ]
   },
   {
      "order_id": 1391,
      "warehouse_name": "остров невезения",
      "highway_cost": -10,
      "products": [
         {
            "product": "плюмбус",
            "price": 250,
            "quantity": 2
         }
      ]
   },
   {
      "order_id": 83474,
      "warehouse_name": "хутор близ Диканьки",
      "highway_cost": -75,
      "products": [
         {
            "product": "плюмбус",
            "price": 250,
            "quantity": 2
         },
         {
            "product": "ломтик июльского неба",
            "price": 450,
            "quantity": 3
         }
      ]
   },
   {
      "order_id": 84471,
      "warehouse_name": "хутор близ Диканьки",
      "highway_cost": -60,
      "products": [
         {
            "product": "плюмбус",
            "price": 250,
            "quantity": 1
         },
         {
            "product": "ломтик июльского неба",
            "price": 450,
            "quantity": 1
         },
         {
            "product": "подписка на suppi-блог",
            "price": 150,
            "quantity": 2
         }
      ]
   },
   {
      "order_id": 96799,
      "warehouse_name": "остров невезения",
      "highway_cost": -10,
      "products": [
         {
            "product": "ломтик июльского неба",
            "price": 450,
            "quantity": 2
         }
      ]
   },
   {
      "order_id": 99324,
      "warehouse_name": "остров невезения",
      "highway_cost": -10,
      "products": [
         {
            "product": "автограф Стаса Барецкого",
            "price": 600,
            "quantity": 1
         },
         {
            "product": "билет в Израиль",
            "price": 1000,
            "quantity": 1
         }
      ]
   },
   {
      "order_id": 85787,
      "warehouse_name": "хутор близ Диканьки",
      "highway_cost": -90,
      "products": [
         {
            "product": "зеленая пластинка",
            "price": 10,
            "quantity": 3
         },
         {
            "product": "зеленая пластинка",
            "price": 10,
            "quantity": 2
         },
         {
            "product": "билет в Израиль",
            "price": 1000,
            "quantity": 1
         }
      ]
   },
   {
      "order_id": 28774,
      "warehouse_name": "отель Лето",
      "highway_cost": -175,
      "products": [
         {
            "product": "билет в Израиль",
            "price": 1000,
            "quantity": 2
         },
         {
            "product": "статуэтка Ленина",
            "price": 200,
            "quantity": 3
         },
         {
            "product": "билет в Израиль",
            "price": 1000,
            "quantity": 2
         }
      ]
   },
   {
      "order_id": 68707,
      "warehouse_name": "отель Лето",
      "highway_cost": -50,
      "products": [
         {
            "product": "плюмбус",
            "price": 250,
            "quantity": 2
         }
      ]
   },
   {
      "order_id": 99220,
      "warehouse_name": "хутор близ Диканьки",
      "highway_cost": -75,
      "products": [
         {
            "product": "плюмбус",
            "price": 250,
            "quantity": 3
         },
         {
            "product": "подписка на suppi-блог",
            "price": 150,
            "quantity": 1
         },
         {
            "product": "плюмбус",
            "price": 250,
            "quantity": 1
         }
      ]
   },
   {
      "order_id": 59930,
      "warehouse_name": "остров невезения",
      "highway_cost": -20,
      "products": [
         {
            "product": "зеленая пластинка",
            "price": 10,
            "quantity": 2
         },
         {
            "product": "статуэтка Ленина",
            "price": 200,
            "quantity": 2
         }
      ]
   },
   {
      "order_id": 70074,
      "warehouse_name": "остров невезения",
      "highway_cost": -30,
      "products": [
         {
            "product": "плюмбус",
            "price": 250,
            "quantity": 2
         },
         {
            "product": "плюмбус",
            "price": 250,
            "quantity": 1
         },
         {
            "product": "ломтик июльского неба",
            "price": 450,
            "quantity": 3
         }
      ]
   },
   {
      "order_id": 12715,
      "warehouse_name": "хутор близ Диканьки",
      "highway_cost": -45,
      "products": [
         {
            "product": "автограф Стаса Барецкого",
            "price": 600,
            "quantity": 1
         },
         {
            "product": "автограф Стаса Барецкого",
            "price": 600,
            "quantity": 2
         }
      ]
   },
   {
      "order_id": 63213,
      "warehouse_name": "Мордор",
      "highway_cost": -30,
      "products": [
         {
            "product": "зеленая пластинка",
            "price": 10,
            "quantity": 3
         }
      ]
   },
   {
      "order_id": 32313,
      "warehouse_name": "хутор близ Диканьки",
      "highway_cost": -120,
      "products": [
         {
            "product": "билет в Израиль",
            "price": 1000,
            "quantity": 3
         },
         {
            "product": "плюмбус",
            "price": 250,
            "quantity": 2
         },
         {
            "product": "зеленая пластинка",
            "price": 10,
            "quantity": 3
         }
      ]
   },
   {
      "order_id": 65113,
      "warehouse_name": "хутор близ Диканьки",
      "highway_cost": -30,
      "products": [
         {
            "product": "плюмбус",
            "price": 250,
            "quantity": 2
         }
      ]
   },
   {
      "order_id": 56905,
      "warehouse_name": "Мордор",
      "highway_cost": -20,
      "products": [
         {
            "product": "билет в Израиль",
            "price": 1000,
            "quantity": 2
         }
      ]
   },
   {
      "order_id": 14742,
      "warehouse_name": "хутор близ Диканьки",
      "highway_cost": -60,
      "products": [
         {
            "product": "статуэтка Ленина",
            "price": 200,
            "quantity": 1
         },
         {
            "product": "автограф Стаса Барецкого",
            "price": 600,
            "quantity": 1
         },
         {
            "product": "плюмбус",
            "price": 250,
            "quantity": 2
         }
      ]
   },
   {
      "order_id": 16240,
      "warehouse_name": "Мордор",
      "highway_cost": -20,
      "products": [
         {
            "product": "билет в Израиль",
            "price": 1000,
            "quantity": 2
         }
      ]
   },
   {
      "order_id": 79318,
      "warehouse_name": "Мордор",
      "highway_cost": -30,
      "products": [
         {
            "product": "автограф Стаса Барецкого",
            "price": 600,
            "quantity": 1
         },
         {
            "product": "статуэтка Ленина",
            "price": 200,
            "quantity": 2
         }
      ]
   },
   {
      "order_id": 20914,
      "warehouse_name": "гиперборея",
      "highway_cost": -40,
      "products": [
         {
            "product": "билет в Израиль",
            "price": 1000,
            "quantity": 2
         }
      ]
   },
   {
      "order_id": 42314,
      "warehouse_name": "хутор близ Диканьки",
      "highway_cost": -45,
      "products": [
         {
            "product": "статуэтка Ленина",
            "price": 200,
            "quantity": 1
         },
         {
            "product": "статуэтка Ленина",
            "price": 200,
            "quantity": 2
         }
      ]
   },
   {
      "order_id": 68783,
      "warehouse_name": "остров невезения",
      "highway_cost": -15,
      "products": [
         {
            "product": "статуэтка Ленина",
            "price": 200,
            "quantity": 3
         }
      ]
   },
   {
      "order_id": 47954,
      "warehouse_name": "гиперборея",
      "highway_cost": -60,
      "products": [
         {
            "product": "билет в Израиль",
            "price": 1000,
            "quantity": 3
         }
      ]
   },
   {
      "order_id": 83618,
      "warehouse_name": "Мордор",
      "highway_cost": -30,
      "products": [
         {
            "product": "зеленая пластинка",
            "price": 10,
            "quantity": 3
         }
      ]
   },
   {
      "order_id": 57775,
      "warehouse_name": "хутор близ Диканьки",
      "highway_cost": -30,
      "products": [
         {
            "product": "статуэтка Ленина",
            "price": 200,
            "quantity": 2
         }
      ]
   },
   {
      "order_id": 66474,
      "warehouse_name": "гиперборея",
      "highway_cost": -140,
      "products": [
         {
            "product": "плюмбус",
            "price": 250,
            "quantity": 2
         },
         {
            "product": "автограф Стаса Барецкого",
            "price": 600,
            "quantity": 3
         },
         {
            "product": "билет в Израиль",
            "price": 1000,
            "quantity": 2
         }
      ]
   },
   {
      "order_id": 72097,
      "warehouse_name": "остров невезения",
      "highway_cost": -30,
      "products": [
         {
            "product": "ломтик июльского неба",
            "price": 450,
            "quantity": 3
         },
         {
            "product": "зеленая пластинка",
            "price": 10,
            "quantity": 3
         }
      ]
   },
   {
      "order_id": 74454,
      "warehouse_name": "отель Лето",
      "highway_cost": -150,
      "products": [
         {
            "product": "зеленая пластинка",
            "price": 10,
            "quantity": 1
         },
         {
            "product": "автограф Стаса Барецкого",
            "price": 600,
            "quantity": 2
         },
         {
            "product": "билет в Израиль",
            "price": 1000,
            "quantity": 3
         }
      ]
   },
   {
      "order_id": 14350,
      "warehouse_name": "гиперборея",
      "highway_cost": -120,
      "products": [
         {
            "product": "автограф Стаса Барецкого",
            "price": 600,
            "quantity": 1
         },
         {
            "product": "ломтик июльского неба",
            "price": 450,
            "quantity": 3
         },
         {
            "product": "автограф Стаса Барецкого",
            "price": 600,
            "quantity": 2
         }
      ]
   },
   {
      "order_id": 4035,
      "warehouse_name": "хутор близ Диканьки",
      "highway_cost": -75,
      "products": [
         {
            "product": "автограф Стаса Барецкого",
            "price": 600,
            "quantity": 2
         },
         {
            "product": "билет в Израиль",
            "price": 1000,
            "quantity": 3
         }
      ]
   },
   {
      "order_id": 67495,
      "warehouse_name": "Мордор",
      "highway_cost": -70,
      "products": [
         {
            "product": "подписка на suppi-блог",
            "price": 150,
            "quantity": 1
         },
         {
            "product": "подписка на suppi-блог",
            "price": 150,
            "quantity": 3
         },
         {
            "product": "подписка на suppi-блог",
            "price": 150,
            "quantity": 3
         }
      ]
   },
   {
      "order_id": 49616,
      "warehouse_name": "отель Лето",
      "highway_cost": -100,
      "products": [
         {
            "product": "билет в Израиль",
            "price": 1000,
            "quantity": 3
         },
         {
            "product": "зеленая пластинка",
            "price": 10,
            "quantity": 1
         }
      ]
   },
   {
      "order_id": 83887,
      "warehouse_name": "гиперборея",
      "highway_cost": -80,
      "products": [
         {
            "product": "зеленая пластинка",
            "price": 10,
            "quantity": 1
         },
         {
            "product": "статуэтка Ленина",
            "price": 200,
            "quantity": 2
         },
         {
            "product": "билет в Израиль",
            "price": 1000,
            "quantity": 1
         }
      ]
   },
   {
      "order_id": 50030,
      "warehouse_name": "гиперборея",
      "highway_cost": -140,
      "products": [
         {
            "product": "подписка на suppi-блог",
            "price": 150,
            "quantity": 3
         },
         {
            "product": "билет в Израиль",
            "price": 1000,
            "quantity": 2
         },
         {
            "product": "автограф Стаса Барецкого",
            "price": 600,
            "quantity": 2
         }
      ]
   },
   {
      "order_id": 2558,
      "warehouse_name": "хутор близ Диканьки",
      "highway_cost": -75,
      "products": [
         {
            "product": "плюмбус",
            "price": 250,
            "quantity": 1
         },
         {
            "product": "зеленая пластинка",
            "price": 10,
            "quantity": 3
         },
         {
            "product": "подписка на suppi-блог",
            "price": 150,
            "quantity": 1
         }
      ]
   },
   {
      "order_id": 82378,
      "warehouse_name": "остров невезения",
      "highway_cost": -5,
      "products": [
         {
            "product": "статуэтка Ленина",
            "price": 200,
            "quantity": 1
         }
      ]
   },
   {
      "order_id": 88503,
      "warehouse_name": "гиперборея",
      "highway_cost": -140,
      "products": [
         {
            "product": "зеленая пластинка",
            "price": 10,
            "quantity": 2
         },
         {
            "product": "билет в Израиль",
            "price": 1000,
            "quantity": 3
         },
         {
            "product": "подписка на suppi-блог",
            "price": 150,
            "quantity": 2
         }
      ]
   },
   {
      "order_id": 17339,
      "warehouse_name": "гиперборея",
      "highway_cost": -60,
      "products": [
         {
            "product": "автограф Стаса Барецкого",
            "price": 600,
            "quantity": 3
         }
      ]
   },
   {
      "order_id": 2108,
      "warehouse_name": "остров невезения",
      "highway_cost": -10,
      "products": [
         {
            "product": "зеленая пластинка",
            "price": 10,
            "quantity": 1
         },
         {
            "product": "статуэтка Ленина",
            "price": 200,
            "quantity": 1
         }
      ]
   },
   {
      "order_id": 48000,
      "warehouse_name": "остров невезения",
      "highway_cost": -30,
      "products": [
         {
            "product": "плюмбус",
            "price": 250,
            "quantity": 1
         },
         {
            "product": "плюмбус",
            "price": 250,
            "quantity": 3
         },
         {
            "product": "статуэтка Ленина",
            "price": 200,
            "quantity": 2
         }
      ]
   },
   {
      "order_id": 2091,
      "warehouse_name": "отель Лето",
      "highway_cost": -100,
      "products": [
         {
            "product": "ломтик июльского неба",
            "price": 450,
            "quantity": 2
         },
         {
            "product": "плюмбус",
            "price": 250,
            "quantity": 2
         }
      ]
   },
   {
      "order_id": 35330,
      "warehouse_name": "отель Лето",
      "highway_cost": -125,
      "products": [
         {
            "product": "билет в Израиль",
            "price": 1000,
            "quantity": 2
         },
         {
            "product": "зеленая пластинка",
            "price": 10,
            "quantity": 3
         }
      ]
   },
   {
      "order_id": 89159,
      "warehouse_name": "гиперборея",
      "highway_cost": -40,
      "products": [
         {
            "product": "подписка на suppi-блог",
            "price": 150,
            "quantity": 2
         }
      ]
   },
   {
      "order_id": 22103,
      "warehouse_name": "гиперборея",
      "highway_cost": -60,
      "products": [
         {
            "product": "плюмбус",
            "price": 250,
            "quantity": 1
         },
         {
            "product": "подписка на suppi-блог",
            "price": 150,
            "quantity": 1
         },
         {
            "product": "билет в Израиль",
            "price": 1000,
            "quantity": 1
         }
      ]
   },
   {
      "order_id": 64670,
      "warehouse_name": "гиперборея",
      "highway_cost": -100,
      "products": [
         {
            "product": "билет в Израиль",
            "price": 1000,
            "quantity": 2
         },
         {
            "product": "ломтик июльского неба",
            "price": 450,
            "quantity": 3
         }
      ]
   },
   {
      "order_id": 52587,
      "warehouse_name": "Мордор",
      "highway_cost": -80,
      "products": [
         {
            "product": "зеленая пластинка",
            "price": 10,
            "quantity": 2
         },
         {
            "product": "плюмбус",
            "price": 250,
            "quantity": 3
         },
         {
            "product": "автограф Стаса Барецкого",
            "price": 600,
            "quantity": 3
         }
      ]
   },
   {
      "order_id": 88114,
      "warehouse_name": "отель Лето",
      "highway_cost": -75,
      "products": [
         {
            "product": "ломтик июльского неба",
            "price": 450,
            "quantity": 1
         },
         {
            "product": "подписка на suppi-блог",
            "price": 150,
            "quantity": 1
         },
         {
            "product": "плюмбус",
            "price": 250,
            "quantity": 1
         }
      ]
   },
   {
      "order_id": 72357,
      "warehouse_name": "гиперборея",
      "highway_cost": -100,
      "products": [
         {
            "product": "подписка на suppi-блог",
            "price": 150,
            "quantity": 1
         },
         {
            "product": "билет в Израиль",
            "price": 1000,
            "quantity": 2
         },
         {
            "product": "билет в Израиль",
            "price": 1000,
            "quantity": 2
         }
      ]
   },
   {
      "order_id": 82545,
      "warehouse_name": "отель Лето",
      "highway_cost": -125,
      "products": [
         {
            "product": "подписка на suppi-блог",
            "price": 150,
            "quantity": 2
         },
         {
            "product": "плюмбус",
            "price": 250,
            "quantity": 3
         }
      ]
   },
   {
      "order_id": 59590,
      "warehouse_name": "отель Лето",
      "highway_cost": -75,
      "products": [
         {
            "product": "билет в Израиль",
            "price": 1000,
            "quantity": 3
         }
      ]
   },
   {
      "order_id": 20814,
      "warehouse_name": "хутор близ Диканьки",
      "highway_cost": -45,
      "products": [
         {
            "product": "статуэтка Ленина",
            "price": 200,
            "quantity": 2
         },
         {
            "product": "автограф Стаса Барецкого",
            "price": 600,
            "quantity": 1
         }
      ]
   },
   {
      "order_id": 32918,
      "warehouse_name": "хутор близ Диканьки",
      "highway_cost": -105,
      "products": [
         {
            "product": "статуэтка Ленина",
            "price": 200,
            "quantity": 1
         },
         {
            "product": "автограф Стаса Барецкого",
            "price": 600,
            "quantity": 3
         },
         {
            "product": "плюмбус",
            "price": 250,
            "quantity": 3
         }
      ]
   },
   {
      "order_id": 33899,
      "warehouse_name": "гиперборея",
      "highway_cost": -20,
      "products": [
         {
            "product": "билет в Израиль",
            "price": 1000,
            "quantity": 1
         }
      ]
   },
   {
      "order_id": 72309,
      "warehouse_name": "остров невезения",
      "highway_cost": -5,
      "products": [
         {
            "product": "билет в Израиль",
            "price": 1000,
            "quantity": 1
         }
      ]
   },
   {
      "order_id": 98423,
      "warehouse_name": "хутор близ Диканьки",
      "highway_cost": -30,
      "products": [
         {
            "product": "автограф Стаса Барецкого",
            "price": 600,
            "quantity": 2
         }
      ]
   },
   {
      "order_id": 28543,
      "warehouse_name": "хутор близ Диканьки",
      "highway_cost": -75,
      "products": [
         {
            "product": "статуэтка Ленина",
            "price": 200,
            "quantity": 3
         },
         {
            "product": "статуэтка Ленина",
            "price": 200,
            "quantity": 2
         }
      ]
   },
   {
      "order_id": 64068,
      "warehouse_name": "Мордор",
      "highway_cost": -10,
      "products": [
         {
            "product": "подписка на suppi-блог",
            "price": 150,
            "quantity": 1
         }
      ]
   },
   {
      "order_id": 75938,
      "warehouse_name": "гиперборея",
      "highway_cost": -80,
      "products": [
         {
            "product": "зеленая пластинка",
            "price": 10,
            "quantity": 1
         },
         {
            "product": "ломтик июльского неба",
            "price": 450,
            "quantity": 3
         }
      ]
   },
   {
      "order_id": 47230,
      "warehouse_name": "отель Лето",
      "highway_cost": -25,
      "products": [
         {
            "product": "ломтик июльского неба",
            "price": 450,
            "quantity": 1
         }
      ]
   },
   {
      "order_id": 64268,
      "warehouse_name": "хутор близ Диканьки",
      "highway_cost": -75,
      "products": [
         {
            "product": "автограф Стаса Барецкого",
            "price": 600,
            "quantity": 1
         },
         {
            "product": "зеленая пластинка",
            "price": 10,
            "quantity": 1
         },
         {
            "product": "подписка на suppi-блог",
            "price": 150,
            "quantity": 3
         }
      ]
   },
   {
      "order_id": 65559,
      "warehouse_name": "остров невезения",
      "highway_cost": -20,
      "products": [
         {
            "product": "статуэтка Ленина",
            "price": 200,
            "quantity": 3
         },
         {
            "product": "статуэтка Ленина",
            "price": 200,
            "quantity": 1
         }
      ]
   },
   {
      "order_id": 6535,
      "warehouse_name": "хутор близ Диканьки",
      "highway_cost": -105,
      "products": [
         {
            "product": "автограф Стаса Барецкого",
            "price": 600,
            "quantity": 2
         },
         {
            "product": "автограф Стаса Барецкого",
            "price": 600,
            "quantity": 2
         },
         {
            "product": "зеленая пластинка",
            "price": 10,
            "quantity": 3
         }
      ]
   },
   {
      "order_id": 77850,
      "warehouse_name": "хутор близ Диканьки",
      "highway_cost": -60,
      "products": [
         {
            "product": "билет в Израиль",
            "price": 1000,
            "quantity": 2
         },
         {
            "product": "автограф Стаса Барецкого",
            "price": 600,
            "quantity": 2
         }
      ]
   },
   {
      "order_id": 76803,
      "warehouse_name": "отель Лето",
      "highway_cost": -25,
      "products": [
         {
            "product": "зеленая пластинка",
            "price": 10,
            "quantity": 1
         }
      ]
   },
   {
      "order_id": 99246,
      "warehouse_name": "хутор близ Диканьки",
      "highway_cost": -45,
      "products": [
         {
            "product": "автограф Стаса Барецкого",
            "price": 600,
            "quantity": 3
         }
      ]
   },
   {
      "order_id": 96721,
      "warehouse_name": "Мордор",
      "highway_cost": -20,
      "products": [
         {
            "product": "ломтик июльского неба",
            "price": 450,
            "quantity": 2
         }
      ]
   },
   {
      "order_id": 88509,
      "warehouse_name": "гиперборея",
      "highway_cost": -60,
      "products": [
         {
            "product": "автограф Стаса Барецкого",
            "price": 600,
            "quantity": 1
         },
         {
            "product": "ломтик июльского неба",
            "price": 450,
            "quantity": 2
         }
      ]
   },
   {
      "order_id": 33780,
      "warehouse_name": "гиперборея",
      "highway_cost": -120,
      "products": [
         {
            "product": "подписка на suppi-блог",
            "price": 150,
            "quantity": 2
         },
         {
            "product": "статуэтка Ленина",
            "price": 200,
            "quantity": 2
         },
         {
            "product": "зеленая пластинка",
            "price": 10,
            "quantity": 2
         }
      ]
   },
   {
      "order_id": 70216,
      "warehouse_name": "хутор близ Диканьки",
      "highway_cost": -90,
      "products": [
         {
            "product": "плюмбус",
            "price": 250,
            "quantity": 2
         },
         {
            "product": "статуэтка Ленина",
            "price": 200,
            "quantity": 2
         },
         {
            "product": "статуэтка Ленина",
            "price": 200,
            "quantity": 2
         }
      ]
   },
   {
      "order_id": 26702,
      "warehouse_name": "Мордор",
      "highway_cost": -40,
      "products": [
         {
            "product": "статуэтка Ленина",
            "price": 200,
            "quantity": 1
         },
         {
            "product": "статуэтка Ленина",
            "price": 200,
            "quantity": 3
         }
      ]
   },
   {
      "order_id": 83889,
      "warehouse_name": "отель Лето",
      "highway_cost": -150,
      "products": [
         {
            "product": "зеленая пластинка",
            "price": 10,
            "quantity": 2
         },
         {
            "product": "автограф Стаса Барецкого",
            "price": 600,
            "quantity": 1
         },
         {
            "product": "статуэтка Ленина",
            "price": 200,
            "quantity": 3
         }
      ]
   },
   {
      "order_id": 16012,
      "warehouse_name": "отель Лето",
      "highway_cost": -50,
      "products": [
         {
            "product": "ломтик июльского неба",
            "price": 450,
            "quantity": 2
         }
      ]
   },
   {
      "order_id": 61521,
      "warehouse_name": "хутор близ Диканьки",
      "highway_cost": -45,
      "products": [
         {
            "product": "ломтик июльского неба",
            "price": 450,
            "quantity": 3
         }
      ]
   },
   {
      "order_id": 15237,
      "warehouse_name": "хутор близ Диканьки",
      "highway_cost": -60,
      "products": [
         {
            "product": "зеленая пластинка",
            "price": 10,
            "quantity": 1
         },
         {
            "product": "плюмбус",
            "price": 250,
            "quantity": 1
         },
         {
            "product": "зеленая пластинка",
            "price": 10,
            "quantity": 2
         }
      ]
   },
   {
      "order_id": 20645,
      "warehouse_name": "отель Лето",
      "highway_cost": -50,
      "products": [
         {
            "product": "ломтик июльского неба",
            "price": 450,
            "quantity": 2
         }
      ]
   },
   {
      "order_id": 70849,
      "warehouse_name": "остров невезения",
      "highway_cost": -25,
      "products": [
         {
            "product": "зеленая пластинка",
            "price": 10,
            "quantity": 1
         },
         {
            "product": "плюмбус",
            "price": 250,
            "quantity": 2
         },
         {
            "product": "зеленая пластинка",
            "price": 10,
            "quantity": 2
         }
      ]
   },
   {
      "order_id": 36764,
      "warehouse_name": "гиперборея",
      "highway_cost": -20,
      "products": [
         {
            "product": "подписка на suppi-блог",
            "price": 150,
            "quantity": 1
         }
      ]
   },
   {
      "order_id": 28106,
      "warehouse_name": "хутор близ Диканьки",
      "highway_cost": -30,
      "products": [
         {
            "product": "подписка на suppi-блог",
            "price": 150,
            "quantity": 1
         },
         {
            "product": "статуэтка Ленина",
            "price": 200,
            "quantity": 1
         }
      ]
   },
   {
      "order_id": 98100,
      "warehouse_name": "остров невезения",
      "highway_cost": -10,
      "products": [
         {
            "product": "автограф Стаса Барецкого",
            "price": 600,
            "quantity": 1
         },
         {
            "product": "билет в Израиль",
            "price": 1000,
            "quantity": 1
         }
      ]
   },
   {
      "order_id": 79293,
      "warehouse_name": "отель Лето",
      "highway_cost": -75,
      "products": [
         {
            "product": "статуэтка Ленина",
            "price": 200,
            "quantity": 1
         },
         {
            "product": "автограф Стаса Барецкого",
            "price": 600,
            "quantity": 1
         },
         {
            "product": "ломтик июльского неба",
            "price": 450,
            "quantity": 1
         }
      ]
   },
   {
      "order_id": 2930,
      "warehouse_name": "Мордор",
      "highway_cost": -30,
      "products": [
         {
            "product": "плюмбус",
            "price": 250,
            "quantity": 2
         },
         {
            "product": "плюмбус",
            "price": 250,
            "quantity": 1
         }
      ]
   },
   {
      "order_id": 124,
      "warehouse_name": "хутор близ Диканьки",
      "highway_cost": -45,
      "products": [
         {
            "product": "плюмбус",
            "price": 250,
            "quantity": 3
         }
      ]
   }
]
task_json = pd.read_json('trial_task.json')
df = pd.json_normalize(json,"products",['order_id', "warehouse_name", "highway_cost"])

# Задание 1
delivery_costs = {}
for index, row in task_json.iterrows():
   if row['warehouse_name'] in delivery_costs.keys():
       pass
   else:
       quantity = 0
       for product in row['products']:
            quantity += product['quantity']
       delivery_costs[row['warehouse_name']] = (row['highway_cost'] * -1) / quantity
num1 = pd.DataFrame(list(delivery_costs.items()), columns = ['warehouse_name', 'tarif'])
print(f'Задание 1: \n{num1}')



# Задание 2
num2 = df.merge(num1, how='left', on="warehouse_name")
num2['q2'] = num2.quantity * num2.tarif
num2['p2'] = num2.quantity * num2.price
num2['profit'] = num2.p2 - num2.q2
num_2 = num2[["product","p2", "quantity", "profit", "q2"]].groupby("product").sum().rename(columns={'p2': "expenses", "highway_cost": 'expenses', '2p': 'income'})
print(f'\nЗадание 2: \n{num_2}')

# Задание 3
num3 = num2[['order_id', 'profit']].groupby('order_id').sum()
print(f"\nЗадание 3: \n{num3}")
print(f"Срендняя прибыль заказов: {num3['profit'].mean()}\n")


# Задание 4
main_table = pd.DataFrame({'warehouse_name': [], 'product': [], 'quantity': [], 'profit': [],
                                'percent_profit_product_of_warehouse': [], 'accumulated_percent_profit_product_of_warehouse': []})
main_dict = {}

for index, row in task_json.iterrows():

  if row['warehouse_name']  not in main_dict.keys():
      main_dict[row['warehouse_name']] = {}
  for product in row['products']:
      if product['product'] in main_dict[row['warehouse_name']].keys():
          main_dict[row['warehouse_name']][product['product']]['quantity'] += product['quantity']
          main_dict[row['warehouse_name']][product['product']]['profit'] += product['quantity'] * (
                      product['price'] - delivery_costs[row['warehouse_name']])
      else:
          main_dict[row['warehouse_name']][product['product']]= {}
          main_dict[row['warehouse_name']][product['product']]['quantity'] = product['quantity']
          main_dict[row['warehouse_name']][product['product']]['profit'] = \
              product['quantity']*(product['price']-delivery_costs[row['warehouse_name']])
          main_dict[row['warehouse_name']][product['product']]['percent_profit_product_of_warehouse'] = 0


for warehouse in main_dict.keys():
  total_profit = 0

  for product in main_dict[warehouse].keys():
      if main_dict[warehouse][product]['profit'] > 0:
          total_profit += main_dict[warehouse][product]['profit']
  for product in main_dict[warehouse].keys():
      if main_dict[warehouse][product]['profit'] < 0:
          main_dict[warehouse][product]['percent_profit_product_of_warehouse'] = 0
      else:
          main_dict[warehouse][product]['percent_profit_product_of_warehouse'] = \
              math.floor(main_dict[warehouse][product]['profit'] * 10000 / total_profit) / 100



for warehouse in main_dict.keys():
  for product in main_dict[warehouse].keys():
      new_row = pd.DataFrame({'warehouse_name': [warehouse],
                              'product': [product],
                              'quantity': [main_dict[warehouse][product]['quantity']],
                              'profit': [main_dict[warehouse][product]['profit']],
                              'percent_profit_product_of_warehouse': [main_dict[warehouse][product]['percent_profit_product_of_warehouse']]})
      main_table = pd.concat([main_table, new_row], ignore_index=True)


print(f'Задание 4: \n{main_table}\n')


# Задание 5
main_table = main_table.sort_values(['warehouse_name', 'percent_profit_product_of_warehouse'], ascending=False)

print(f'Задание 5:  \n {main_table}\n')




# Задание 6
total_percent = 0
cur_warehouse = ""

for index, row in main_table.iterrows():
  if row['warehouse_name'] == cur_warehouse:
      total_percent += row['percent_profit_product_of_warehouse']
      main_table.at[index, 'accumulated_percent_profit_product_of_warehouse'] = total_percent
  else:
      total_percent = row['percent_profit_product_of_warehouse']
      cur_warehouse = row['warehouse_name']
      main_table.at[index, 'accumulated_percent_profit_product_of_warehouse'] = total_percent

main_table = main_table.reset_index(drop=True)


def funcfo6(percent):
   if percent <= 70:
      return 'A'
   elif percent <= 90:
      return 'B'
   else:
      return 'C'
main_table['category'] = main_table[
  'accumulated_percent_profit_product_of_warehouse'].apply(funcfo6)

print(f'Задание 6: \n{main_table}')


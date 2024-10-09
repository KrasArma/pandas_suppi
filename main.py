import pandas as pd
import math

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


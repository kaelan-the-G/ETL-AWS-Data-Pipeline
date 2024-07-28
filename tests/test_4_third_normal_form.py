#Global varibles needed for function

product_table=[]

#Function to test

from extract_load_transform.lambda_function import third_nf

#Importing test data

from mock_data.mock_data_lists import list_of_dicts_2nf

#Data variable for tests and module imports

import collections
order_table, product_table, order_products = third_nf(list_of_dicts_2nf)

#Unit test functions

def test_product_size_name_seperate():
    first_product_name = 'Iced americano'
    first_product_size = 'Regular'
    assert (product_table[0]['name'], product_table[0]['size']) == (first_product_name, first_product_size)

def test_price_is_pence():
    penny_price_first_product = 215
    assert product_table[0]['price'] == penny_price_first_product

def test_no_repeat_order_id():
    happy_path = 1
    id_list = []
    for entry in order_table:
        id_list += [entry['order_id']]
    count = [id_list.count(i) for i in id_list]
    for result in count:
        assert result == happy_path

def test_no_duplicate_product_size_pairs():
    count = collections.Counter([tuple(d.items()) for d in product_table])
    values = count.values()
    for result in values:
        if result > 1:
            raise Exception("Duplicate product id in products table")

def test_no_duplicate_order_product_rows(): #testing unique ID pairs
    count = collections.Counter([tuple(d.items()) for d in order_products])
    values = count.values()
    for result in values:
        if result > 1:
            raise Exception("Duplicate product id in products table")
        
def test_correct_order_product_id_any():
    correct_result = {'order_products_id': 2,
                'order_id': 0,
                'product_id': 1
            }
    assert order_products[1] == correct_result









    
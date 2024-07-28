#Function being tested

from extract_load_transform.lambda_function import first_nf

#Mock data before first normal form

from mock_data.mock_data_lists import list_of_dicts

#Output data varible used for both tests

output_dict_list = first_nf(list_of_dicts)

#Unit test functions

def test_indiv_dict_per_product():
    total_individual_projects = 27
    assert len(output_dict_list) == total_individual_projects

def test_orders_in_product_seperated():
    for indiv_dict in output_dict_list:
        if ',' in indiv_dict['order_details_string']:
            raise Exception('Order products not correctly seperated')



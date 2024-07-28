#Function being tested

from extract_load_transform.lambda_function import convert_csv

#Testing that sensitive has been removed

mock_raw_data = open("tests/mock_data/raw_data.csv")

def test_card_number_removed():
    test_list = convert_csv(mock_raw_data)
    test_list_str = str(test_list)
    assert 'card_number' not in test_list_str

def test_customer_name_removed():
    test_list = convert_csv(mock_raw_data)
    test_list_str = str(test_list)
    assert 'customer_name' not in test_list_str

    


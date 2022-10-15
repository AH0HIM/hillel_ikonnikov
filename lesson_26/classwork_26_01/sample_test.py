from test_config import config


def test_foo():
    target_server_ip = config['myapp']['servers']['main_server']
    print("\nCONFIG FILE OUTPUT: " + target_server_ip)

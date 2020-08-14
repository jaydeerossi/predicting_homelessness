import pandas as pd
import postal_address  as post


def load_health_and_hospitals_address_data():
    filename = 'S:\dcore-prj0107-SHARED\health_and_hospitals_addresses.csv'
    src_df = pd.read_csv(filename)
    return src_df.rename(columns={'Location 1': 'address_1'})[['address_1']]


def load_generic_address_data():
    filename = 'S:\dcore-prj0107-SHARED\sample_addresses.csv'
    src_df = pd.read_csv(filename)
    return src_df[['address_1']]


def standardize_address(df, address_col='address_1'):
    pass

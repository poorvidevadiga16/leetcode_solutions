import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    Find_products=(products['low_fats']=='Y')&(products['recyclable']=='Y')
    return products.loc[Find_products,['product_id']]
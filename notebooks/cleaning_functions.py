import pandas as pd 
import re


def clean_strings_column (df_column, str_replace_dictio):
    for k,v in str_replace_dictio.items():
        df_column = df_column.str.replace(k,v)
    return df_column

def clean_values_column (df, values_replace_dictio):
    for k,v in values_replace_dictio.items():
        df.replace(k,v,inplace = True)
    return df


def value_replace_dictio_regex(original_values_iterable, pattern_dictio, else_value):

    value_replace_clean = {}

    for k,v in pattern_dictio.items():
        for w in original_values_iterable:
            if re.search(k, w, flags=re.IGNORECASE):
                value_replace_clean[w] = v
            else:
                value_replace_clean[w] = else_value
    return value_replace_clean

def drop_rows_by_value(df,df_column,value_list):
    for l in value_list:
        df= df.drop(df[df_column == l].index)
    return df


def values_iterable_regex(df_column,pattern):
    regex_values = []
    for x in df_column:
        if re.search(pattern,x,flags=re.IGNORECASE):
            regex_values.append(x)
    regex_values = set(regex_values)
    return regex_values
import pandas as pd

def data_review(df):
    '''
    Función para revisar el tipo de datos contenido dentro de cada columna así como el porcentaje de nulos y la cantidad de filas que estan toalmente nulas.
    Recibe como parámetro el dataframe a examinar.
    '''

    mi_dict = {"nombre_campo": [], "tipo_datos": [], "no_nulos_%": [], "no_nulos_Qty": [], "nulos_%": [], "nulos_Qty": []}

    for columna in df.columns:
        porcentaje_no_nulos = (df[columna].count() / len(df)) * 100
        mi_dict["nombre_campo"].append(columna)
        mi_dict["tipo_datos"].append(df[columna].apply(type).unique())
        mi_dict["no_nulos_%"].append(round(porcentaje_no_nulos, 2))
        mi_dict["no_nulos_Qty"].append(df[columna].count())
        mi_dict["nulos_%"].append(round(100-porcentaje_no_nulos, 2))
        mi_dict['nulos_Qty'].append(df[columna].isnull().sum())

    df_info = pd.DataFrame(mi_dict)
    
    print("\nTotal full null rows: ", df.isna().all(axis=1).sum())
    print("\nTotal rows: ", len(df))
    
    return df_info

def replace_all_nulls(df):

    for column in df.columns:
        mask = df[column].notnull()
        dtype = df[column][mask].apply(type).unique()

        if dtype[0] == str:
            df[column] = df[column].fillna('No data')
        if dtype[0] == float:
            mean = df[column].mean()
            df[column] = df[column].fillna(mean)
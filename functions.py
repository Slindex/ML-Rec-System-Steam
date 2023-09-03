import pandas as pd


path_userdata = 'data/functions/userdata.csv'
path_countreviews = 'data/functions/countreviews.csv'
path_genre = 'data/functions/genre.csv'
path_userforgenre = 'data/functions/userforgenre.csv'
path_developer = 'data/functions/developer.csv'

df_userdata = pd.read_csv(path_userdata)
df_countreviews = pd.read_csv(path_countreviews)
df_genre = pd.read_csv(path_genre)
df_ufgenre = pd.read_csv(path_userforgenre)
df_developer = pd.read_csv(path_developer)


def userdata(User_id: str):

    spent = df_userdata['total_spent'][df_userdata['user_id'] == User_id]
    total_spent = float(spent.iloc[0])

    item_qty = df_userdata['total_items'][df_userdata['user_id'] == User_id]
    total_items = int(item_qty.iloc[0])

    recom_qty = df_userdata['total_recom'][df_userdata['user_id'] == User_id]
    total_recom = int(recom_qty.iloc[0])

    recom_per = (total_recom / total_items)*100

    info = {'Total_spent': total_spent,
            'Total_items': total_items,
            'Recommend_percentage': recom_per}
    
    return info

def countreviews(startdate: str, endate: str):

    df_countreviews['posted'] = pd.to_datetime(df_countreviews['posted'])

    start_date = pd.to_datetime(startdate)
    end_date = pd.to_datetime(endate)

    filtered_df = df_countreviews[(df_countreviews['posted'] >= start_date) & (df_countreviews['posted'] <= end_date)]

    users_qty = len(filtered_df['user_id'].unique())
    reviews_qty = len(df_countreviews['user_id'].unique())
    recom_per = round((users_qty / reviews_qty) * 100, 2)

    info = {'users_qty': users_qty,
            'recommend_%': recom_per}
    
    return info

def genre(genre: str):

    ranking = df_genre['ranking'][df_genre['genres'] == genre]
    ranking = int(ranking.iloc[0])

    ptf = df_genre['playtime_forever'][df_genre['genres'] == genre]
    ptf = int(ptf.iloc[0])

    info = {'Ranking': ranking,
            'Total_playtime(h)': ptf}

    return info

def userforgenre(genre:str):

    df = df_ufgenre[df_ufgenre['genres'] == genre]
    df = df.iloc[0:5]

    user_1 = df['user_id'].iloc[0]
    url_1 = df['user_url'].iloc[0]
    user_2 = df['user_id'].iloc[1]
    url_2 = df['user_url'].iloc[1]
    user_3 = df['user_id'].iloc[2]
    url_3 = df['user_url'].iloc[2]
    user_4 = df['user_id'].iloc[3]
    url_4 = df['user_url'].iloc[3]
    user_5 = df['user_id'].iloc[4]
    url_5 = df['user_url'].iloc[4]

    info = [{'user_id': user_1, 'user_url': url_1},
            {'user_id': user_2, 'user_url': url_2},
            {'user_id': user_3, 'user_url': url_3},
            {'user_id': user_4, 'user_url': url_4},
            {'user_id': user_5, 'user_url': url_5}]

    return info

def developer(dev: str):

    info = []

    df = df_developer
    df['free_%'] = round((df['free_qty'] / df['items_qty'])*100, 2)
    df = df[df['developer'] == dev]
    df = df.sort_values(by='year', ascending=False).reset_index(drop=True)
    df = df[['year', 'free_%']]

    for _, row in df.iterrows():
        row_data = dict(row)
        info.append(row_data)
    
    info = [{'year': int(dic['year']), 'free_%': dic['free_%']} for dic in info]

    return info
import pandas as pd


path_userdata = 'data/functions/userdata.csv'
df_userdata = pd.read_csv(path_userdata)

path_countreviews = 'data/functions/countreviews.csv'
df_countreviews = pd.read_csv(path_countreviews)

path_genre = 'data/functions/genre.csv'
df_genre = pd.read_csv(path_genre)


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
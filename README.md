# BackEnd Development and Cosine Similarity ML Model for Steam

This project is a practical knowledge recopilation for the development, deploy and testing of an API using FastAPI framework for hosting multiple endpoint queries aswell as a Cosine Similarity Machine Learning model.

Please refer to the following table for check all the files content:

| ID | Name          | Type   | Description                                                           |
|----|---------------|--------|-----------------------------------------------------------------------|
| 1  | data          | .csv/npy | Contains summarized data for endpoints queries and ML model operation|
| 2  | ETL | .ipynb | Contains Notebooks with the ETL process for each Steam API Json                 |
| 3  | ETL/utils | .py | Contains utility functions used for the ETL process                |
| 4  | .gitignore | .git | Contains ignored raw data (Too heavy for be uploaded to Render) and a testing notebook|
| 5  | Dockerfile | .dockerfile | Docker instructions for environment set-up|
| 6  | functions | .py | Contains functions used by the BackEnd (main) file and its end points|
| 7  | main | .py | Contains HTTP request methods for BackEnd functionality|
| 8  | ml-model | .ipynb | Step by step process for ML-model set up, fitting and memory usage optimization|
| 9  | requirements | .txt | Libraries required for backend functioning |

<br>

> **IMPORTANT:** Additional Libraries were used for data processing and ML model development but weren't included in the requirements file

## Raw Data

Raw data were parsed from Json files to csv and npy formats. An example of the general Json files structure is showed in the following block:

```json
{
  "user_id": "76561198030389591",
  "items_count": 12,
  "steam_id": "76561198030389591",
  "user_url": "http://steamcommunity.com/profiles/76561198030389591",
  "items": [
    {
      "item_id": "205790",
      "item_name": "Dota 2 Test",
      "playtime_forever": 0,
      "playtime_2weeks": 0
    },
    {
      "item_id": "96800",
      "item_name": "Nexuiz",
      "playtime_forever": 19,
      "playtime_2weeks": 0
    },
    {
      "item_id": "216370",
      "item_name": "Nexuiz Beta",
      "playtime_forever": 7,
      "playtime_2weeks": 0
    }
  ]
}
```

## Datasets

This project involved 3 big Json files extracted from Steam API about Australian users and games data published at the time. In general terms the information contained in this file were:

* User Reviews
* User Items Acquired
* Steam Games Data

The following section contains detailed information about every dataset and their initial state of art (Data types and Null values).

### Steam Games

The following table contains the summarized information about the dataset attributes:


| Column          | dType                                   | No_null_%  | No_null_Qty  | Null_%  | Null_Qty  |
|-----------------|-----------------------------------------|------------|--------------|---------|-----------|
| publisher       | [<class 'float'>, <class 'str'>]        | 20.00      | 24083        | 80.00   | 96362     |
| genres          | [<class 'float'>, <class 'list'>]       | 23.95      | 28852        | 76.05   | 91593     |
| app_name        | [<class 'float'>, <class 'str'>]        | 26.68      | 32133        | 73.32   | 88312     |
| title           | [<class 'float'>, <class 'str'>]        | 24.98      | 30085        | 75.02   | 90360     |
| url             | [<class 'float'>, <class 'str'>]        | 26.68      | 32135        | 73.32   | 88310     |
| release_date    | [<class 'float'>, <class 'str'>]        | 24.96      | 30068        | 75.04   | 90377     |
| tags            | [<class 'float'>, <class 'list'>]       | 26.54      | 31972        | 73.46   | 88473     |
| reviews_url     | [<class 'float'>, <class 'str'>]        | 26.68      | 32133        | 73.32   | 88312     |
| discount_price  | [<class 'float'>]                       | 0.19       | 225          | 99.81   | 120220    |
| specs           | [<class 'float'>, <class 'list'>]       | 26.12      | 31465        | 73.88   | 88980     |
| price           | [<class 'float'>, <class 'str'>]        | 25.54      | 30758        | 74.46   | 89687     |
| early_access    | [<class 'float'>, <class 'bool'>]       | 26.68      | 32135        | 73.32   | 88310     |
| id              | [<class 'float'>, <class 'str'>]        | 26.68      | 32133        | 73.32   | 88312     |
| metascore       | [<class 'float'>, <class 'int'>, <class 'str'>] | 2.22  | 2677      | 97.78   | 117768    |
| developer       | [<class 'float'>, <class 'str'>]        | 23.94      | 28836        | 76.06   | 91609     |
| user_id         | [<class 'str'>, <class 'float'>]        | 73.32      | 88310        | 26.68   | 32135     |
| steam_id        | [<class 'str'>, <class 'float'>]        | 73.32      | 88310        | 26.68   | 32135     |
| items           | [<class 'list'>, <class 'float'>]       | 73.32      | 88310        | 26.68   | 32135     |
| items_count     | [<class 'float'>]                       | 73.32      | 88310        | 26.68   | 32135     |

<br>

Float values in the majority of columns represent null values and were managed considering the following criteria:

* Columns with more than 90% null values - **Columns Eliminated**
* Records with 15 or more null values - **Records Eliminated**
* Columns with less than 0.5% null values - **Records Eliminated**
* Columns with redundant information (Equal to another column or obtainable from other dataset) - **Columns Eliminated**
* Columns with null values between 5% and 30% - **Imputed Values** ('No data' for str and mean value for float and int)

Some special characters were treated with the following criteria:

* Price column values from the following list were imputed to zero:
    - Free To Play
    - Free to Play
    - Free
    - Free Demo
    - Play for Free!
    - Install Now
    - Play WARMACHINE: Tactics Demo
    - Free Mod
    - Install Theme
    - Third-party
    - Play Now
    - Free HITMAN™ Holiday Pack
    - Play the Demo
    - Free to Try
    - Free Movie
    - Free to Use

<br>

* Price column values with 'Starting at $499.00' - **Imputed to 499**
* Price column values with 'Starting at $449.00' - **Imputed to 449**

Resulting DataFrame after Null values management and transformations:

| Column          | dType             | No_Null_% | No_Null_Qty | Null_% | Null_Qty |
|-----------------|-------------------|-----------|-------------|--------|----------|
| publisher       | [<class 'str'>]  | 100.0     | 32132       | 0.0    | 0        |
| genres          | [<class 'str'>]  | 100.0     | 32132       | 0.0    | 0        |
| app_name        | [<class 'str'>]  | 100.0     | 32132       | 0.0    | 0        |
| url             | [<class 'str'>]  | 100.0     | 32132       | 0.0    | 0        |
| release_date    | [<class 'str'>]  | 100.0     | 32132       | 0.0    | 0        |
| tags            | [<class 'str'>]  | 100.0     | 32132       | 0.0    | 0        |
| reviews_url     | [<class 'str'>]  | 100.0     | 32132       | 0.0    | 0        |
| specs           | [<class 'str'>]  | 100.0     | 32132       | 0.0    | 0        |
| price           | [<class 'float'>]| 100.0     | 32132       | 0.0    | 0        |
| early_access    | [<class 'bool'>] | 100.0     | 32132       | 0.0    | 0        |
| id              | [<class 'int'>]  | 100.0     | 32132       | 0.0    | 0        |
| developer       | [<class 'str'>]  | 100.0     | 32132       | 0.0    | 0        |


### User Items

The following table contains the summarized information about the dataset attributes:

| Column           | dType             | No_Null_% | No_Null_Qty | Null_% | Null_Qty |
|------------------|-------------------|-----------|-------------|--------|----------|
| item_id          | [<class 'int'>]  | 100.0     | 5153209     | 0.0    | 0        |
| item_name        | [<class 'str'>]  | 100.0     | 5153209     | 0.0    | 0        |
| playtime_forever | [<class 'int'>]  | 100.0     | 5153209     | 0.0    | 0        |
| playtime_2weeks  | [<class 'int'>]  | 100.0     | 5153209     | 0.0    | 0        |
| user_id          | [<class 'str'>]  | 100.0     | 5153209     | 0.0    | 0        |
| items_count      | [<class 'int'>]  | 100.0     | 5153209     | 0.0    | 0        |
| steam_id         | [<class 'int'>]  | 100.0     | 5153209     | 0.0    | 0        |
| user_url         | [<class 'str'>]  | 100.0     | 5153209     | 0.0    | 0        |

This dataset had no Null values, only **59104** duplicated records that were removed. No further data transformation were applied for this dataset.

### User Reviews

The following table contains the summarized information about the dataset attributes:

| Column       | dType                             | No_Null_% | No_Null_Qty | Null_%  | Null_Qty |
|--------------|-----------------------------------|-----------|-------------|---------|----------|
| funny        | [<class 'float'>, <class 'str'>] | 13.75     | 8150        | 86.25   | 51125    |
| posted       | [<class 'str'>]                  | 100.00    | 59275       | 0.00    | 0        |
| last_edited  | [<class 'float'>, <class 'str'>] | 10.36     | 6140        | 89.64   | 53135    |
| item_id      | [<class 'int'>]                  | 100.00    | 59275       | 0.00    | 0        |
| helpful      | [<class 'str'>]                  | 100.00    | 59275       | 0.00    | 0        |
| recommend    | [<class 'bool'>]                 | 100.00    | 59275       | 0.00    | 0        |
| review       | [<class 'str'>]                  | 100.00    | 59275       | 0.00    | 0        |
| user_id      | [<class 'str'>]                  | 100.00    | 59275       | 0.00    | 0        |
| user_url     | [<class 'str'>]                  | 100.00    | 59275       | 0.00    | 0        |

**874** Duplicated records were eliminated. Float values in columns represent null values and were managed considering the following criteria:

* Columns with more than 85% null values - **Columns Eliminated**

Resulting dataframe:

| Column       | dType                             | No_Null_% | No_Null_Qty | Null_%  | Null_Qty |
|--------------|-----------------------------------|-----------|-------------|---------|----------|
| posted       | [<class 'str'>]                  | 100.00    | 58401       | 0.00    | 0        |
| item_id      | [<class 'int'>]                  | 100.00    | 58401       | 0.00    | 0        |
| helpful      | [<class 'str'>]                  | 100.00    | 58401       | 0.00    | 0        |
| recommend    | [<class 'bool'>]                 | 100.00    | 58401       | 0.00    | 0        |
| review       | [<class 'str'>]                  | 100.00    | 58401       | 0.00    | 0        |
| user_id      | [<class 'str'>]                  | 100.00    | 58401       | 0.00    | 0        |
| user_url     | [<class 'str'>]                  | 100.00    | 58401       | 0.00    | 0        |
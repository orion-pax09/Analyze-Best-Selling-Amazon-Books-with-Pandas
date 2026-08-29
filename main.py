import pandas as pd
df = pd.read_csv("bestsellers with categories.csv")
new_df = df.copy()
new_df = new_df.drop_duplicates()
new_df = new_df.rename(columns={"Name": "Title", "Year": "Publication Year", "User Rating": "Rating"})
new_df["Price"] = new_df["Price"].astype(float)
most_Selling_books = new_df["Author"].value_counts()
most_rating_books =new_df.loc[new_df["Rating"] >=4.8 , ["Title" , "Author"]]
genre_performance = new_df.groupby("Genre")["Rating"].mean()
bestperformance = genre_performance.idxmax()

most_rating_books.to_csv("cleaned_bestsellers.csv" , index=False)
most_rating_books.to_csv("high_rated_books.csv" , index=False)
genre_performance.to_csv("Genre_performance_avg.csv" , index=False)

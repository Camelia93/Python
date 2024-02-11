import pandas
import pandas as pd


df = pd.read_csv(r"C:\Users\valil\Desktop\programe\Squirrel_Data.csv")

# Specify column names
color_column = 'Primary Fur Color'
age_column = 'Age'


gray_squirrels = df[df[color_column] == 'Gray']
cinnamon_squirrels = df[df[color_column] == "Cinnamon"]
black_squirrels = df[df[color_column] == "Black"]
no_gray_squirrels = len(gray_squirrels)
no_cinnamon_squirrels = len(cinnamon_squirrels)
no_black_squirrels= len(black_squirrels)


data_dict = {
    color_column: ['Gray', 'Cinnamon', 'Black'],
    'Count': [no_gray_squirrels, no_cinnamon_squirrels, no_black_squirrels]
}

data_dataframe = pd.DataFrame(data_dict)

# Add the 'Age' column to the new DataFrame
#data_dataframe[age_column] = df.groupby(color_column)[age_column].mean().values

# Save the new DataFrame to CSV
data_dataframe.to_csv("new_data.csv", index=False)
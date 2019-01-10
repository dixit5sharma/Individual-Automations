import pandas as pd

df = pd.read_csv("Files\\censuspopdata.csv")
print(df.head())        # Prints first 5 Rows - <class 'pandas.core.frame.DataFrame'>

Songs = {"Heading1":["a","b","c","d","e"],"Heading2":["p","o","i","u","y"],"Heading3":[11,12,13,14,15]}
s_frame = pd.DataFrame(Songs)
print(s_frame)

x = s_frame[["Heading1"]]       # Making new DataFrame from existing one with particular columns
print(x)

cell_1 = s_frame.iloc[0,0]              # loc method is for integer location arguments
print("Cell-1 =",cell_1)

cell_2 = s_frame.loc[0,"Heading2"]      # loc method is for string column location arguments
print("Cell-2 =",cell_2)

new = s_frame.loc[0:2,"Heading1":"Heading2"]        # Dataframe slicing
print(new)

print(s_frame["Heading3"]>=13)      # Boolean Dataframe

save_this = s_frame[s_frame["Heading3"]>=13]        # DataFrame formed where Boolena is True
print(save_this)
save_this.to_csv("Files\\Heading3_GreaterThan13.csv")       # Use "to_csv" method to save DataFrame to .csv
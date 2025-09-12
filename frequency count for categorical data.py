#In this exercise, you're going to look at the 'Borough', 'State', and 'Site Fill' columns to make sure all the values in there are valid.
#When looking at the output, do a sanity check: Are all values in the 'State' column from NY, for example? Since the dataset consists 
#of applications filed in NY, you would expect this to be the case.

Print the value counts for:
The 'Borough' column.
The 'State' column.
The 'Site Fill' column.

# Print the value counts for 'Borough'
print(df['Borough'].value_counts(dropna=False))

# Print the value_counts for 'State'
print(df['State'].value_counts(dropna=False))

# Print the value counts for 'Site Fill'
print(df['Site Fill'].value_counts(dropna=False))

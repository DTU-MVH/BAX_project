#!/opt/homebrew/bin/python3.11
import os
import pandas as pd

Energies_4S0O = pd.read_csv("22117/energies_4S0O.csv", sep=",")
Energies_2K7W = pd.read_csv("22117/energies_2K7W.csv", sep=",")

df_4S0O = pd.DataFrame(Energies_4S0O).drop(["WT residue type", "chain ID"], axis = 1).T
df_2K7W = pd.DataFrame(Energies_2K7W).drop(["WT residue type", "chain ID"], axis = 1).T

#The first 20 residues are from BCL2 peptide, as should not be compared
df_2K7W = df_2K7W.drop([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], axis = 1)
#Now the length of df_4S0O is the same as df_2K7W
#print(df_2K7W.size, df_4S0O.size)

print(df_4S0O.columns)

df_diff = pd.DataFrame()
for res in range(192):
    """if res in range(10):
        print(df_2K7W[res+20].subtract(df_4S0O[res], fill_value=0.0))"""
    df_diff = pd.concat([df_diff, df_2K7W[res+20].subtract(df_4S0O[res], fill_value=0.0)], axis=1)

new_columns = [str(i) for i in range(192)]
df_diff.columns = new_columns

df_diff.T.to_csv("22117/energies_diff_4S0O_2K7W.csv", sep=";")
print(df_diff)





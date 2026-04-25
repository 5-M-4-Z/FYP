import os
import pandas as pd

print("The file is running")


# Creating dictionary for the master data
master_data = {
                    "Patch Width": [],
                    "Patch Length": [],
                    "Patch X": [],
                    "Patch Y": [],
                    "Feed X": [],
                    "Feed Y": [],
                    "Truncation along X": [],
                    "Truncation along Y": [],
                    "Frequency value": [],
                    "S11 dB value": [],
                    "S22 dB value": [],
                    "S33 dB value": [],
                    "S44 dB value": []
                }

# following code would generate an excel file that will consist of master data of the raw data from feed x and y

lst = [r"D:\Meesam\FYP\4-Patch\Data Sets\Datasets-3 level framework\S11 Datasets"]

for folder_path_1 in lst:
    
    
    real_path = folder_path_1
    # List all files in the folder path
    for filename in os.listdir(real_path):
        # Create full path
        full_path = os.path.join(real_path, filename)

        if (os.path.isfile(full_path)) == False:
            print("no file exist")
        else:
            # print(filename)
            # Read the Excel file
            df = pd.read_csv(full_path)

            # Loop through each column and print as a list
            for col in df.columns:
                column_list = df[col].tolist()
                # print(f"Column name: {col}")
                # print(f"Data: {column_list}\n")
                if col == "Freq [GHz]":
                    S11_freq = column_list.copy()
                elif col == "dB(S(1,1)) []":
                    freq_db11 = column_list.copy()
                elif col == "dB(S(2,2)) []":
                    freq_db22 = column_list.copy()
                elif col == "dB(S(3,3)) []":
                    freq_db33 = column_list.copy()
                elif col == "dB(S(4,4)) []":
                    freq_db44 = column_list.copy()
                else:
                    print("No matching column found")
            
            flag = 0
            for ind in range(len(S11_freq)):
                if abs(S11_freq[ind] - 1.575333) < 0.000001:
                    temp11 = S11_freq[ind]
                    temp12 = freq_db11[ind]
                    temp13 = freq_db22[ind]
                    temp14 = freq_db33[ind]
                    temp15 = freq_db44[ind]
                    flag = 1

                elif abs(S11_freq[ind] - 1.575666) < 0.000001:
                    temp21 = S11_freq[ind]
                    temp22 = freq_db11[ind]
                    temp23 = freq_db22[ind]
                    temp24 = freq_db33[ind]
                    temp25 = freq_db44[ind]
                    flag = 2
                if flag == 2:
                    break

            master_data["Frequency value"].append((temp11+temp21)/2)
            master_data["S11 dB value"].append((temp12+temp22)/2)
            master_data["S22 dB value"].append((temp13+temp23)/2)
            master_data["S33 dB value"].append((temp14+temp24)/2)
            master_data["S44 dB value"].append((temp15+temp25)/2)


            temp = filename.split("--")
            lst_of_filename = temp[1].split(", ")
            for i in range(len(lst_of_filename)):
                name, value = lst_of_filename[i].split("=")
                if name.strip() == "hole_x":
                    master_data["Feed X"].append(float(value.strip()))
                elif name.strip() == "hole_y":
                    master_data["Feed Y"].append(float(value.strip()))
                elif name.strip() == "trunc_x":
                    master_data["Truncation along X"].append(float(value.strip()))
                elif name.strip() == "trunc_y":
                    master_data["Truncation along Y"].append(float(value.strip()))
                elif name.strip() == "patch_xsize":
                    master_data["Patch Width"].append(float(value.strip()))
                elif name.strip() == "patch_ysize":
                    master_data["Patch Length"].append(float(value.strip()))
                elif name.strip() == "patch_x":
                    master_data["Patch X"].append(float(value.strip()))
                elif name.strip() == "patch_y":
                    value = value.split(".csv")[0]
                    master_data["Patch Y"].append(float(value.strip()))

            # print(filename)
            # print(master_data)
            


            


        
                
        


    

print("Master data set created successfully")

for key in master_data:
    print(len(master_data[key]))

df = pd.DataFrame(master_data)

# Save to Excel file
df.to_excel("Master Data File - 3 Level Framework.xlsx", index=False)

print("Excel file created successfully!")
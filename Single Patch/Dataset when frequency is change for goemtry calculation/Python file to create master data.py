import os
import pandas as pd

print("The file is running")

# List of all the parameter for the single patch
# frequency = 1575.42*(10**6)
# mil = 0.0254

# patch_width = 45
# patch_length = 45

# ground_width = 90
# ground_length = 90

# patch_x = (ground_width - patch_width) / 2  # (90-45)/2 = 22.5 mm
# patch_y = (ground_length - patch_length) / 2  # (90-45)/2 = 22.5 mm

# # feed x and y when patch's center is starting from origin
# feed_x_relative = 0.0
# feed_y_relative = -13.3873

# # feed x and y relative to the patch , which is reltive to the ground
# feed_x = patch_x + feed_x_relative + (patch_width/2)
# feed_y = patch_y + feed_y_relative + (patch_length/2)

# truncated_length = 6

# # Top-left truncated triangle (near top-left corner of patch)
# truncatedTopLeft_x = [patch_x, patch_x + truncated_length, patch_x]
# truncatedTopLeft_y = [patch_y + patch_length, patch_y + patch_length, patch_y + patch_length - truncated_length]

# # Bottom-right truncated triangle (near bottom-right corner of patch)  
# truncatedBottomRight_x = [patch_x + patch_width, patch_x + patch_width, patch_x + patch_width - truncated_length]
# truncatedBottomRight_y = [patch_y, patch_y + truncated_length, patch_y]



# freq = freq


















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
                    "Peak Frequency": [],
                    "S11 dB value": [],
                    "Axial Ratio at Fr (dB)": []
                }

# following code would generate an excel file that will consist of master data of the raw data from feed x and y

lst = [r"D:\Meesam\FYP\Single Patch\Dataset when frequency is change for goemtry calculation"
       ]

for folder_path_1 in lst:
    
    for _ in range(2):
        
        if _ == 0:
            real_path = folder_path_1 + "\S11 Parameter"
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
                            freq_db = column_list.copy()
                    ind = freq_db.index(min(freq_db))

                    # Finding lower and upper bound for the frequency that had highest dB gain from the cs file
                    # 0.00015 = step size in the csv file and threshold bandwidth = 0.00015*27 = 0.00405 GHz
                    peak_freq = S11_freq[ind]
                    
                    # breaking the file name to get the changed input parameter
                    
                    path_to_list = full_path.split("\\")
                    path_to_list = path_to_list[0:-1]
                    # print("The name of the path in list format is:", name = filename[0:-4].split("_"))
                    # Following pieces of code update parameter for single patch width and length
                    if path_to_list == ["D:", "Meesam", "FYP", "Single Patch", "Dataset when frequency is change for goemtry calculation", 'S11 Parameter']:
                        name = filename[0:-4].split("_")
                        freq = float(name[name.index("Freqo") + 1])

                        subs_height = 0.508
                        subs_e = 3.55
                        mil = 25.4 / 1000

                        patch_w = ((3e11) / (2 * freq)) * ((2 / (subs_e + 1))**(0.5))

                        e_reff = ((subs_e + 1) / 2) + (((subs_e - 1) / 2) * (1 + 12 * (subs_height / patch_w))**(-0.5))

                        delta_l = (subs_height * 0.412 * (e_reff + 0.3) * (patch_w / subs_height + 0.264)) / ((e_reff - 0.258) * (patch_w / subs_height + 0.8))

                        patch_l = ((3e11) / (2 * freq * (e_reff**(0.5)))) - (2 * delta_l)

                        ground_w = 2 * patch_w
                        ground_l = 2 * patch_l

                        feed_x = patch_w / 2
                        feed_y = patch_l / (2 * (e_reff**(0.5)))

                        Q0 = (3e11 * (subs_e**(0.5))) / (4 * freq * subs_height)

                        truncated_length = patch_l * ((1 / (2 * Q0))**(0.5))

                        # Translating feed point(patch centered on ground plane)
                        feed_x = feed_x + (ground_w - patch_w) / 2
                        feed_y = feed_y + (ground_l - patch_l) / 2

                        antenna_x = (ground_w - patch_w) / 2
                        antenna_y = (ground_l - patch_l) / 2

                        truncatedTopLeft_x = [antenna_x, antenna_x + truncated_length, antenna_x]

                        truncatedTopLeft_y = [antenna_y + patch_l,antenna_y + patch_l,antenna_y + patch_l - truncated_length]

                        truncatedBottomRight_x = [antenna_x + patch_w, antenna_x + patch_w, antenna_x + patch_w - truncated_length]

                        truncatedBottomRight_y = [antenna_y, antenna_y + truncated_length, antenna_y]


                        master_data["Patch Width"].append(patch_w)
                        master_data["Patch Length"].append(patch_l)
                        master_data["Patch X"].append(antenna_x)
                        master_data["Patch Y"].append(antenna_y)
                        master_data["Feed X"].append(feed_x)
                        master_data["Feed Y"].append(feed_y)
                        master_data["Truncation along X"].append(truncated_length)
                        master_data["Truncation along Y"].append(truncated_length)
                        master_data["Peak Frequency"].append(peak_freq)
                        master_data["S11 dB value"].append(freq_db[ind])



                    else:
                        print(path_to_list, "alskd", filename)


                # for key in master_data:
                #     print("The length of",key,"=",len(master_data[key]))
        elif _ == 1:
            real_path = folder_path_1 + "\Axial Ratio Parameter"
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
                        if col == "Theta [deg]":
                            theta = column_list.copy()
                        elif col == "dB(AxialRatioValue) []":
                            axial_db = column_list.copy()
                    axial_db_value = axial_db[theta.index(0)]
                    
                    path_to_list = full_path.split("\\")
                    path_to_list = path_to_list[0:-1]
                    # Following pieces of code update parameter for single patch width and length
                    if path_to_list == ["D:", "Meesam", "FYP", "Single Patch", "Dataset when frequency is change for goemtry calculation", 'Axial Ratio Parameter']:
                        master_data["Axial Ratio at Fr (dB)"].append(axial_db_value)


                    else:
                        print(path_to_list, "alskd", filename)

                
        


    

print("Master data set created successfully")

for key in master_data:
    print(len(master_data[key]))

df = pd.DataFrame(master_data)

# Save to Excel file
df.to_excel("Master Data file.xlsx", index=False)

print("Excel file created successfully!")

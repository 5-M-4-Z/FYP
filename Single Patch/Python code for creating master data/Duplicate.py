import os
import pandas as pd

# List of all the parameter for the single patch
frequency = 1575.42*(10**6)
mil = 0.0254

patch_width = 45
patch_length = 45

ground_width = 90
ground_length = 90

patch_x = (ground_width - patch_width) / 2  # (90-45)/2 = 22.5 mm
patch_y = (ground_length - patch_length) / 2  # (90-45)/2 = 22.5 mm

# feed x and y when patch's center is starting from origin
feed_x_relative = 0.0
feed_y_relative = -13.3873

# feed x and y relative to the patch , which is reltive to the ground
feed_x = patch_x + feed_x_relative + (patch_width/2)
feed_y = patch_y + feed_y_relative + (patch_length/2)

truncated_length = 6

# Top-left truncated triangle (near top-left corner of patch)
truncatedTopLeft_x = [patch_x, patch_x + truncated_length, patch_x]
truncatedTopLeft_y = [patch_y + patch_length, patch_y + patch_length, patch_y + patch_length - truncated_length]

# Bottom-right truncated triangle (near bottom-right corner of patch)  
truncatedBottomRight_x = [patch_x + patch_width, patch_x + patch_width, patch_x + patch_width - truncated_length]
truncatedBottomRight_y = [patch_y, patch_y + truncated_length, patch_y]

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
                    "Frequency": [],
                    "S11 dB value": [],
                    "Axial Ratio at Fr (dB)": []
                }

# following code would generate an excel file that will consist of master data of the raw data from feed x and y

lst = [r"D:\UNI\FYP\Single Patch\Datasets\Feed x and y",
       r"D:\UNI\FYP\Single Patch\Datasets\Patch Width & Length",
       r"D:\UNI\FYP\Single Patch\Datasets\Truncation\Dataset - Truncation (0-25 mil)"
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
                    low_bound = round(peak_freq - (0.00015*27),6)
                    upper_bound = round(peak_freq + (0.00015*27),6)
                    lb_ind = S11_freq.index(low_bound)
                    up_ind = S11_freq.index(upper_bound)
                    
                    # The following list include the data points for the specified range
                    S11_freq = S11_freq[lb_ind:up_ind+1]
                    freq_db = freq_db[lb_ind:up_ind+1]

                    # breaking the file name to get the changed input parameter
                    
                    path_to_list = full_path.split("\\")
                    path_to_list = path_to_list[0:-1]
                    # print("The name of the path in list format is:", name = filename[0:-4].split("_"))
                    # Following pieces of code update parameter for single patch width and length
                    if path_to_list == ['D:', 'UNI', 'FYP', 'Single Patch', 'Datasets', 'Patch Width & Length', 'S11 Parameter']:
                        name = filename[0:-4].split("_")
                        patch_width = float(name[name.index("patchW") + 1])
                        patch_length = float(name[name.index("patchL") + 1])
                        

                        for i in range(len(S11_freq)):
                            master_data["Patch Width"].append(patch_width)
                            master_data["Patch Length"].append(patch_length)
                            master_data["Patch X"].append(patch_x)
                            master_data["Patch Y"].append(patch_y)
                            master_data["Feed X"].append(feed_x)
                            master_data["Feed Y"].append(feed_y)
                            master_data["Truncation along X"].append(truncated_length)
                            master_data["Truncation along Y"].append(truncated_length)
                            master_data["Peak Frequency"].append(peak_freq)
                            master_data["Frequency"].append(S11_freq[i])
                            master_data["S11 dB value"].append(freq_db[i])  

                    elif path_to_list == ['D:', 'UNI', 'FYP', 'Single Patch', 'Datasets', 'Feed x and y', 'S11 Parameter']:
                        name = filename[0:-4].split("_")
                        feed_x = float(name[name.index("feedX") + 1])
                        feed_y = float(name[name.index("feedY") + 1])
                        

                        for i in range(len(S11_freq)):
                            master_data["Patch Width"].append(patch_width)
                            master_data["Patch Length"].append(patch_length)
                            master_data["Patch X"].append(patch_x)
                            master_data["Patch Y"].append(patch_y)
                            master_data["Feed X"].append(feed_x)
                            master_data["Feed Y"].append(feed_y)
                            master_data["Truncation along X"].append(truncated_length)
                            master_data["Truncation along Y"].append(truncated_length)
                            master_data["Peak Frequency"].append(peak_freq)
                            master_data["Frequency"].append(S11_freq[i])
                            master_data["S11 dB value"].append(freq_db[i])

                    elif path_to_list == ['D:', 'UNI', 'FYP', 'Single Patch', 'Datasets', 'Truncation', 'Dataset - Truncation (0-25 mil)', 'S11 Parameter']:
                        name = filename[0:-4].split("_")
                        truncX = float(name[name.index("truncX") + 1])
                        truncY = float(name[name.index("truncY") + 1])
                        

                        for i in range(len(S11_freq)):
                            master_data["Patch Width"].append(patch_width)
                            master_data["Patch Length"].append(patch_length)
                            master_data["Patch X"].append(patch_x)
                            master_data["Patch Y"].append(patch_y)
                            master_data["Feed X"].append(feed_x)
                            master_data["Feed Y"].append(feed_y)
                            master_data["Truncation along X"].append(truncX)
                            master_data["Truncation along Y"].append(truncY)
                            master_data["Peak Frequency"].append(peak_freq)
                            master_data["Frequency"].append(S11_freq[i])
                            master_data["S11 dB value"].append(freq_db[i])

                    else:
                        print("no patchW and patchL found in the csv file name")

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
                    if path_to_list == ['D:', 'UNI', 'FYP', 'Single Patch', 'Datasets', 'Patch Width & Length','Axial Ratio Parameter']:
                        for i in range(len(S11_freq)):
                            master_data["Axial Ratio at Fr (dB)"].append(axial_db_value)

                    elif path_to_list == ['D:', 'UNI', 'FYP', 'Single Patch', 'Datasets', 'Feed x and y','Axial Ratio Parameter']:
                        for i in range(len(S11_freq)):
                            master_data["Axial Ratio at Fr (dB)"].append(axial_db_value)

                    elif path_to_list == ['D:', 'UNI', 'FYP', 'Single Patch', 'Datasets', 'Truncation', 'Dataset - Truncation (0-25 mil)','Axial Ratio Parameter']:
                        for i in range(len(S11_freq)):
                            master_data["Axial Ratio at Fr (dB)"].append(axial_db_value)

                
        


    

print("Master data set created successfully")


df = pd.DataFrame(master_data)

# Save to Excel file
df.to_excel("Master Data file.xlsx", index=False)

print("Excel file created successfully!")

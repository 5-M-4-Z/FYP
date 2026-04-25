import os
import pandas as pd

print("File is running...")
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
                    "S44 dB value": [],
                    "AR value": [],
                    "LHCP value": [],
                    "RHCP value": [],
                    "Total gain value": [],
                    "MC S12": [],
                    "MC S13": [],
                    "MC S14": [],
                    "MC S23": [],
                    "MC S24": [],
                    "MC S34": []
                }

lst = [
    r"D:\Meesam\FYP\4-Patch\Data Sets\Datasets\Axial_Ratio_Datasets",
    r"D:\Meesam\FYP\4-Patch\Data Sets\Datasets\LHCP_vs_RHCP_Datasets",
    r"D:\Meesam\FYP\4-Patch\Data Sets\Datasets\MC Datasets",
    r"D:\Meesam\FYP\4-Patch\Data Sets\Datasets\S11 Datasets",
    r"D:\Meesam\FYP\4-Patch\Data Sets\Datasets\Total Gain Datasets"
]

folder1 = lst[0]

# Load all folders ONCE (fast lookup sets)
lhcp_files = set(os.listdir(lst[1]))
mc_files = set(os.listdir(lst[2]))
s11_files = set(os.listdir(lst[3]))
gain_files = set(os.listdir(lst[4]))

for file1 in os.listdir(folder1):
    path1 = os.path.join(folder1, file1)
    if not os.path.isfile(path1):
        continue

    new_name_lhcp = file1
    new_name_mc = file1.replace("Plot", "MC Plot")
    new_name_s11 = file1.replace("Plot", "S-11 Plot")
    new_name_gain = file1.replace("Plot", "Total Gain")

    # first read and extract data from folder 1 (Axial Ratio)
    # Create full path
    full_path = os.path.join(folder1, file1)

    if (os.path.isfile(full_path)) == False:
        print("no file exist")
    else:
        # print(filename)
        # Read the Excel file
        df = pd.read_csv(full_path)
        
        for col in df.columns:
            column_list = df[col].tolist()
            if col == "Theta [deg]":
                theta_column = column_list.copy()
            elif col == "dB(AxialRatioValue) []":
                AR_db_column = column_list.copy()
    
        ind = theta_column.index(0)
        master_data["AR value"].append(AR_db_column[ind])

    # then check if corresponding files exist in other folders and extract data if they do

    # Extacting RHCP and LHCP values from LHCP vs RHCP Datasets folder
    new_full_path = os.path.join(lst[1], new_name_lhcp)
    if (os.path.isfile(new_full_path)) == False:
        print("no file exist")
    else:
        # print(filename)
        # Read the Excel file
        df = pd.read_csv(new_full_path)

        for col in df.columns:
            column_list = df[col].tolist()
            if col == "Theta [deg]":
                theta_column = column_list.copy()
            elif col == "dB(GainLHCP) []":
                LHCP_db_column = column_list.copy()
            elif col == "dB(GainRHCP) []":
                RHCP_db_column = column_list.copy()
        
        ind = theta_column.index(0)
        master_data["LHCP value"].append(LHCP_db_column[ind])
        master_data["RHCP value"].append(RHCP_db_column[ind])


    # Extracting MC values from MC Datasets folder
    new_full_path = os.path.join(lst[2], new_name_mc)
    if (os.path.isfile(new_full_path)) == False:
        print("no file exist")
    else:
        # print(filename)
        # Read the Excel file
        df = pd.read_csv(new_full_path)

        for col in df.columns:
            column_list = df[col].tolist()
            if col == "Freq [GHz]":
                S_freq = column_list.copy()
            elif col == "dB(S(1,2)) []":
                S_freq_12 = column_list.copy()
            elif col == "dB(S(1,3)) []":
                S_freq_13 = column_list.copy()
            elif col == "dB(S(1,4)) []":
                S_freq_14 = column_list.copy()
            elif col == "dB(S(2,3)) []":
                S_freq_23 = column_list.copy()
            elif col == "dB(S(2,4)) []":
                S_freq_24 = column_list.copy()
            elif col == "dB(S(3,4)) []":
                S_freq_34 = column_list.copy()
        
        
        for ind in range(len(S_freq)):
            if abs(S_freq[ind] - 1.575333) < 0.000001:
                temp112 = S_freq_12[ind]
                temp113 = S_freq_13[ind]
                temp114 = S_freq_14[ind]
                temp123 = S_freq_23[ind]
                temp124 = S_freq_24[ind]
                temp134 = S_freq_34[ind]
            elif abs(S_freq[ind] - 1.575666) < 0.000001:
                temp212 = S_freq_12[ind]
                temp213 = S_freq_13[ind]
                temp214 = S_freq_14[ind]
                temp223 = S_freq_23[ind]
                temp224 = S_freq_24[ind]
                temp234 = S_freq_34[ind]


        master_data["MC S12"].append((temp112+temp212)/2)
        master_data["MC S13"].append((temp113+temp213)/2)
        master_data["MC S14"].append((temp114+temp214)/2)
        master_data["MC S23"].append((temp123+temp223)/2)
        master_data["MC S24"].append((temp124+temp224)/2)
        master_data["MC S34"].append((temp134+temp234)/2)


    # Extacting S Parameters from S11 Datasets folder
    new_full_path = os.path.join(lst[3], new_name_s11)
    if (os.path.isfile(new_full_path)) == False:
        print("no file exist")
    else:
        # print(filename)
        # Read the Excel file
        df = pd.read_csv(new_full_path)

        for col in df.columns:
            column_list = df[col].tolist()
            if col == "Freq [GHz]":
                S_freq = column_list.copy()
            elif col == "dB(S(1,1)) []":
                freq_db11 = column_list.copy()
            elif col == "dB(S(2,2)) []":
                freq_db22 = column_list.copy()
            elif col == "dB(S(3,3)) []":
                freq_db33 = column_list.copy()
            elif col == "dB(S(4,4)) []":
                freq_db44 = column_list.copy()
        
        
        for ind in range(len(S_freq)):
            if abs(S_freq[ind] - 1.575333) < 0.000001:
                temp11 = S_freq[ind]
                temp12 = freq_db11[ind]
                temp13 = freq_db22[ind]
                temp14 = freq_db33[ind]
                temp15 = freq_db44[ind]
            elif abs(S_freq[ind] - 1.575666) < 0.000001:
                temp21 = S_freq[ind]
                temp22 = freq_db11[ind]
                temp23 = freq_db22[ind]
                temp24 = freq_db33[ind]
                temp25 = freq_db44[ind]

        master_data["Frequency value"].append((temp11+temp21)/2)
        master_data["S11 dB value"].append((temp12+temp22)/2)
        master_data["S22 dB value"].append((temp13+temp23)/2)
        master_data["S33 dB value"].append((temp14+temp24)/2)
        master_data["S44 dB value"].append((temp15+temp25)/2)


    # Extracting Total Gain values from Total Gain Datasets folder
    new_full_path = os.path.join(lst[4], new_name_gain) 
    if (os.path.isfile(new_full_path)) == False:
        print("no file exist")
    else:
        # print(filename)
        # Read the Excel file
        df = pd.read_csv(new_full_path)

        for col in df.columns:
            column_list = df[col].tolist()
            if col == "Theta [deg]":
                theta_column = column_list.copy()
            elif col == "dB(GainTotal) []":
                gain_column = column_list.copy()
        
        for ind in range(len(theta_column)):
            if theta_column[ind] == 0:
                master_data["Total gain value"].append(gain_column[ind])


    """
    "Patch Width": [],
    "Patch Length": [],
    "Patch X": [],
    "Patch Y": [],
    "Feed X": [],
    "Feed Y": [],
    "Truncation along X": [],
    "Truncation along Y": [],

    """

    temp = file1.split("--")[1].split(".csv")[0].split(", ")
    master_data["Feed X"].append(float(temp[0].split("=")[1].strip()))
    master_data["Feed Y"].append(float(temp[1].split("=")[1].strip()))
    master_data["Truncation along X"].append(float(temp[2].split("=")[1].strip()))
    master_data["Truncation along Y"].append(float(temp[3].split("=")[1].strip()))
    master_data["Patch Width"].append(float(temp[4].split("=")[1].strip()))
    master_data["Patch Length"].append(float(temp[5].split("=")[1].strip()))
    master_data["Patch X"].append(float(temp[6].split("=")[1].strip()))
    master_data["Patch Y"].append(float(temp[7].split("=")[1].strip()))
    

print("Master data set created successfully")

for key in master_data:
    print(len(master_data[key]))

df = pd.DataFrame(master_data)

# Save to Excel file
df.to_excel("Master Data File - LHS Technique.xlsx", index=False)

print("Excel file created successfully!")


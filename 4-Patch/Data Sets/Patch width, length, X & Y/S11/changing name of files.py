import os

def rename_file(old_filename, new_filename):
    try:
        os.rename(old_filename, new_filename)
        print(f"File renamed from '{old_filename}' to '{new_filename}'")
    except FileNotFoundError:
        print(f"Error: '{old_filename}' does not exist.")
    except FileExistsError:
        print(f"Error: '{new_filename}' already exists.")
    except Exception as e:
        print(f"Unexpected error: {e}")

# Example usage:


loop_start = -27
loop_end = 27
loop_step = 3



for i in range (loop_start,loop_end,loop_step):
	patch_x_num = -25 + i*0.0254

	for j in range(loop_start,loop_end,loop_step):
		patch_y_num = 43 + j*0.0254

		for k in range(loop_start,loop_end,loop_step):
			patch_xsize_num = 50 + k*0.0254

			for l in range(loop_start,loop_end,loop_step):
				patch_ysize_num = 50 + l*0.0254
				


name = "Patch width (%f), Patch Length (%f), Patch x (%f), Patch y (%f)" % (patch_xsize_num, patch_ysize_num, patch_x_num, patch_y_num)

old_name = "S11_Data_Sets (patch width, length, x and y)/S-11 Plot -- " + name + ".csv"

name = "Patch x (%f), Patch y (%f), Patch width (%f), Patch Length (%f)" % (patch_x_num, patch_y_num, patch_xsize_num, patch_ysize_num)

new_name = "S11_Data_Sets (patch width, length, x and y)/S-11 Plot -- " + name + ".csv"

# "C:/Users/HU/OneDrive - Habib University/Desktop/Meesam/Axial_Ratio_Data_Sets (patch width, length, x and y)/Axial Ratio Plot -- " + name + ".csv"
				

rename_file(old_name, new_name)

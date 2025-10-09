##########################################
##########################################
##########################################
"""
Following looping can be done in HFSS which creates 3 cubes in each of the xy quadrant
"""

# import ScriptEnv
# ScriptEnv.Initialize("Ansoft.ElectronicsDesktop")
# oDesktop.RestoreWindow()
# oProject = oDesktop.NewProject()
# oProject.InsertDesign("HFSS", "HFSSDesign1", "HFSS Terminal Network", "")
# oDesign = oProject.SetActiveDesign("HFSSDesign1")


# for i in range(12):
# 	if i % 4 == 0:
# 		sign_x = 1
# 		sign_y = 1
# 	elif i % 4 == 1:
# 		sign_x = -1
# 		sign_y = 1
# 	elif i % 4 == 2:
# 		sign_x = -1
# 		sign_y = -1
# 	elif i % 4 == 3:
# 		sign_x = 1
# 		sign_y = -1

# 	sign_x = "%imm" % sign_x
# 	sign_y = "%imm" % sign_y

# 	oEditor = oDesign.SetActiveEditor("3D Modeler")
# 	oEditor.CreateBox(
# 		[
# 			"NAME:BoxParameters",
# 			"XPosition:="		, sign_x,
# 			"YPosition:="		, sign_y,
# 			"ZPosition:="		, "0mm",
# 			"XSize:="		, "1mm",
# 			"YSize:="		, "1mm",
# 			"ZSize:="		, "1mm"
# 		], 
# 		[
# 			"NAME:Attributes",
# 			"Name:="		, "Box1",
# 			"Flags:="		, "",
# 			"Color:="		, "(143 175 143)",
# 			"Transparency:="	, 0,
# 			"PartCoordinateSystem:=", "Global",
# 			"UDMId:="		, "",
# 			"MaterialValue:="	, "\"vacuum\"",
# 			"SurfaceMaterialValue:=", "\"\"",
# 			"SolveInside:="		, True,
# 			"ShellElement:="	, False,
# 			"ShellElementThickness:=", "0mm",
# 			"ReferenceTemperature:=", "20cel",
# 			"IsMaterialEditable:="	, True,
# 			"UseMaterialAppearance:=", False,
# 			"IsLightweight:="	, False
# 		])




##########################################
##########################################
##########################################
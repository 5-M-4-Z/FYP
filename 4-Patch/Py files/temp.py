import ScriptEnv
import math

for i in range (-20,-19):
	hole_x = "%fmm" % (0 + i*0.0254)
	for j in range(-20,-19):
		hole_y = "%fmm" % (82.0032 + j*0.0254)

		ScriptEnv.Initialize("Ansoft.ElectnicsDesktop")
		oDesktop.RestoreWindow()
		oProject = oDesktop.NewProject()
		oProject.InsertDesign("HFSS", "HFSSDesign1", "HFSS Modal Network", "")
		oDesign = oProject.SetActiveDesign("HFSSDesign1")
		oEditor = oDesign.SetActiveEditor("3D Modeler")

		# Constants
		c = 3e11             # Speed of light in mm/s
		f0 = 1.57542e9       # Resonant frequency in Hz (L1 GPS)
		er = 3.55            # Relative permittivity rogers
		h = 0.508            # Substrate height in mm
		height = 0.035       # Height of patch and ground plane in mm
		lambda_0 = c / f0    # Free-space wavelength in mm

		W = c / (2 * f0) * math.sqrt(2 / (er + 1))
		epsilon_eff = (er + 1)/2 + (er - 1)/2 * (1 + 12 * h / W)**(-0.5)
		delta_L = 0.412 * h * ((epsilon_eff + 0.3) * (W / h + 0.264)) / ((epsilon_eff - 0.258) * (W / h + 0.8))
		Leff = c / (2 * f0 * math.sqrt(epsilon_eff))
		L = Leff - 2 * delta_L
		# Calculate ground plane dimensions
		L = 50
		W = 50


		circle_x=0
		circle_y= 54.9968
		circle_z=0
		height_cylinder = 2

		# Calculate truncation dimensions based on your equation
		# a = ((round(L * math.sqrt(1 / (2 * (c * math.sqrt(er) / (4 * f0 * h)))),0)))
		a=3

		# Calculate truncaration triangle dimensions (right triangle)
		trunc_base = a  # Base of the triangle (from your equation)
		trunc_perpendicular = a  # Perpendicular side (same as base for square patch)
		trunc_hypotenuse = math.sqrt(trunc_base**2 + trunc_perpendicular**2)  # Pythagoras
		# Centering offsets
		x_patch_start = (-W / 2)  # Centered on ground plane
		y_patch_start = (-L / 2)  # Centered on ground plane
		# String versions
		L_str = "%.3fmm" % L
		W_str = "%.3fmm" % W
		h_str = "%.3fmm" % h
		height_str = "%.3fmm" % height
		height_cylinder_str = "%.3fmm" % height_cylinder

		xp_str = "%.3fmm" % (-W / 2)
		yp_str = "%.3fmm" % y_patch_start


		circle_x_str= circle_x_str = "%.3fmm" % circle_x
		circle_y_str= circle_y_str = "%.4fmm" % circle_y
		circle_z_str= circle_z_str = "%.3fmm" % circle_z

		# Convert to strings with units
		trunc_base_str = "%.3fmm" % trunc_base
		trunc_perp_str = "%.3fmm" % trunc_perpendicular

		# Truncation corners based on patch dimensions
		# Top-right truncation (positive X, positive Y on patch plane)
		trunc1_x1 = x_patch_start + W - a
		trunc1_y1 = y_patch_start + L
		trunc1_x2 = x_patch_start + W
		trunc1_y2 = y_patch_start + L - a

		# Bottom-left truncation (negative X, negative Y on patch plane)
		trunc2_x1 = x_patch_start
		trunc2_y1 = y_patch_start + a
		trunc2_x2 = x_patch_start + a
		trunc2_y2 = y_patch_start

		# String versions for HFSS
		trunc1_x1_str = "%.2fmm" % trunc1_x1
		trunc1_y1_str = "%.2fmm" % trunc1_y1
		trunc1_x2_str = "%.2fmm" % trunc1_x2
		trunc1_y2_str = "%.2fmm" % trunc1_y2

		trunc2_x1_str = "%.2fmm" % trunc2_x1
		trunc2_y1_str = "%.2fmm" % trunc2_y1
		trunc2_x2_str = "%.2fmm" % trunc2_x2
		trunc2_y2_str = "%.2fmm" % trunc2_y2

		# Hole Location
		# hole_x = "%fmm" % 0.55
		# hole_y = "%fmm" % 82.0032


		
		oDesign = oProject.SetActiveDesign("HFSSDesign1")
		oEditor = oDesign.SetActiveEditor("3D Modeler")
		# Create circular ground plane (copper)
		oEditor.CreateCylinder(
			[
				"NAME:CylinderParameters",
				"XCenter:=", "0mm",
				"YCenter:=", "0mm",
				"ZCenter:=", "0mm",
				"Radius:=", "138mm",  # Radius of ground plane
				"Height:=", height_str,
				"WhichAxis:=", "Z",
				"NumSides:=", "0"
			],
			[
				"NAME:Attributes",
				"Name:=", "Ground_Circle",
				"Flags:=", "",
				"Color:=", "(242 145 233)",
				"Transparency:=", 0.6,
				"PartCoordinateSystem:=", "Global",
				"MaterialValue:=", "\"copper\"",
				"SolveInside:=", False
			])
		oEditor.CreateCylinder(
			[
				"NAME:CylinderParameters",
				"XCenter:=", hole_x,
				"YCenter:=", hole_y,
				"ZCenter:=", "0mm",              
				"Radius:=", "1.6mm",
				"Height:=", height_str,           # Ground height only
				"WhichAxis:=", "Z",
				"NumSides:=", "0"
			],
			[
				"NAME:Attributes",
				"Name:=", "GroundHole1",
				"MaterialValue:=", "\"vacuum\"",
				"SolveInside:=", True,
				"Color:=", "(128 128 128)",
				"Transparency:=", 0.3
			])

		oEditor.Copy(
			[
				"NAME:Selections",
				"Selections:="		, "GroundHole1"
			])
		oEditor.Paste()
		oEditor.Paste()
		oEditor.Paste()
		oEditor.Rotate(
			[
				"NAME:Selections",
				"Selections:="		, "GroundHole2",
				"NewPartsModelFlag:="	, "Model"
			], 
			[
				"NAME:RotateParameters",
				"RotateAxis:="		, "Z",
				"RotateAngle:="		, "90deg"
			])
		oEditor.Rotate(
			[
				"NAME:Selections",
				"Selections:="		, "GroundHole3",
				"NewPartsModelFlag:="	, "Model"
			], 
			[
				"NAME:RotateParameters",
				"RotateAxis:="		, "Z",
				"RotateAngle:="		, "180deg"
			])
		oEditor.Rotate(
			[
				"NAME:Selections",
				"Selections:="		, "GroundHole4",
				"NewPartsModelFlag:="	, "Model"
			], 
			[
				"NAME:RotateParameters",
				"RotateAxis:="		, "Z",
				"RotateAngle:="		, "270deg"
			])
		oEditor.Subtract(
			[
				"NAME:Selections",
				"Blank Parts:="		, "Ground_Circle",
				"Tool Parts:="		, "GroundHole1,GroundHole2,GroundHole3,GroundHole4"
			], 
			[
				"NAME:SubtractParameters",
				"KeepOriginals:="	, False,
				"TurnOnNBodyBoolean:="	, True
			])

		# Substrate 
		oEditor.CreateCylinder(
			[
				"NAME:CylinderParameters",
				"XCenter:=", "0mm",
				"YCenter:=", "0mm",
				"ZCenter:=", height_str,
				"Radius:=", "138mm",  
				"Height:=", h_str,
				"WhichAxis:=", "Z",
				"NumSides:=", "0"
			],
			[
				"NAME:Attributes",
				"Name:=", "Substrate_Circle",
				"Flags:=", "",
				"Color:=", "(242 145 233)",
				"Transparency:=", 0.8,
				"PartCoordinateSystem:=", "Global",
				"MaterialValue:=", "\"Rogers RO4003 (tm)\"",
				"SolveInside:=", True
			])

		# cylinder for the substrate hole
		oEditor.CreateCylinder(
			[
				"NAME:CylinderParameters",
				"XCenter:=", hole_x,
				"YCenter:=", hole_y,
				"ZCenter:=", height_str,             
				"Radius:=", "0.8mm",
				"Height:=", h_str,  # Total height of patch above ground 
				"WhichAxis:=", "Z",
				"NumSides:=", "0"
			],
			[
				"NAME:Attributes",
				"Name:=", "SubstrateHole",
				"MaterialValue:=", "\"vacuum\"",
				"SolveInside:=", True,
				"Color:=", "(128 128 128)",
				"Transparency:=", 0.2
			])
		oEditor.Copy(
			[
				"NAME:Selections",
				"Selections:="		, "SubstrateHole"
			])
		oEditor.Paste()
		oEditor.Paste()
		oEditor.Paste()
		oEditor.Rotate(
			[
				"NAME:Selections",
				"Selections:="		, "SubstrateHole1",
				"NewPartsModelFlag:="	, "Model"
			], 
			[
				"NAME:RotateParameters",
				"RotateAxis:="		, "Z",
				"RotateAngle:="		, "90deg"
			])
		oEditor.Rotate(
			[
				"NAME:Selections",
				"Selections:="		, "SubstrateHole2",
				"NewPartsModelFlag:="	, "Model"
			], 
			[
				"NAME:RotateParameters",
				"RotateAxis:="		, "Z",
				"RotateAngle:="		, "180deg"
			])
		oEditor.Rotate(
			[
				"NAME:Selections",
				"Selections:="		, "SubstrateHole3",
				"NewPartsModelFlag:="	, "Model"
			], 
			[
				"NAME:RotateParameters",
				"RotateAxis:="		, "Z",
				"RotateAngle:="		, "270deg"
			])
		oEditor.Subtract(
			[
				"NAME:Selections",
				"Blank Parts:="		, "Substrate_Circle",
				"Tool Parts:="		, "SubstrateHole,SubstrateHole1,SubstrateHole2,SubstrateHole3"
			], 
			[
				"NAME:SubtractParameters",
				"KeepOriginals:="	, False,
				"TurnOnNBodyBoolean:="	, True
			])

		# Patch P1
		total_height = height + h  # Total height of patch above ground
		total_height_str = "%.3fmm" % total_height
		oEditor.CreateBox(
			[
				"NAME:BoxParameters",
				"XPosition:=", "-25mm",
				"YPosition:=", "43mm",
				"ZPosition:=", total_height_str,
				"XSize:=", "50mm",
				"YSize:=", "50mm",
				"ZSize:=", height_str
			],
			[
				"NAME:Attributes",
				"Name:=", "P1",
				"Flags:=", "",
				"Color:=", "(230 0 5)",
				"Transparency:=", 0.5,
				"PartCoordinateSystem:=", "Global",
				"MaterialValue:=","\"copper\"" ,
				"SolveInside:=", False
			])

		#  Patch P2
		oEditor.CreateBox(
			[
				"NAME:BoxParameters",
				"XPosition:=", "43mm",
				"YPosition:=", "-25mm",
				"ZPosition:=", total_height_str,
				"XSize:=", L_str,
				"YSize:=", W_str,
				"ZSize:=", height_str
			],
			[
				"NAME:Attributes",
				"Name:=", "P2",
				"Flags:=", "",
				"Color:=", "(230 0 5)",
				"Transparency:=", 0.5,
				"PartCoordinateSystem:=", "Global",
				"MaterialValue:=", "\"copper\"",
				"SolveInside:=", False
			])

		# Substrate for Patch P3
		oEditor.CreateBox(
			[
				"NAME:BoxParameters",
				"XPosition:=", "-25mm",
				"YPosition:=", "-93mm",
				"ZPosition:=", total_height_str,
				"XSize:=", "50mm",
				"YSize:=", "50mm",
				"ZSize:=", height_str
			],
			[
				"NAME:Attributes",
				"Name:=", "P3",
				"Flags:=", "",
				"Color:=", "(230 0 5)",
				"Transparency:=", 0.5,
				"PartCoordinateSystem:=", "Global",
				"MaterialValue:=","\"copper\"",
				"SolveInside:=", False
			])

		# Substrate for Patch P4
		oEditor.CreateBox(
			[
				"NAME:BoxParameters",
				"XPosition:=", "-93mm",
				"YPosition:=", "-25mm",
				"ZPosition:=", total_height_str,
				"XSize:=", "50mm",
				"YSize:=", "50mm",
				"ZSize:=", height_str
			],
			[
				"NAME:Attributes",
				"Name:=", "P4",
				"Flags:=", "",
				"Color:=", "(230 0 5)",
				"Transparency:=", 0.5,
				"PartCoordinateSystem:=", "Global",
				"MaterialValue:=", "\"copper\"",
				"SolveInside:=", False
			])

		a_trunc1 = 3  # Top-left truncation size
		a_trunc2 = 3  # Bottom-right truncation size (different for asymmetry)

		patch_thickness = 0.035  # Patch thickness in mm
		# Truncation 1: Top-Left Corner  
		x1 = -25           # left edge of patch
		y1 = 43+50       # top edge of patch
		z1 = height + h + height           # on top of substrate (same as patch)

		# Create triangular polyline for truncation
		oEditor.CreatePolyline(
			[
				"NAME:PolylineParameters",
				"IsPolylineCovered:=", True,  # Changed to True for better handling
				"IsPolylineClosed:=", True,
				[
					"NAME:PolylinePoints",
					["NAME:PLPoint", "X:=", "%.3fmm" % x1, "Y:=", "%.3fmm" % y1, "Z:=", "%.3fmm" % z1],
					["NAME:PLPoint", "X:=", "%.3fmm" % (x1 + a_trunc1), "Y:=", "%.3fmm" % y1, "Z:=", "%.3fmm" % z1],  
					["NAME:PLPoint", "X:=", "%.3fmm" % x1, "Y:=", "%.3fmm" % (y1 - a), "Z:=", "%.3fmm" % z1]   
				],
				[
					"NAME:PolylineSegments",
					["NAME:PLSegment", "SegmentType:=", "Line", "StartIndex:=", 0, "NoOfPoints:=", 2],
					["NAME:PLSegment", "SegmentType:=", "Line", "StartIndex:=", 1, "NoOfPoints:=", 2],
					["NAME:PLSegment", "SegmentType:=", "Line", "StartIndex:=", 2, "NoOfPoints:=", 2]
				],
				["NAME:PolylineXSection", "XSectionType:=", "None", "XSectionOrient:=", "Auto"]
			],
			[
				"NAME:Attributes",
				"Name:=", "Truncation1",
				"Flags:=", "",
				"Color:=", "(0 255 0)",
				"Transparency:=", 0,
				"PartCoordinateSystem:=", "Global",
				"MaterialValue:=", "\"vacuum\"",
				"SolveInside:=", True
			])

		# Cover and thicken (simplified approach)
		oEditor.ThickenSheet(
			[
				"NAME:Selections",
				"Selections:=", "Truncation1"
			],
			[
				"NAME:ThickenSheetParameters",
				"Thickness:=", "%.3fmm" % patch_thickness,  # Use actual patch thickness variable
				"BothSides:=", False
			])

		# Truncation 2: Bottom-Right Corner
		x2 = -25 + 50       # right edge of patch
		y2 = 43          # bottom edge of patch
		z2 = height + h + height           # same height as patch

		oEditor.CreatePolyline(
			[
				"NAME:PolylineParameters",
				"IsPolylineCovered:=", True,
				"IsPolylineClosed:=", True,  # Changed to True for proper closure
				[
					"NAME:PolylinePoints",
					["NAME:PLPoint", "X:=", "%.3fmm" % x2, "Y:=", "%.3fmm" % y2, "Z:=", "%.3fmm" % z2],
					["NAME:PLPoint", "X:=", "%.3fmm" % (x2 - a_trunc2), "Y:=", "%.3fmm" % y2, "Z:=", "%.3fmm" % z2],
					["NAME:PLPoint", "X:=", "%.3fmm" % x2, "Y:=", "%.3fmm" % (y2 + a ), "Z:=", "%.3fmm" % z2]
				],
				[
					"NAME:PolylineSegments",
					["NAME:PLSegment", "SegmentType:=", "Line", "StartIndex:=", 0, "NoOfPoints:=", 2],
					["NAME:PLSegment", "SegmentType:=", "Line", "StartIndex:=", 1, "NoOfPoints:=", 2],
					["NAME:PLSegment", "SegmentType:=", "Line", "StartIndex:=", 2, "NoOfPoints:=", 2]
				],
				["NAME:PolylineXSection", "XSectionType:=", "None", "XSectionOrient:=", "Auto"]
			],
			[
				"NAME:Attributes",
				"Name:=", "Truncation2",
				"Flags:=", "",
				"Color:=", "(255 165 0)",
				"Transparency:=", 0,
				"PartCoordinateSystem:=", "Global",
				"MaterialValue:=", "\"vacuum\"",
				"SolveInside:=", True
			])

		# Thicken directly 
		oEditor.ThickenSheet(
			[
				"NAME:Selections",
				"Selections:=", "Truncation2"
			],
			[
				"NAME:ThickenSheetParameters",
				"Thickness:=", "%.3fmm" % patch_thickness,  # Use actual patch thickness variable
				"BothSides:=", False
			])

		oEditor.Copy(
			[
				"NAME:Selections",
				"Selections:="		, "Truncation1"
			])
		oEditor.Paste()
		oEditor.Copy(
			[
				"NAME:Selections",
				"Selections:="		, "Truncation2"
			])
		oEditor.Paste()
		oEditor.Copy(
			[
				"NAME:Selections",
				"Selections:="		, "Truncation1"
			])
		oEditor.Paste()
		oEditor.Copy(
			[
				"NAME:Selections",
				"Selections:="		, "Truncation2"
			])
		oEditor.Paste()
		oEditor.Copy(
			[
				"NAME:Selections",
				"Selections:="		, "Truncation1"
			])
		oEditor.Paste()
		oEditor.Copy(
			[
				"NAME:Selections",
				"Selections:="		, "Truncation2"
			])
		oEditor.Paste()
		oEditor.Rotate(
			[
				"NAME:Selections",
				"Selections:="		, "Truncation3",
				"NewPartsModelFlag:="	, "Model"
			], 
			[
				"NAME:RotateParameters",
				"RotateAxis:="		, "Z",
				"RotateAngle:="		, "90deg"
			])
		oEditor.Rotate(
			[
				"NAME:Selections",
				"Selections:="		, "Truncation4",
				"NewPartsModelFlag:="	, "Model"
			], 
			[
				"NAME:RotateParameters",
				"RotateAxis:="		, "Z",
				"RotateAngle:="		, "90deg"
			])
		oEditor.Rotate(
			[
				"NAME:Selections",
				"Selections:="		, "Truncation5",
				"NewPartsModelFlag:="	, "Model"
			], 
			[
				"NAME:RotateParameters",
				"RotateAxis:="		, "Z",
				"RotateAngle:="		, "180deg"
			])
		oEditor.Rotate(
			[
				"NAME:Selections",
				"Selections:="		, "Truncation6",
				"NewPartsModelFlag:="	, "Model"
			], 
			[
				"NAME:RotateParameters",
				"RotateAxis:="		, "Z",
				"RotateAngle:="		, "180deg"
			])
		oEditor.Rotate(
			[
				"NAME:Selections",
				"Selections:="		, "Truncation7",
				"NewPartsModelFlag:="	, "Model"
			], 
			[
				"NAME:RotateParameters",
				"RotateAxis:="		, "Z",
				"RotateAngle:="		, "270deg"
			])
		oEditor.Rotate(
			[
				"NAME:Selections",
				"Selections:="		, "Truncation8",
				"NewPartsModelFlag:="	, "Model"
			], 
			[
				"NAME:RotateParameters",
				"RotateAxis:="		, "Z",
				"RotateAngle:="		, "270deg"
			])
		oEditor.Subtract(
			[
				"NAME:Selections",
				"Blank Parts:="		, "P1",
				"Tool Parts:="		, "Truncation1,Truncation2"
			], 
			[
				"NAME:SubtractParameters",
				"KeepOriginals:="	, False,
				"TurnOnNBodyBoolean:="	, True
			])
		oEditor.Subtract(
			[
				"NAME:Selections",
				"Blank Parts:="		, "P2",
				"Tool Parts:="		, "Truncation7,Truncation8"
			], 
			[
				"NAME:SubtractParameters",
				"KeepOriginals:="	, False,
				"TurnOnNBodyBoolean:="	, True
			])
		oEditor.Subtract(
			[
				"NAME:Selections",
				"Blank Parts:="		, "P3",
				"Tool Parts:="		, "Truncation5,Truncation6"
			], 
			[
				"NAME:SubtractParameters",
				"KeepOriginals:="	, False,
				"TurnOnNBodyBoolean:="	, True
			])
		oEditor.Subtract(
			[
				"NAME:Selections",
				"Blank Parts:="		, "P4",
				"Tool Parts:="		, "Truncation3,Truncation4"
			], 
			[
				"NAME:SubtractParameters",
				"KeepOriginals:="	, False,
				"TurnOnNBodyBoolean:="	, True
			])

		oEditor = oDesign.SetActiveEditor("3D Modeler")
		oEditor.CreateCylinder(
			[
				"NAME:CylinderParameters",
				"XCenter:="		, hole_x,
				"YCenter:="		, hole_y,
				"ZCenter:="		, "0mm",
				"Radius:="		, "1.6mm",
				"Height:="		, "-"+height_cylinder_str,
				"WhichAxis:="		, "Z",
				"NumSides:="		, "0"
			], 
			[
				"NAME:Attributes",
				"Name:="		, "CoaxCover1",
				"Flags:="		, "",
				"Color:="		, "(143 175 143)",
				"Transparency:="	, 0,
				"PartCoordinateSystem:=", "Global",
				"UDMId:="		, "",
				"MaterialValue:="	, "\"glass_PTFEreinf\"",
				"SurfaceMaterialValue:=", "\"\"",
				"SolveInside:="		, True,
				"ShellElement:="	, False,
				"ShellElementThickness:=", "0mm",
				"ReferenceTemperature:=", "20cel",
				"IsMaterialEditable:="	, True,
				"IsSurfaceMaterialEditable:=", True,
				"UseMaterialAppearance:=", False,
				"IsLightweight:="	, False
			])
		oEditor = oDesign.SetActiveEditor("3D Modeler")
		oEditor.Copy(
			[
				"NAME:Selections",
				"Selections:="		, "CoaxCover1"
			])
		oEditor.Paste()
		oEditor.Paste()
		oEditor.Paste()
		oEditor.Rotate(
			[
				"NAME:Selections",
				"Selections:="		, "CoaxCover2",
				"NewPartsModelFlag:="	, "Model"
			], 
			[
				"NAME:RotateParameters",
				"RotateAxis:="		, "Z",
				"RotateAngle:="		, "90deg"
			])
		oEditor.Rotate(
			[
				"NAME:Selections",
				"Selections:="		, "CoaxCover3",
				"NewPartsModelFlag:="	, "Model"
			], 
			[
				"NAME:RotateParameters",
				"RotateAxis:="		, "Z",
				"RotateAngle:="		, "180deg"
			])
		oEditor.Rotate(
			[
				"NAME:Selections",
				"Selections:="		, "CoaxCover4",
				"NewPartsModelFlag:="	, "Model"
			], 
			[
				"NAME:RotateParameters",
				"RotateAxis:="		, "Z",
				"RotateAngle:="		, "270deg"
			])

		oEditor = oDesign.SetActiveEditor("3D Modeler")
		oEditor.CreateCylinder(
			[
				"NAME:CylinderParameters",
				"XCenter:="		, hole_x,
				"YCenter:="		, hole_y,
				"ZCenter:="		, "0mm",
				"Radius:="		, "0.8mm",
				"Height:="		, "-"+height_cylinder_str,
				"WhichAxis:="		, "Z",
				"NumSides:="		, "0"
			], 
			[
				"NAME:Attributes",
				"Name:="		, "Coax_Pin1",
				"Flags:="		, "",
				"Color:="		, "(143 175 143)",
				"Transparency:="	, 0,
				"PartCoordinateSystem:=", "Global",
				"UDMId:="		, "",
				"MaterialValue:="	, "\"copper\"",
				"SurfaceMaterialValue:=", "\"\"",
				"SolveInside:="		, False,
				"ShellElement:="	, False,
				"ShellElementThickness:=", "0mm",
				"ReferenceTemperature:=", "20cel",
				"IsMaterialEditable:="	, True,
				"IsSurfaceMaterialEditable:=", True,
				"UseMaterialAppearance:=", False,
				"IsLightweight:="	, False
			])
		oEditor = oDesign.SetActiveEditor("3D Modeler")
		oEditor.Copy(
			[
				"NAME:Selections",
				"Selections:="		, "Coax_Pin1"
			])
		oEditor.Paste()
		oEditor.Paste()
		oEditor.Paste()
		oEditor.Rotate(
			[
				"NAME:Selections",
				"Selections:="		, "Coax_Pin2",
				"NewPartsModelFlag:="	, "Model"
			], 
			[
				"NAME:RotateParameters",
				"RotateAxis:="		, "Z",
				"RotateAngle:="		, "90deg"
			])
		oEditor.Rotate(
			[
				"NAME:Selections",
				"Selections:="		, "Coax_Pin3",
				"NewPartsModelFlag:="	, "Model"
			], 
			[
				"NAME:RotateParameters",
				"RotateAxis:="		, "Z",
				"RotateAngle:="		, "180deg"
			])
		oEditor.Rotate(
			[
				"NAME:Selections",
				"Selections:="		, "Coax_Pin4",
				"NewPartsModelFlag:="	, "Model"
			], 
			[
				"NAME:RotateParameters",
				"RotateAxis:="		, "Z",
				"RotateAngle:="		, "270deg"
			])
		############################
		oEditor.CreateCylinder(
			[
				"NAME:CylinderParameters",
				"XCenter:="		, hole_x,
				"YCenter:="		, hole_y,
				"ZCenter:="		, "0mm",
				"Radius:="		, "0.8mm",
				"Height:="		, total_height_str,
				"WhichAxis:="		, "Z",
				"NumSides:="		, "0"
			], 
			[
				"NAME:Attributes",
				"Name:="		, "Probe1",
				"Flags:="		, "",
				"Color:="		, "(143 175 143)",
				"Transparency:="	, 0,
				"PartCoordinateSystem:=", "Global",
				"UDMId:="		, "",
				"MaterialValue:="	, "\"copper\"",
				"SurfaceMaterialValue:=", "\"\"",
				"SolveInside:="		, False,
				"ShellElement:="	, False,
				"ShellElementThickness:=", "0mm",
				"ReferenceTemperature:=", "20cel",
				"IsMaterialEditable:="	, True,
				"IsSurfaceMaterialEditable:=", True,
				"UseMaterialAppearance:=", False,
				"IsLightweight:="	, False
			])
		oEditor = oDesign.SetActiveEditor("3D Modeler")
		oEditor.Copy(
			[
				"NAME:Selections",
				"Selections:="		, "Probe1"
			])
		oEditor.Paste()
		oEditor.Paste()
		oEditor.Paste()
		oEditor.Rotate(
			[
				"NAME:Selections",
				"Selections:="		, "Probe2",
				"NewPartsModelFlag:="	, "Model"
			], 
			[
				"NAME:RotateParameters",
				"RotateAxis:="		, "Z",
				"RotateAngle:="		, "90deg"
			])
		oEditor.Rotate(
			[
				"NAME:Selections",
				"Selections:="		, "Probe3",
				"NewPartsModelFlag:="	, "Model"
			], 
			[
				"NAME:RotateParameters",
				"RotateAxis:="		, "Z",
				"RotateAngle:="		, "180deg"
			])
		oEditor.Rotate(
			[
				"NAME:Selections",
				"Selections:="		, "Probe4",
				"NewPartsModelFlag:="	, "Model"
			], 
			[
				"NAME:RotateParameters",
				"RotateAxis:="		, "Z",
				"RotateAngle:="		, "270deg"
			])
		# Airbox margin
		air_margin = lambda_0 / 4  # Margin on all sides

		# Airbox dimensions
		W_air = ((W * 2) + 2 * air_margin)+168
		L_air = ((L * 2) + 2 * air_margin)+168
		H_air = h + height + height + air_margin

		# Airbox position (centered around ground/patch array)
		x_air_start = -W_air / 2
		y_air_start = -L_air / 2
		z_air_start = -air_margin  # start slightly below the ground

		# Convert to strings
		W_air_str = "%.3fmm" % W_air
		L_air_str = "%.3fmm" % L_air
		H_air_str = "%.3fmm" % H_air
		x_air_str = "%.3fmm" % x_air_start
		y_air_str = "%.3fmm" % y_air_start
		z_air_str = "%.3fmm" % z_air_start

		# Create Airbox
		oEditor.CreateBox(
			[
				"NAME:BoxParameters",
				"XPosition:=", x_air_str,
				"YPosition:=", y_air_str,
				"ZPosition:=", "0mm",
				"XSize:=", W_air_str,
				"YSize:=", L_air_str,
				"ZSize:=", H_air_str
			],
			[
				"NAME:Attributes",
				"Name:=", "AirBox",
				"Flags:=", "",
				"Color:=", "(62 241 251)",
				"Transparency:=", 0.93,
				"PartCoordinateSystem:=", "Global",
				"MaterialValue:=", "\"air\"",
				"SolveInside:=", True
			])

		# Dynamic boundary assignment with error handling
		try:
			oEditor = oDesign.SetActiveEditor("3D Modeler")
			
			# Get all faces of the AirBox
			airbox_faces = oEditor.GetFaceIDs("AirBox")
			
			if not airbox_faces:
				raise Exception("Could not find faces for AirBox")
			
			# Identify and exclude the bottom face
			faces_to_assign = []
			bottom_face = None
			
			for face_id in airbox_faces:
				face_center = oEditor.GetFaceCenter(face_id)
				z_pos = float(face_center[2].replace("mm", ""))
				
				# The bottom face is at z=0 (or very close)
				if abs(z_pos) < 1e-6:
					bottom_face = face_id
				else:
					faces_to_assign.append(int(face_id))  # Ensure face IDs are integers
			
			if not faces_to_assign:
				raise Exception("No suitable faces found for radiation boundary")
			
			# Assign radiation boundaries
			oModule = oDesign.GetModule("BoundarySetup")
			oModule.AssignRadiation(
				[
					"NAME:Rad1",
					"Faces:=", faces_to_assign,
					"IsIncidentField:=", False,
					"IsEnforcedField:=", False,
					"UseAdaptiveIE:=", False
				]
			)

		except Exception as e:
			print("Error assigning radiation boundary:", e)

		oEditor = oDesign.SetActiveEditor("3D Modeler")
		oEditor.CreateCircle(
			[
				"NAME:CircleParameters",
				"IsCovered:="		, True,
				"XCenter:="		, hole_x,
				"YCenter:="		, hole_y,
				"ZCenter:="		, "-" + height_cylinder_str,
				"Radius:="		, "1.6mm",
				"WhichAxis:="		, "Z",
				"NumSegments:="		, "0"
			], 
			[
				"NAME:Attributes",
				"Name:="		, "Port1",
				"Flags:="		, "",
				"Color:="		, "(143 175 143)",
				"Transparency:="	, 0,
				"PartCoordinateSystem:=", "Global",
				"UDMId:="		, "",
				"MaterialValue:="	, "\"vacuum\"",
				"SurfaceMaterialValue:=", "\"\"",
				"SolveInside:="		, True,
				"ShellElement:="	, False,
				"ShellElementThickness:=", "0mm",
				"ReferenceTemperature:=", "20cel",
				"IsMaterialEditable:="	, True,
				"IsSurfaceMaterialEditable:=", True,
				"UseMaterialAppearance:=", False,
				"IsLightweight:="	, False
			])
		oEditor.Copy(
			[
				"NAME:Selections",
				"Selections:="		, "Port1"
			])
		oEditor.Paste()
		oEditor.Paste()
		oEditor.Paste()
		oEditor.Rotate(
			[
				"NAME:Selections",
				"Selections:="		, "Port2",
				"NewPartsModelFlag:="	, "Model"
			], 
			[
				"NAME:RotateParameters",
				"RotateAxis:="		, "Z",
				"RotateAngle:="		, "90deg"
			])
		oEditor.Rotate(
			[
				"NAME:Selections",
				"Selections:="		, "Port3",
				"NewPartsModelFlag:="	, "Model"
			], 
			[
				"NAME:RotateParameters",
				"RotateAxis:="		, "Z",
				"RotateAngle:="		, "180deg"
			])
		oEditor.Rotate(
			[
				"NAME:Selections",
				"Selections:="		, "Port4",
				"NewPartsModelFlag:="	, "Model"
			], 
			[
				"NAME:RotateParameters",
				"RotateAxis:="		, "Z",
				"RotateAngle:="		, "270deg"
			])
		oModule = oDesign.GetModule("BoundarySetup")
		oModule.AssignWavePort(
			[
				"NAME:1",
				"Objects:="		, ["Port1"],
				"WavePortType:="	, "Default",
				"NumModes:="		, 1,
				"UseLineModeAlignment:=", False,
				"DoDeembed:="		, False,
				[
					"NAME:Modes",
					[
						"NAME:Mode1",
						"ModeNum:="		, 1,
						"UseIntLine:="		, False,
						"CharImp:="		, "Zpi"
					]
				],
				"UseAnalyticAlignment:=", False,
				"ShowReporterFilter:="	, False,
				"ReporterFilter:="	, [True]
			])
		oModule.AssignWavePort(
			[
				"NAME:2",
				"Objects:="		, ["Port2"],
				"WavePortType:="	, "Default",
				"NumModes:="		, 1,
				"UseLineModeAlignment:=", False,
				"DoDeembed:="		, False,
				[
					"NAME:Modes",
					[
						"NAME:Mode1",
						"ModeNum:="		, 1,
						"UseIntLine:="		, False,
						"CharImp:="		, "Zpi"
					]
				],
				"UseAnalyticAlignment:=", False,
				"ShowReporterFilter:="	, False,
				"ReporterFilter:="	, [True]
			])
		oModule.AssignWavePort(
			[
				"NAME:3",
				"Objects:="		, ["Port3"],
				"WavePortType:="	, "Default",
				"NumModes:="		, 1,
				"UseLineModeAlignment:=", False,
				"DoDeembed:="		, False,
				[
					"NAME:Modes",
					[
						"NAME:Mode1",
						"ModeNum:="		, 1,
						"UseIntLine:="		, False,
						"CharImp:="		, "Zpi"
					]
				],
				"UseAnalyticAlignment:=", False,
				"ShowReporterFilter:="	, False,
				"ReporterFilter:="	, [True]
			])
		oModule.AssignWavePort(
			[
				"NAME:4",
				"Objects:="		, ["Port4"],
				"WavePortType:="	, "Default",
				"NumModes:="		, 1,
				"UseLineModeAlignment:=", False,
				"DoDeembed:="		, False,
				[
					"NAME:Modes",
					[
						"NAME:Mode1",
						"ModeNum:="		, 1,
						"UseIntLine:="		, False,
						"CharImp:="		, "Zpi"
					]
				],
				"UseAnalyticAlignment:=", False,
				"ShowReporterFilter:="	, False,
				"ReporterFilter:="	, [True]
			])

		oModule = oDesign.GetModule("Solutions")
		oModule.EditSources(
			[
				[
					"IncludePortPostProcessing:=", False,
					"SpecifySystemPower:="	, False
				],
				[
					"Name:="		, "1:1",
					"Magnitude:="		, "1W",
					"Phase:="		, "0deg"
				],
				[
					"Name:="		, "2:1",
					"Magnitude:="		, "1W",
					"Phase:="		, "-90deg"
				],
				[
					"Name:="		, "3:1",
					"Magnitude:="		, "1W",
					"Phase:="		, "-180deg"
				],
				[
					"Name:="		, "4:1",
					"Magnitude:="		, "1W",
					"Phase:="		, "-270deg"
				]
			])


		oModule = oDesign.GetModule("AnalysisSetup")
		oModule.InsertSetup("HfssDriven", 
			[
				"NAME:Setup1",
				"SolveType:="		, "Single",
				"Frequency:="		, "1.57542GHz",
				"MaxDeltaS:="		, 0.02,
				"UseMatrixConv:="	, False,
				"MaximumPasses:="	, 20,
				"MinimumPasses:="	, 1,
				"MinimumConvergedPasses:=", 1,
				"PercentRefinement:="	, 30,
				"IsEnabled:="		, True,
				[
					"NAME:MeshLink",
					"ImportMesh:="		, False
				],
				"BasisOrder:="		, 1,
				"DoLambdaRefine:="	, True,
				"DoMaterialLambda:="	, True,
				"SetLambdaTarget:="	, False,
				"Target:="		, 0.3333,
				"UseMaxTetIncrease:="	, False,
				"PortAccuracy:="	, 2,
				"UseABCOnPort:="	, False,
				"SetPortMinMaxTri:="	, False,
				"DrivenSolverType:="	, "Direct Solver",
				"EnhancedLowFreqAccuracy:=", False,
				"SaveRadFieldsOnly:="	, False,
				"SaveAnyFields:="	, True,
				"IESolverType:="	, "Auto",
				"LambdaTargetForIESolver:=", 0.15,
				"UseDefaultLambdaTgtForIESolver:=", True,
				"IE Solver Accuracy:="	, "Balanced",
				"InfiniteSphereSetup:="	, "",
				"MaxPass:="		, 10,
				"MinPass:="		, 1,
				"MinConvPass:="		, 1,
				"PerError:="		, 1,
				"PerRefine:="		, 30
			])

		oModule = oDesign.GetModule("AnalysisSetup")
		oModule.InsertFrequencySweep("Setup1", 
			[
				"NAME:Sweep",
				"IsEnabled:="		, True,
				"RangeType:="		, "LinearCount",
				"RangeStart:="		, "1.55GHz",
				"RangeEnd:="		, "1.6GHz",
				"RangeCount:="		, 10001,
				"Type:="		, "Fast",
				"SaveFields:="		, True,
				"SaveRadFields:="	, False,
				"GenerateFieldsForAllFreqs:=", False
			])

		# oProject.SaveAs("C:\\Users\\hp\\Desktop\\STRP\\Project1.aedt", True)


		oModule = oDesign.GetModule("RadField")
		oModule.InsertInfiniteSphereSetup(
			[
				"NAME:Infinite Sphere1",
				"UseCustomRadiationSurface:=", False,
				"CSDefinition:="	, "Theta-Phi",
				"Polarization:="	, "Linear",
				"ThetaStart:="		, "-180deg",
				"ThetaStop:="		, "180deg",
				"ThetaStep:="		, "10deg",
				"PhiStart:="		, "0deg",
				"PhiStop:="		, "360deg",
				"PhiStep:="		, "10deg",
				"UseLocalCS:="		, False
			])
		oDesign.AnalyzeAll()
		oProject.SaveAs("D:\\UNI\\FYP\\Temp\\temp.aedt", True)
		oModule = oDesign.GetModule("ReportSetup")
		oModule.CreateReport("S Parameter Plot 1", "Modal Solution Data", "Rectangular Plot", "Setup1 : Sweep", 
			[
				"Domain:="		, "Sweep"
			], 
			[
				"Freq:="		, ["All"]
			], 
			[
				"X Component:="		, "Freq",
				"Y Component:="		, ["dB(S(1,1))"]
			])

		oModule = oDesign.GetModule("ReportSetup")
		oModule.CreateReport("Axial Ratio Plot 1", "Far Fields", "Rectangular Plot", "Setup1 : LastAdaptive", 
			[
				"Context:="		, "Infinite Sphere1"
			], 
			[
				"Theta:="		, ["All"],
				"Phi:="			, ["0deg"],
				"Freq:="		, ["1.57542GHz"]
			], 
			[
				"X Component:="		, "Theta",
				"Y Component:="		, ["dB(AxialRatioValue)"]
			])

		oEditor = oDesign.SetActiveEditor("3D Modeler")

		oModule = oDesign.GetModule("ReportSetup")
		oModule.ExportToFile("S Parameter Plot 1", "D:/UNI/FYP/S11_Data_Sets/S-11 Plot--Hole_x:" + hole_x + " -- Hole_y:" + hole_y + ".csv", False)
		oModule.ExportToFile("Axial Ratio Plot 1", "D:/UNI/FYP/Axial_Ratio_Data_Sets/Axial Ratio Plot--Hole_x:" + hole_x + " -- Hole_y:" + hole_y + ".csv", False)
		oDesktop.DeleteProject("temp")



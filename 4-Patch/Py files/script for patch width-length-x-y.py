import ScriptEnv
import math
ScriptEnv.Initialize("Ansoft.ElectnicsDesktop")
oDesktop.RestoreWindow()

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


				# Patch Co-ordinate & dimensions
				# patch_x_num = -25
				# patch_y_num = 43

				# patch_xsize_num = 50
				# patch_ysize_num = 50

				height_cylinder = 2

				# Truncation horizontal/vertical length
				a=3

				# String versions
				L_str = "%fmm" % patch_xsize_num
				W_str = "%fmm" % patch_ysize_num
				h_str = "%fmm" % h
				height_str = "%fmm" % height
				height_cylinder_str = "%fmm" % height_cylinder


				# Hole Location
				hole_x = "%fmm" % 0.55
				hole_y = "%fmm" % 82.0032
				


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
				total_height_str = "%fmm" % total_height
				oEditor.CreateBox(
					[
						"NAME:BoxParameters",
						"XPosition:=", "%fmm" % patch_x_num,
						"YPosition:=", "%fmm" % patch_y_num,
						"ZPosition:=", total_height_str,
						"XSize:=", "%fmm" % patch_xsize_num,
						"YSize:=", "%fmm" % patch_ysize_num,
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

				a_trunc1 = 3  # Top-left truncation size
				a_trunc2 = 3  # Bottom-right truncation size (different for asymmetry)

				patch_thickness = height  # Patch thickness in mm
				# Truncation 1: Top-Left Corner  
				x1 = patch_x_num           # left edge of patch
				y1 = patch_y_num + patch_ysize_num       # top edge of patch
				z1 = height + h + height           # on top of substrate (same as patch)

				# Create triangular polyline for truncation
				oEditor.CreatePolyline(
					[
						"NAME:PolylineParameters",
						"IsPolylineCovered:=", True,  # Changed to True for better handling
						"IsPolylineClosed:=", True,
						[
							"NAME:PolylinePoints",
							["NAME:PLPoint", "X:=", "%fmm" % x1, "Y:=", "%fmm" % y1, "Z:=", "%fmm" % z1],
							["NAME:PLPoint", "X:=", "%fmm" % (x1 + a_trunc1), "Y:=", "%fmm" % y1, "Z:=", "%fmm" % z1],  
							["NAME:PLPoint", "X:=", "%fmm" % x1, "Y:=", "%fmm" % (y1 - a), "Z:=", "%fmm" % z1]   
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
						"Thickness:=", "%fmm" % patch_thickness,  # Use actual patch thickness variable
						"BothSides:=", False
					])

				# Truncation 2: Bottom-Right Corner
				x2 = patch_x_num + patch_xsize_num       # right edge of patch
				y2 = patch_y_num          # bottom edge of patch
				z2 = height + h + height           # same height as patch

				oEditor.CreatePolyline(
					[
						"NAME:PolylineParameters",
						"IsPolylineCovered:=", True,
						"IsPolylineClosed:=", True,  # Changed to True for proper closure
						[
							"NAME:PolylinePoints",
							["NAME:PLPoint", "X:=", "%fmm" % x2, "Y:=", "%fmm" % y2, "Z:=", "%fmm" % z2],
							["NAME:PLPoint", "X:=", "%fmm" % (x2 - a_trunc2), "Y:=", "%fmm" % y2, "Z:=", "%fmm" % z2],
							["NAME:PLPoint", "X:=", "%fmm" % x2, "Y:=", "%fmm" % (y2 + a ), "Z:=", "%fmm" % z2]
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
						"Thickness:=", "%fmm" % patch_thickness,  # Use actual patch thickness variable
						"BothSides:=", False
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

				# Now copying and pasting the truncated patch and rotating it (equally spaced)
				oEditor.Copy(
					[
						"NAME:Selections",
						"Selections:="		, "P1"
					])
				oEditor.Paste()
				oEditor.Paste()
				oEditor.Paste()
				oEditor.Rotate(
					[
						"NAME:Selections",
						"Selections:="		, "P4",
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
						"Selections:="		, "P3",
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
						"Selections:="		, "P2",
						"NewPartsModelFlag:="	, "Model"
					], 
					[
						"NAME:RotateParameters",
						"RotateAxis:="		, "Z",
						"RotateAngle:="		, "90deg"
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
				W_air = ((patch_xsize_num * 2) + 2 * air_margin)+168
				L_air = ((patch_ysize_num * 2) + 2 * air_margin)+168
				H_air = h + height + height + air_margin

				# Airbox position (centered around ground/patch array)
				x_air_start = -W_air / 2
				y_air_start = -L_air / 2
				z_air_start = -air_margin  # start slightly below the ground

				# Convert to strings
				W_air_str = "%fmm" % W_air
				L_air_str = "%fmm" % L_air
				H_air_str = "%fmm" % H_air
				x_air_str = "%fmm" % x_air_start
				y_air_str = "%fmm" % y_air_start
				z_air_str = "%fmm" % z_air_start

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
				oProject.SaveAs("D:\\UNI\\FYP\\4-Patch\\Temp\\temp.aedt", True)
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
				name = "Patch width (%f), Patch Length (%f), Patch x (%f), Patch y (%f)" % (patch_xsize_num, patch_ysize_num, patch_x_num, patch_y_num)

				oModule.ExportToFile("S Parameter Plot 1", "D:/UNI/FYP/4-Patch/S11_Data_Sets (patch width, length, x and y)/S-11 Plot -- " + name + ".csv", False)
				oModule.ExportToFile("Axial Ratio Plot 1", "D:/UNI/FYP/4-Patch/Axial_Ratio_Data_Sets (patch width, length, x and y)/Axial Ratio Plot -- " + name + ".csv", False)
				oDesktop.DeleteProject("temp")



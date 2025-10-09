$begin 'Profile'
	$begin 'ProfileGroup'
		MajorVer=2024
		MinorVer=1
		Name='Solution Process'
		$begin 'StartInfo'
			I(1, 'Start Time', '10/08/2025 20:05:43')
			I(1, 'Host', 'DESKTOP-1MLKABB')
			I(1, 'Processor', '4')
			I(1, 'OS', 'NT 10.0')
			I(1, 'Product', 'HFSS Version 2024.1.0')
		$end 'StartInfo'
		$begin 'TotalInfo'
			I(1, 'Elapsed Time', '00:18:10')
			I(1, 'ComEngine Memory', '76.4 M')
		$end 'TotalInfo'
		GroupOptions=8
		TaskDataOptions('CPU Time'=8, Memory=8, 'Real Time'=8)
		ProfileItem('', 0, 0, 0, 0, 0, 'I(1, 1, \'Executing From\', \'D:\\\\Software\\\\Ansys\\\\AnsysEM\\\\v241\\\\Win64\\\\HFSSCOMENGINE.exe\')', false, true)
		$begin 'ProfileGroup'
			MajorVer=2024
			MinorVer=1
			Name='HPC'
			$begin 'StartInfo'
				I(1, 'Type', 'Disabled')
			$end 'StartInfo'
			$begin 'TotalInfo'
				I(0, ' ')
			$end 'TotalInfo'
			GroupOptions=0
			TaskDataOptions(Memory=8)
			ProfileItem('Machine', 0, 0, 0, 0, 0, 'I(5, 1, \'Name\', \'DESKTOP-1MLKABB\', 1, \'Memory\', \'7.88 GB\', 3, \'RAM Limit\', 90, \'%f%%\', 2, \'Cores\', 1, false, 1, \'Free Disk Space\', \'44.3 GB\')', false, true)
		$end 'ProfileGroup'
		ProfileItem('', 0, 0, 0, 0, 0, 'I(1, 1, \'Allow off core\', \'True\')', false, true)
		ProfileItem('', 0, 0, 0, 0, 0, 'I(1, 1, \'Solution Basis Order\', \'1\')', false, true)
		ProfileItem('Design Validation', 0, 0, 0, 0, 0, 'I(1, 0, \'Elapsed time : 00:00:00 , HFSS ComEngine Memory : 72.8 M\')', false, true)
		ProfileItem('', 0, 0, 0, 0, 0, 'I(1, 0, \'Perform full validations with standard port validations\')', false, true)
		ProfileItem('', 0, 0, 0, 0, 0, 'I(1, 0, \'\')', false, true)
		$begin 'ProfileGroup'
			MajorVer=2024
			MinorVer=1
			Name='Initial Meshing'
			$begin 'StartInfo'
				I(1, 'Time', '10/08/2025 20:05:43')
			$end 'StartInfo'
			$begin 'TotalInfo'
				I(1, 'Elapsed Time', '00:00:45')
			$end 'TotalInfo'
			GroupOptions=4
			TaskDataOptions('CPU Time'=8, Memory=8, 'Real Time'=8)
			ProfileItem('Mesh', 17, 0, 13, 0, 158000, 'I(3, 1, \'Type\', \'TAU\', 2, \'Cores\', 1, false, 2, \'Tetrahedra\', 94290, false)', true, true)
			ProfileItem('Coarsen', 13, 0, 13, 0, 158000, 'I(1, 2, \'Tetrahedra\', 31196, false)', true, true)
			ProfileItem('Lambda Refine', 1, 0, 1, 0, 50964, 'I(2, 2, \'Tetrahedra\', 31347, false, 2, \'Cores\', 1, false)', true, true)
			ProfileItem('Simulation Setup', 0, 0, 0, 0, 243512, 'I(1, 1, \'Disk\', \'0 Bytes\')', true, true)
			ProfileItem('Port Adapt', 5, 0, 4, 0, 258120, 'I(2, 2, \'Tetrahedra\', 16108, false, 1, \'Disk\', \'168 KB\')', true, true)
			ProfileItem('Port Refine', 3, 0, 3, 0, 61744, 'I(2, 2, \'Tetrahedra\', 31494, false, 2, \'Cores\', 1, false)', true, true)
		$end 'ProfileGroup'
		$begin 'ProfileGroup'
			MajorVer=2024
			MinorVer=1
			Name='Adaptive Meshing'
			$begin 'StartInfo'
				I(1, 'Time', '10/08/2025 20:06:29')
			$end 'StartInfo'
			$begin 'TotalInfo'
				I(1, 'Elapsed Time', '00:14:01')
			$end 'TotalInfo'
			GroupOptions=4
			TaskDataOptions('CPU Time'=8, Memory=8, 'Real Time'=8)
			$begin 'ProfileGroup'
				MajorVer=2024
				MinorVer=1
				Name='Adaptive Pass 1'
				$begin 'StartInfo'
					I(1, 'Frequency', '1.57542GHz')
				$end 'StartInfo'
				$begin 'TotalInfo'
					I(0, ' ')
				$end 'TotalInfo'
				GroupOptions=0
				TaskDataOptions('CPU Time'=8, Memory=8, 'Real Time'=8)
				ProfileItem(' ', 0, 0, 0, 0, 0, 'I(1, 0, \'\')', false, true)
				ProfileItem('Simulation Setup ', 1, 0, 1, 0, 251600, 'I(2, 2, \'Tetrahedra\', 16382, false, 1, \'Disk\', \'12.6 KB\')', true, true)
				ProfileItem('Matrix Assembly', 3, 0, 3, 0, 300960, 'I(6, 2, \'Tetrahedra\', 16382, false, 2, \'1 Triangles\', 98, false, 2, \'2 Triangles\', 100, false, 2, \'3 Triangles\', 103, false, 2, \'4 Triangles\', 100, false, 1, \'Disk\', \'0 Bytes\')', true, true)
				ProfileItem('Matrix Solve', 5, 0, 5, 0, 641892, 'I(5, 1, \'Type\', \'DCS\', 2, \'Cores\', 1, false, 2, \'Matrix size\', 120872, false, 3, \'Matrix bandwidth\', 19.2563, \'%5.1f\', 1, \'Disk\', \'839 Bytes\')', true, true)
				ProfileItem('Field Recovery', 3, 0, 3, 0, 641892, 'I(2, 2, \'Excitations\', 4, false, 1, \'Disk\', \'2.26 MB\')', true, true)
				ProfileItem('Data Transfer', 0, 0, 0, 0, 76900, 'I(1, 0, \'Adaptive Pass 1\')', true, true)
			$end 'ProfileGroup'
			ProfileItem('', 0, 0, 0, 0, 0, 'I(1, 0, \'\')', false, true)
			$begin 'ProfileGroup'
				MajorVer=2024
				MinorVer=1
				Name='Adaptive Pass 2'
				$begin 'StartInfo'
					I(1, 'Frequency', '1.57542GHz')
				$end 'StartInfo'
				$begin 'TotalInfo'
					I(0, ' ')
				$end 'TotalInfo'
				GroupOptions=0
				TaskDataOptions('CPU Time'=8, Memory=8, 'Real Time'=8)
				ProfileItem('Adaptive Refine', 3, 0, 3, 0, 63832, 'I(2, 2, \'Tetrahedra\', 35158, false, 2, \'Cores\', 1, false)', true, true)
				ProfileItem(' ', 0, 0, 0, 0, 0, 'I(1, 0, \'\')', false, true)
				ProfileItem('Simulation Setup ', 1, 0, 1, 0, 259196, 'I(2, 2, \'Tetrahedra\', 19198, false, 1, \'Disk\', \'15.9 KB\')', true, true)
				ProfileItem('Matrix Assembly', 3, 0, 3, 0, 316128, 'I(6, 2, \'Tetrahedra\', 19198, false, 2, \'1 Triangles\', 98, false, 2, \'2 Triangles\', 100, false, 2, \'3 Triangles\', 103, false, 2, \'4 Triangles\', 100, false, 1, \'Disk\', \'0 Bytes\')', true, true)
				ProfileItem('Matrix Solve', 6, 0, 6, 0, 747712, 'I(5, 1, \'Type\', \'DCS\', 2, \'Cores\', 1, false, 2, \'Matrix size\', 140132, false, 3, \'Matrix bandwidth\', 19.5182, \'%5.1f\', 1, \'Disk\', \'1 Bytes\')', true, true)
				ProfileItem('Field Recovery', 2, 0, 2, 0, 747712, 'I(2, 2, \'Excitations\', 4, false, 1, \'Disk\', \'938 KB\')', true, true)
				ProfileItem('Data Transfer', 0, 0, 0, 0, 77180, 'I(1, 0, \'Adaptive Pass 2\')', true, true)
				ProfileItem('', 0, 0, 0, 0, 0, 'I(1, 3, \'Max Mag. Delta S\', 0.517224, \'%.5f\')', false, true)
			$end 'ProfileGroup'
			ProfileItem('', 0, 0, 0, 0, 0, 'I(1, 0, \'\')', false, true)
			$begin 'ProfileGroup'
				MajorVer=2024
				MinorVer=1
				Name='Adaptive Pass 3'
				$begin 'StartInfo'
					I(1, 'Frequency', '1.57542GHz')
				$end 'StartInfo'
				$begin 'TotalInfo'
					I(0, ' ')
				$end 'TotalInfo'
				GroupOptions=0
				TaskDataOptions('CPU Time'=8, Memory=8, 'Real Time'=8)
				ProfileItem('Adaptive Refine', 3, 0, 3, 0, 64632, 'I(2, 2, \'Tetrahedra\', 38414, false, 2, \'Cores\', 1, false)', true, true)
				ProfileItem(' ', 0, 0, 0, 0, 0, 'I(1, 0, \'\')', false, true)
				ProfileItem('Simulation Setup ', 1, 0, 1, 0, 267556, 'I(2, 2, \'Tetrahedra\', 21707, false, 1, \'Disk\', \'17.4 KB\')', true, true)
				ProfileItem('Matrix Assembly', 4, 0, 4, 0, 331600, 'I(6, 2, \'Tetrahedra\', 21707, false, 2, \'1 Triangles\', 98, false, 2, \'2 Triangles\', 100, false, 2, \'3 Triangles\', 103, false, 2, \'4 Triangles\', 100, false, 1, \'Disk\', \'0 Bytes\')', true, true)
				ProfileItem('Matrix Solve', 7, 0, 7, 0, 843088, 'I(5, 1, \'Type\', \'DCS\', 2, \'Cores\', 1, false, 2, \'Matrix size\', 157452, false, 3, \'Matrix bandwidth\', 19.6828, \'%5.1f\', 1, \'Disk\', \'1 Bytes\')', true, true)
				ProfileItem('Field Recovery', 2, 0, 2, 0, 843088, 'I(2, 2, \'Excitations\', 4, false, 1, \'Disk\', \'956 KB\')', true, true)
				ProfileItem('Data Transfer', 0, 0, 0, 0, 77240, 'I(1, 0, \'Adaptive Pass 3\')', true, true)
				ProfileItem('', 0, 0, 0, 0, 0, 'I(1, 3, \'Max Mag. Delta S\', 0.388864, \'%.5f\')', false, true)
			$end 'ProfileGroup'
			ProfileItem('', 0, 0, 0, 0, 0, 'I(1, 0, \'\')', false, true)
			$begin 'ProfileGroup'
				MajorVer=2024
				MinorVer=1
				Name='Adaptive Pass 4'
				$begin 'StartInfo'
					I(1, 'Frequency', '1.57542GHz')
				$end 'StartInfo'
				$begin 'TotalInfo'
					I(0, ' ')
				$end 'TotalInfo'
				GroupOptions=0
				TaskDataOptions('CPU Time'=8, Memory=8, 'Real Time'=8)
				ProfileItem('Adaptive Refine', 2, 0, 2, 0, 63504, 'I(2, 2, \'Tetrahedra\', 39653, false, 2, \'Cores\', 1, false)', true, true)
				ProfileItem(' ', 0, 0, 0, 0, 0, 'I(1, 0, \'\')', false, true)
				ProfileItem('Simulation Setup ', 1, 0, 1, 0, 270096, 'I(2, 2, \'Tetrahedra\', 22796, false, 1, \'Disk\', \'17.8 KB\')', true, true)
				ProfileItem('Matrix Assembly', 4, 0, 4, 0, 337132, 'I(6, 2, \'Tetrahedra\', 22796, false, 2, \'1 Triangles\', 98, false, 2, \'2 Triangles\', 100, false, 2, \'3 Triangles\', 103, false, 2, \'4 Triangles\', 100, false, 1, \'Disk\', \'0 Bytes\')', true, true)
				ProfileItem('Matrix Solve', 8, 0, 8, 0, 877440, 'I(5, 1, \'Type\', \'DCS\', 2, \'Cores\', 1, false, 2, \'Matrix size\', 164598, false, 3, \'Matrix bandwidth\', 19.7734, \'%5.1f\', 1, \'Disk\', \'1 Bytes\')', true, true)
				ProfileItem('Field Recovery', 2, 0, 2, 0, 877440, 'I(2, 2, \'Excitations\', 4, false, 1, \'Disk\', \'824 KB\')', true, true)
				ProfileItem('Data Transfer', 0, 0, 0, 0, 77316, 'I(1, 0, \'Adaptive Pass 4\')', true, true)
				ProfileItem('', 0, 0, 0, 0, 0, 'I(1, 3, \'Max Mag. Delta S\', 0.317842, \'%.5f\')', false, true)
			$end 'ProfileGroup'
			ProfileItem('', 0, 0, 0, 0, 0, 'I(1, 0, \'\')', false, true)
			$begin 'ProfileGroup'
				MajorVer=2024
				MinorVer=1
				Name='Adaptive Pass 5'
				$begin 'StartInfo'
					I(1, 'Frequency', '1.57542GHz')
				$end 'StartInfo'
				$begin 'TotalInfo'
					I(0, ' ')
				$end 'TotalInfo'
				GroupOptions=0
				TaskDataOptions('CPU Time'=8, Memory=8, 'Real Time'=8)
				ProfileItem('Adaptive Refine', 3, 0, 3, 0, 67516, 'I(2, 2, \'Tetrahedra\', 42310, false, 2, \'Cores\', 1, false)', true, true)
				ProfileItem(' ', 0, 0, 0, 0, 0, 'I(1, 0, \'\')', false, true)
				ProfileItem('Simulation Setup ', 1, 0, 1, 0, 275512, 'I(2, 2, \'Tetrahedra\', 24896, false, 1, \'Disk\', \'18.2 KB\')', true, true)
				ProfileItem('Matrix Assembly', 4, 0, 4, 0, 348120, 'I(6, 2, \'Tetrahedra\', 24896, false, 2, \'1 Triangles\', 98, false, 2, \'2 Triangles\', 100, false, 2, \'3 Triangles\', 103, false, 2, \'4 Triangles\', 100, false, 1, \'Disk\', \'0 Bytes\')', true, true)
				ProfileItem('Matrix Solve', 9, 0, 9, 0, 945268, 'I(5, 1, \'Type\', \'DCS\', 2, \'Cores\', 1, false, 2, \'Matrix size\', 178920, false, 3, \'Matrix bandwidth\', 19.8872, \'%5.1f\', 1, \'Disk\', \'1 Bytes\')', true, true)
				ProfileItem('Field Recovery', 3, 0, 3, 0, 945268, 'I(2, 2, \'Excitations\', 4, false, 1, \'Disk\', \'975 KB\')', true, true)
				ProfileItem('Data Transfer', 0, 0, 0, 0, 77320, 'I(1, 0, \'Adaptive Pass 5\')', true, true)
				ProfileItem('', 0, 0, 0, 0, 0, 'I(1, 3, \'Max Mag. Delta S\', 0.263985, \'%.5f\')', false, true)
			$end 'ProfileGroup'
			ProfileItem('', 0, 0, 0, 0, 0, 'I(1, 0, \'\')', false, true)
			$begin 'ProfileGroup'
				MajorVer=2024
				MinorVer=1
				Name='Adaptive Pass 6'
				$begin 'StartInfo'
					I(1, 'Frequency', '1.57542GHz')
				$end 'StartInfo'
				$begin 'TotalInfo'
					I(0, ' ')
				$end 'TotalInfo'
				GroupOptions=0
				TaskDataOptions('CPU Time'=8, Memory=8, 'Real Time'=8)
				ProfileItem('Adaptive Refine', 2, 0, 3, 0, 66308, 'I(2, 2, \'Tetrahedra\', 43558, false, 2, \'Cores\', 1, false)', true, true)
				ProfileItem(' ', 0, 0, 0, 0, 0, 'I(1, 0, \'\')', false, true)
				ProfileItem('Simulation Setup ', 1, 0, 1, 0, 278604, 'I(2, 2, \'Tetrahedra\', 25961, false, 1, \'Disk\', \'21.3 KB\')', true, true)
				ProfileItem('Matrix Assembly', 4, 0, 4, 0, 353744, 'I(6, 2, \'Tetrahedra\', 25961, false, 2, \'1 Triangles\', 98, false, 2, \'2 Triangles\', 100, false, 2, \'3 Triangles\', 103, false, 2, \'4 Triangles\', 100, false, 1, \'Disk\', \'0 Bytes\')', true, true)
				ProfileItem('Matrix Solve', 9, 0, 9, 0, 981264, 'I(5, 1, \'Type\', \'DCS\', 2, \'Cores\', 1, false, 2, \'Matrix size\', 186028, false, 3, \'Matrix bandwidth\', 19.9494, \'%5.1f\', 1, \'Disk\', \'1 Bytes\')', true, true)
				ProfileItem('Field Recovery', 3, 0, 4, 0, 981264, 'I(2, 2, \'Excitations\', 4, false, 1, \'Disk\', \'884 KB\')', true, true)
				ProfileItem('Data Transfer', 0, 0, 0, 0, 77328, 'I(1, 0, \'Adaptive Pass 6\')', true, true)
				ProfileItem('', 0, 0, 0, 0, 0, 'I(1, 3, \'Max Mag. Delta S\', 0.206901, \'%.5f\')', false, true)
			$end 'ProfileGroup'
			ProfileItem('', 0, 0, 0, 0, 0, 'I(1, 0, \'\')', false, true)
			$begin 'ProfileGroup'
				MajorVer=2024
				MinorVer=1
				Name='Adaptive Pass 7'
				$begin 'StartInfo'
					I(1, 'Frequency', '1.57542GHz')
				$end 'StartInfo'
				$begin 'TotalInfo'
					I(0, ' ')
				$end 'TotalInfo'
				GroupOptions=0
				TaskDataOptions('CPU Time'=8, Memory=8, 'Real Time'=8)
				ProfileItem('Adaptive Refine', 3, 0, 3, 0, 68296, 'I(2, 2, \'Tetrahedra\', 44979, false, 2, \'Cores\', 1, false)', true, true)
				ProfileItem(' ', 0, 0, 0, 0, 0, 'I(1, 0, \'\')', false, true)
				ProfileItem('Simulation Setup ', 1, 0, 1, 0, 283668, 'I(2, 2, \'Tetrahedra\', 27115, false, 1, \'Disk\', \'21.3 KB\')', true, true)
				ProfileItem('Matrix Assembly', 4, 0, 4, 0, 361080, 'I(6, 2, \'Tetrahedra\', 27115, false, 2, \'1 Triangles\', 98, false, 2, \'2 Triangles\', 100, false, 2, \'3 Triangles\', 103, false, 2, \'4 Triangles\', 100, false, 1, \'Disk\', \'2 Bytes\')', true, true)
				ProfileItem('Matrix Solve', 9, 0, 9, 0, 1019608, 'I(5, 1, \'Type\', \'DCS\', 2, \'Cores\', 1, false, 2, \'Matrix size\', 193816, false, 3, \'Matrix bandwidth\', 20.0054, \'%5.1f\', 1, \'Disk\', \'1 Bytes\')', true, true)
				ProfileItem('Field Recovery', 3, 0, 3, 0, 1019608, 'I(2, 2, \'Excitations\', 4, false, 1, \'Disk\', \'916 KB\')', true, true)
				ProfileItem('Data Transfer', 0, 0, 0, 0, 77336, 'I(1, 0, \'Adaptive Pass 7\')', true, true)
				ProfileItem('', 0, 0, 0, 0, 0, 'I(1, 3, \'Max Mag. Delta S\', 0.210394, \'%.5f\')', false, true)
			$end 'ProfileGroup'
			ProfileItem('', 0, 0, 0, 0, 0, 'I(1, 0, \'\')', false, true)
			$begin 'ProfileGroup'
				MajorVer=2024
				MinorVer=1
				Name='Adaptive Pass 8'
				$begin 'StartInfo'
					I(1, 'Frequency', '1.57542GHz')
				$end 'StartInfo'
				$begin 'TotalInfo'
					I(0, ' ')
				$end 'TotalInfo'
				GroupOptions=0
				TaskDataOptions('CPU Time'=8, Memory=8, 'Real Time'=8)
				ProfileItem('Adaptive Refine', 2, 0, 3, 0, 69232, 'I(2, 2, \'Tetrahedra\', 46339, false, 2, \'Cores\', 1, false)', true, true)
				ProfileItem(' ', 0, 0, 0, 0, 0, 'I(1, 0, \'\')', false, true)
				ProfileItem('Simulation Setup ', 1, 0, 1, 0, 286076, 'I(2, 2, \'Tetrahedra\', 28192, false, 1, \'Disk\', \'21.7 KB\')', true, true)
				ProfileItem('Matrix Assembly', 4, 0, 4, 0, 365820, 'I(6, 2, \'Tetrahedra\', 28192, false, 2, \'1 Triangles\', 98, false, 2, \'2 Triangles\', 100, false, 2, \'3 Triangles\', 103, false, 2, \'4 Triangles\', 100, false, 1, \'Disk\', \'0 Bytes\')', true, true)
				ProfileItem('Matrix Solve', 10, 0, 10, 0, 1056664, 'I(5, 1, \'Type\', \'DCS\', 2, \'Cores\', 1, false, 2, \'Matrix size\', 201202, false, 3, \'Matrix bandwidth\', 20.046, \'%5.1f\', 1, \'Disk\', \'1 Bytes\')', true, true)
				ProfileItem('Field Recovery', 4, 0, 4, 0, 1056664, 'I(2, 2, \'Excitations\', 4, false, 1, \'Disk\', \'930 KB\')', true, true)
				ProfileItem('Data Transfer', 0, 0, 0, 0, 77340, 'I(1, 0, \'Adaptive Pass 8\')', true, true)
				ProfileItem('', 0, 0, 0, 0, 0, 'I(1, 3, \'Max Mag. Delta S\', 0.103327, \'%.5f\')', false, true)
			$end 'ProfileGroup'
			ProfileItem('', 0, 0, 0, 0, 0, 'I(1, 0, \'\')', false, true)
			$begin 'ProfileGroup'
				MajorVer=2024
				MinorVer=1
				Name='Adaptive Pass 9'
				$begin 'StartInfo'
					I(1, 'Frequency', '1.57542GHz')
				$end 'StartInfo'
				$begin 'TotalInfo'
					I(0, ' ')
				$end 'TotalInfo'
				GroupOptions=0
				TaskDataOptions('CPU Time'=8, Memory=8, 'Real Time'=8)
				ProfileItem('Adaptive Refine', 3, 0, 3, 0, 74916, 'I(2, 2, \'Tetrahedra\', 50536, false, 2, \'Cores\', 1, false)', true, true)
				ProfileItem(' ', 0, 0, 0, 0, 0, 'I(1, 0, \'\')', false, true)
				ProfileItem('Simulation Setup ', 1, 0, 1, 0, 293084, 'I(2, 2, \'Tetrahedra\', 31198, false, 1, \'Disk\', \'22.4 KB\')', true, true)
				ProfileItem('Matrix Assembly', 5, 0, 5, 0, 382724, 'I(6, 2, \'Tetrahedra\', 31198, false, 2, \'1 Triangles\', 98, false, 2, \'2 Triangles\', 100, false, 2, \'3 Triangles\', 103, false, 2, \'4 Triangles\', 100, false, 1, \'Disk\', \'0 Bytes\')', true, true)
				ProfileItem('Matrix Solve', 11, 0, 11, 0, 1154380, 'I(5, 1, \'Type\', \'DCS\', 2, \'Cores\', 1, false, 2, \'Matrix size\', 222408, false, 3, \'Matrix bandwidth\', 20.1085, \'%5.1f\', 1, \'Disk\', \'1 Bytes\')', true, true)
				ProfileItem('Field Recovery', 4, 0, 4, 0, 1154380, 'I(2, 2, \'Excitations\', 4, false, 1, \'Disk\', \'1.17 MB\')', true, true)
				ProfileItem('Data Transfer', 0, 0, 0, 0, 77356, 'I(1, 0, \'Adaptive Pass 9\')', true, true)
				ProfileItem('', 0, 0, 0, 0, 0, 'I(1, 3, \'Max Mag. Delta S\', 0.127898, \'%.5f\')', false, true)
			$end 'ProfileGroup'
			ProfileItem('', 0, 0, 0, 0, 0, 'I(1, 0, \'\')', false, true)
			$begin 'ProfileGroup'
				MajorVer=2024
				MinorVer=1
				Name='Adaptive Pass 10'
				$begin 'StartInfo'
					I(1, 'Frequency', '1.57542GHz')
				$end 'StartInfo'
				$begin 'TotalInfo'
					I(0, ' ')
				$end 'TotalInfo'
				GroupOptions=0
				TaskDataOptions('CPU Time'=8, Memory=8, 'Real Time'=8)
				ProfileItem('Adaptive Refine', 3, 0, 3, 0, 72172, 'I(2, 2, \'Tetrahedra\', 52103, false, 2, \'Cores\', 1, false)', true, true)
				ProfileItem(' ', 0, 0, 0, 0, 0, 'I(1, 0, \'\')', false, true)
				ProfileItem('Simulation Setup ', 1, 0, 1, 0, 296176, 'I(2, 2, \'Tetrahedra\', 32445, false, 1, \'Disk\', \'25.2 KB\')', true, true)
				ProfileItem('Matrix Assembly', 5, 0, 5, 0, 389252, 'I(6, 2, \'Tetrahedra\', 32445, false, 2, \'1 Triangles\', 98, false, 2, \'2 Triangles\', 100, false, 2, \'3 Triangles\', 103, false, 2, \'4 Triangles\', 100, false, 1, \'Disk\', \'0 Bytes\')', true, true)
				ProfileItem('Matrix Solve', 12, 0, 12, 0, 1190236, 'I(5, 1, \'Type\', \'DCS\', 2, \'Cores\', 1, false, 2, \'Matrix size\', 230920, false, 3, \'Matrix bandwidth\', 20.1478, \'%5.1f\', 1, \'Disk\', \'1 Bytes\')', true, true)
				ProfileItem('Field Recovery', 4, 0, 4, 0, 1190236, 'I(2, 2, \'Excitations\', 4, false, 1, \'Disk\', \'1.01 MB\')', true, true)
				ProfileItem('Data Transfer', 0, 0, 0, 0, 77404, 'I(1, 0, \'Adaptive Pass 10\')', true, true)
				ProfileItem('', 0, 0, 0, 0, 0, 'I(1, 3, \'Max Mag. Delta S\', 0.083948, \'%.5f\')', false, true)
			$end 'ProfileGroup'
			ProfileItem('', 0, 0, 0, 0, 0, 'I(1, 0, \'\')', false, true)
			$begin 'ProfileGroup'
				MajorVer=2024
				MinorVer=1
				Name='Adaptive Pass 11'
				$begin 'StartInfo'
					I(1, 'Frequency', '1.57542GHz')
				$end 'StartInfo'
				$begin 'TotalInfo'
					I(0, ' ')
				$end 'TotalInfo'
				GroupOptions=0
				TaskDataOptions('CPU Time'=8, Memory=8, 'Real Time'=8)
				ProfileItem('Adaptive Refine', 4, 0, 4, 0, 80036, 'I(2, 2, \'Tetrahedra\', 56524, false, 2, \'Cores\', 1, false)', true, true)
				ProfileItem(' ', 0, 0, 0, 0, 0, 'I(1, 0, \'\')', false, true)
				ProfileItem('Simulation Setup ', 2, 0, 2, 0, 304656, 'I(2, 2, \'Tetrahedra\', 35693, false, 1, \'Disk\', \'24.4 KB\')', true, true)
				ProfileItem('Matrix Assembly', 5, 0, 5, 0, 407172, 'I(6, 2, \'Tetrahedra\', 35693, false, 2, \'1 Triangles\', 98, false, 2, \'2 Triangles\', 100, false, 2, \'3 Triangles\', 103, false, 2, \'4 Triangles\', 100, false, 1, \'Disk\', \'0 Bytes\')', true, true)
				ProfileItem('Matrix Solve', 13, 0, 13, 0, 1295972, 'I(5, 1, \'Type\', \'DCS\', 2, \'Cores\', 1, false, 2, \'Matrix size\', 253622, false, 3, \'Matrix bandwidth\', 20.2092, \'%5.1f\', 1, \'Disk\', \'1 Bytes\')', true, true)
				ProfileItem('Field Recovery', 4, 0, 4, 0, 1295972, 'I(2, 2, \'Excitations\', 4, false, 1, \'Disk\', \'1.29 MB\')', true, true)
				ProfileItem('Data Transfer', 0, 0, 0, 0, 77428, 'I(1, 0, \'Adaptive Pass 11\')', true, true)
				ProfileItem('', 0, 0, 0, 0, 0, 'I(1, 3, \'Max Mag. Delta S\', 0.0337702, \'%.5f\')', false, true)
			$end 'ProfileGroup'
			ProfileItem('', 0, 0, 0, 0, 0, 'I(1, 0, \'\')', false, true)
			$begin 'ProfileGroup'
				MajorVer=2024
				MinorVer=1
				Name='Adaptive Pass 12'
				$begin 'StartInfo'
					I(1, 'Frequency', '1.57542GHz')
				$end 'StartInfo'
				$begin 'TotalInfo'
					I(0, ' ')
				$end 'TotalInfo'
				GroupOptions=0
				TaskDataOptions('CPU Time'=8, Memory=8, 'Real Time'=8)
				ProfileItem('Adaptive Refine', 4, 0, 4, 0, 87836, 'I(2, 2, \'Tetrahedra\', 62457, false, 2, \'Cores\', 1, false)', true, true)
				ProfileItem(' ', 0, 0, 0, 0, 0, 'I(1, 0, \'\')', false, true)
				ProfileItem('Simulation Setup ', 2, 0, 2, 0, 318480, 'I(2, 2, \'Tetrahedra\', 40006, false, 1, \'Disk\', \'26.8 KB\')', true, true)
				ProfileItem('Matrix Assembly', 6, 0, 6, 0, 433572, 'I(6, 2, \'Tetrahedra\', 40006, false, 2, \'1 Triangles\', 98, false, 2, \'2 Triangles\', 100, false, 2, \'3 Triangles\', 103, false, 2, \'4 Triangles\', 100, false, 1, \'Disk\', \'0 Bytes\')', true, true)
				ProfileItem('Matrix Solve', 16, 0, 16, 0, 1441120, 'I(5, 1, \'Type\', \'DCS\', 2, \'Cores\', 1, false, 2, \'Matrix size\', 283870, false, 3, \'Matrix bandwidth\', 20.2701, \'%5.1f\', 1, \'Disk\', \'1 Bytes\')', true, true)
				ProfileItem('Field Recovery', 4, 0, 4, 0, 1441120, 'I(2, 2, \'Excitations\', 4, false, 1, \'Disk\', \'1.49 MB\')', true, true)
				ProfileItem('Data Transfer', 0, 0, 0, 0, 77548, 'I(1, 0, \'Adaptive Pass 12\')', true, true)
				ProfileItem('', 0, 0, 0, 0, 0, 'I(1, 3, \'Max Mag. Delta S\', 0.0480686, \'%.5f\')', false, true)
			$end 'ProfileGroup'
			ProfileItem('', 0, 0, 0, 0, 0, 'I(1, 0, \'\')', false, true)
			$begin 'ProfileGroup'
				MajorVer=2024
				MinorVer=1
				Name='Adaptive Pass 13'
				$begin 'StartInfo'
					I(1, 'Frequency', '1.57542GHz')
				$end 'StartInfo'
				$begin 'TotalInfo'
					I(0, ' ')
				$end 'TotalInfo'
				GroupOptions=0
				TaskDataOptions('CPU Time'=8, Memory=8, 'Real Time'=8)
				ProfileItem('Adaptive Refine', 3, 0, 3, 0, 84720, 'I(2, 2, \'Tetrahedra\', 64476, false, 2, \'Cores\', 1, false)', true, true)
				ProfileItem(' ', 0, 0, 0, 0, 0, 'I(1, 0, \'\')', false, true)
				ProfileItem('Simulation Setup ', 2, 0, 2, 0, 322532, 'I(2, 2, \'Tetrahedra\', 41685, false, 1, \'Disk\', \'27.2 KB\')', true, true)
				ProfileItem('Matrix Assembly', 6, 0, 6, 0, 442664, 'I(6, 2, \'Tetrahedra\', 41685, false, 2, \'1 Triangles\', 98, false, 2, \'2 Triangles\', 100, false, 2, \'3 Triangles\', 103, false, 2, \'4 Triangles\', 100, false, 1, \'Disk\', \'0 Bytes\')', true, true)
				ProfileItem('Matrix Solve', 17, 0, 16, 0, 1495280, 'I(5, 1, \'Type\', \'DCS\', 2, \'Cores\', 1, false, 2, \'Matrix size\', 295168, false, 3, \'Matrix bandwidth\', 20.3132, \'%5.1f\', 1, \'Disk\', \'1 Bytes\')', true, true)
				ProfileItem('Field Recovery', 6, 0, 5, 0, 1495280, 'I(2, 2, \'Excitations\', 4, false, 1, \'Disk\', \'1.25 MB\')', true, true)
				ProfileItem('Data Transfer', 0, 0, 0, 0, 77528, 'I(1, 0, \'Adaptive Pass 13\')', true, true)
				ProfileItem('', 0, 0, 0, 0, 0, 'I(1, 3, \'Max Mag. Delta S\', 0.0447682, \'%.5f\')', false, true)
			$end 'ProfileGroup'
			ProfileItem('', 0, 0, 0, 0, 0, 'I(1, 0, \'\')', false, true)
			$begin 'ProfileGroup'
				MajorVer=2024
				MinorVer=1
				Name='Adaptive Pass 14'
				$begin 'StartInfo'
					I(1, 'Frequency', '1.57542GHz')
				$end 'StartInfo'
				$begin 'TotalInfo'
					I(0, ' ')
				$end 'TotalInfo'
				GroupOptions=0
				TaskDataOptions('CPU Time'=8, Memory=8, 'Real Time'=8)
				ProfileItem('Adaptive Refine', 5, 0, 5, 0, 91856, 'I(2, 2, \'Tetrahedra\', 69568, false, 2, \'Cores\', 1, false)', true, true)
				ProfileItem(' ', 0, 0, 0, 0, 0, 'I(1, 0, \'\')', false, true)
				ProfileItem('Simulation Setup ', 3, 0, 2, 0, 332848, 'I(2, 2, \'Tetrahedra\', 45569, false, 1, \'Disk\', \'30.7 KB\')', true, true)
				ProfileItem('Matrix Assembly', 6, 0, 6, 0, 463812, 'I(6, 2, \'Tetrahedra\', 45569, false, 2, \'1 Triangles\', 98, false, 2, \'2 Triangles\', 100, false, 2, \'3 Triangles\', 103, false, 2, \'4 Triangles\', 100, false, 1, \'Disk\', \'0 Bytes\')', true, true)
				ProfileItem('Matrix Solve', 18, 0, 18, 0, 1625592, 'I(5, 1, \'Type\', \'DCS\', 2, \'Cores\', 1, false, 2, \'Matrix size\', 322068, false, 3, \'Matrix bandwidth\', 20.3675, \'%5.1f\', 1, \'Disk\', \'1 Bytes\')', true, true)
				ProfileItem('Field Recovery', 8, 0, 6, 0, 1625592, 'I(2, 2, \'Excitations\', 4, false, 1, \'Disk\', \'1.56 MB\')', true, true)
				ProfileItem('Data Transfer', 0, 0, 0, 0, 77532, 'I(1, 0, \'Adaptive Pass 14\')', true, true)
				ProfileItem('', 0, 0, 0, 0, 0, 'I(1, 3, \'Max Mag. Delta S\', 0.0929056, \'%.5f\')', false, true)
			$end 'ProfileGroup'
			ProfileItem('', 0, 0, 0, 0, 0, 'I(1, 0, \'\')', false, true)
			$begin 'ProfileGroup'
				MajorVer=2024
				MinorVer=1
				Name='Adaptive Pass 15'
				$begin 'StartInfo'
					I(1, 'Frequency', '1.57542GHz')
				$end 'StartInfo'
				$begin 'TotalInfo'
					I(0, ' ')
				$end 'TotalInfo'
				GroupOptions=0
				TaskDataOptions('CPU Time'=8, Memory=8, 'Real Time'=8)
				ProfileItem('Adaptive Refine', 7, 0, 6, 0, 102800, 'I(2, 2, \'Tetrahedra\', 78080, false, 2, \'Cores\', 1, false)', true, true)
				ProfileItem(' ', 0, 0, 0, 0, 0, 'I(1, 0, \'\')', false, true)
				ProfileItem('Simulation Setup ', 4, 0, 3, 0, 353080, 'I(2, 2, \'Tetrahedra\', 51786, false, 1, \'Disk\', \'35.3 KB\')', true, true)
				ProfileItem('Matrix Assembly', 9, 0, 8, 0, 499864, 'I(6, 2, \'Tetrahedra\', 51786, false, 2, \'1 Triangles\', 98, false, 2, \'2 Triangles\', 100, false, 2, \'3 Triangles\', 103, false, 2, \'4 Triangles\', 100, false, 1, \'Disk\', \'0 Bytes\')', true, true)
				ProfileItem('Matrix Solve', 24, 0, 22, 0, 1833496, 'I(5, 1, \'Type\', \'DCS\', 2, \'Cores\', 1, false, 2, \'Matrix size\', 365734, false, 3, \'Matrix bandwidth\', 20.4144, \'%5.1f\', 1, \'Disk\', \'1 Bytes\')', true, true)
				ProfileItem('Field Recovery', 7, 0, 6, 0, 1833496, 'I(2, 2, \'Excitations\', 4, false, 1, \'Disk\', \'1.94 MB\')', true, true)
				ProfileItem('Data Transfer', 0, 0, 0, 0, 77544, 'I(1, 0, \'Adaptive Pass 15\')', true, true)
				ProfileItem('', 0, 0, 0, 0, 0, 'I(1, 3, \'Max Mag. Delta S\', 0.075969, \'%.5f\')', false, true)
			$end 'ProfileGroup'
			ProfileItem('', 0, 0, 0, 0, 0, 'I(1, 0, \'\')', false, true)
			$begin 'ProfileGroup'
				MajorVer=2024
				MinorVer=1
				Name='Adaptive Pass 16'
				$begin 'StartInfo'
					I(1, 'Frequency', '1.57542GHz')
				$end 'StartInfo'
				$begin 'TotalInfo'
					I(0, ' ')
				$end 'TotalInfo'
				GroupOptions=0
				TaskDataOptions('CPU Time'=8, Memory=8, 'Real Time'=8)
				ProfileItem('Adaptive Refine', 5, 0, 5, 0, 107260, 'I(2, 2, \'Tetrahedra\', 85851, false, 2, \'Cores\', 1, false)', true, true)
				ProfileItem(' ', 0, 0, 0, 0, 0, 'I(1, 0, \'\')', false, true)
				ProfileItem('Simulation Setup ', 2, 0, 2, 0, 371504, 'I(2, 2, \'Tetrahedra\', 57539, false, 1, \'Disk\', \'38.8 KB\')', true, true)
				ProfileItem('Matrix Assembly', 8, 0, 8, 0, 534832, 'I(6, 2, \'Tetrahedra\', 57539, false, 2, \'1 Triangles\', 98, false, 2, \'2 Triangles\', 100, false, 2, \'3 Triangles\', 103, false, 2, \'4 Triangles\', 100, false, 1, \'Disk\', \'0 Bytes\')', true, true)
				ProfileItem('Matrix Solve', 26, 0, 24, 0, 1873276, 'I(5, 1, \'Type\', \'DCS\', 2, \'Cores\', 1, false, 2, \'Matrix size\', 405748, false, 3, \'Matrix bandwidth\', 20.4625, \'%5.1f\', 1, \'Disk\', \'1 Bytes\')', true, true)
				ProfileItem('Field Recovery', 6, 0, 6, 0, 1873276, 'I(2, 2, \'Excitations\', 4, false, 1, \'Disk\', \'2.01 MB\')', true, true)
				ProfileItem('Data Transfer', 0, 0, 0, 0, 77548, 'I(1, 0, \'Adaptive Pass 16\')', true, true)
				ProfileItem('', 0, 0, 0, 0, 0, 'I(1, 3, \'Max Mag. Delta S\', 0.0793048, \'%.5f\')', false, true)
			$end 'ProfileGroup'
			ProfileItem('', 0, 0, 0, 0, 0, 'I(1, 0, \'\')', false, true)
			$begin 'ProfileGroup'
				MajorVer=2024
				MinorVer=1
				Name='Adaptive Pass 17'
				$begin 'StartInfo'
					I(1, 'Frequency', '1.57542GHz')
				$end 'StartInfo'
				$begin 'TotalInfo'
					I(0, ' ')
				$end 'TotalInfo'
				GroupOptions=0
				TaskDataOptions('CPU Time'=8, Memory=8, 'Real Time'=8)
				ProfileItem('Adaptive Refine', 6, 0, 6, 0, 115180, 'I(2, 2, \'Tetrahedra\', 92951, false, 2, \'Cores\', 1, false)', true, true)
				ProfileItem(' ', 0, 0, 0, 0, 0, 'I(1, 0, \'\')', false, true)
				ProfileItem('Simulation Setup ', 5, 0, 3, 0, 386212, 'I(2, 2, \'Tetrahedra\', 62902, false, 1, \'Disk\', \'38.9 KB\')', true, true)
				ProfileItem('Matrix Assembly', 11, 0, 9, 0, 564056, 'I(6, 2, \'Tetrahedra\', 62902, false, 2, \'1 Triangles\', 98, false, 2, \'2 Triangles\', 100, false, 2, \'3 Triangles\', 103, false, 2, \'4 Triangles\', 100, false, 1, \'Disk\', \'0 Bytes\')', true, true)
				ProfileItem('Matrix Solve', 32, 0, 28, 0, 1870508, 'I(5, 1, \'Type\', \'DCS\', 2, \'Cores\', 1, false, 2, \'Matrix size\', 442962, false, 3, \'Matrix bandwidth\', 20.5024, \'%5.1f\', 1, \'Disk\', \'2 Bytes\')', true, true)
				ProfileItem('Field Recovery', 9, 0, 9, 0, 1870508, 'I(2, 2, \'Excitations\', 4, false, 1, \'Disk\', \'2.09 MB\')', true, true)
				ProfileItem('Data Transfer', 0, 0, 0, 0, 77588, 'I(1, 0, \'Adaptive Pass 17\')', true, true)
				ProfileItem('', 0, 0, 0, 0, 0, 'I(1, 3, \'Max Mag. Delta S\', 0.0914816, \'%.5f\')', false, true)
			$end 'ProfileGroup'
			ProfileItem('', 0, 0, 0, 0, 0, 'I(1, 0, \'\')', false, true)
			$begin 'ProfileGroup'
				MajorVer=2024
				MinorVer=1
				Name='Adaptive Pass 18'
				$begin 'StartInfo'
					I(1, 'Frequency', '1.57542GHz')
				$end 'StartInfo'
				$begin 'TotalInfo'
					I(0, ' ')
				$end 'TotalInfo'
				GroupOptions=0
				TaskDataOptions('CPU Time'=8, Memory=8, 'Real Time'=8)
				ProfileItem('Adaptive Refine', 7, 0, 7, 0, 124300, 'I(2, 2, \'Tetrahedra\', 103140, false, 2, \'Cores\', 1, false)', true, true)
				ProfileItem(' ', 0, 0, 0, 0, 0, 'I(1, 0, \'\')', false, true)
				ProfileItem('Simulation Setup ', 3, 0, 3, 0, 406140, 'I(2, 2, \'Tetrahedra\', 70172, false, 1, \'Disk\', \'45.5 KB\')', true, true)
				ProfileItem('Matrix Assembly', 10, 0, 10, 0, 605472, 'I(6, 2, \'Tetrahedra\', 70172, false, 2, \'1 Triangles\', 98, false, 2, \'2 Triangles\', 100, false, 2, \'3 Triangles\', 103, false, 2, \'4 Triangles\', 100, false, 1, \'Disk\', \'0 Bytes\')', true, true)
				ProfileItem('Matrix Solve', 36, 0, 32, 0, 2117584, 'I(5, 1, \'Type\', \'DCS\', 2, \'Cores\', 1, false, 2, \'Matrix size\', 494572, false, 3, \'Matrix bandwidth\', 20.5134, \'%5.1f\', 1, \'Disk\', \'1 Bytes\')', true, true)
				ProfileItem('Field Recovery', 11, 0, 10, 0, 2117584, 'I(2, 2, \'Excitations\', 4, false, 1, \'Disk\', \'2.46 MB\')', true, true)
				ProfileItem('Data Transfer', 0, 0, 0, 0, 77552, 'I(1, 0, \'Adaptive Pass 18\')', true, true)
				ProfileItem('', 0, 0, 0, 0, 0, 'I(1, 3, \'Max Mag. Delta S\', 0.048743, \'%.5f\')', false, true)
			$end 'ProfileGroup'
			ProfileItem('', 0, 0, 0, 0, 0, 'I(1, 0, \'\')', false, true)
			$begin 'ProfileGroup'
				MajorVer=2024
				MinorVer=1
				Name='Adaptive Pass 19'
				$begin 'StartInfo'
					I(1, 'Frequency', '1.57542GHz')
				$end 'StartInfo'
				$begin 'TotalInfo'
					I(0, ' ')
				$end 'TotalInfo'
				GroupOptions=0
				TaskDataOptions('CPU Time'=8, Memory=8, 'Real Time'=8)
				ProfileItem('Adaptive Refine', 5, 0, 6, 0, 125240, 'I(2, 2, \'Tetrahedra\', 107094, false, 2, \'Cores\', 1, false)', true, true)
				ProfileItem(' ', 0, 0, 0, 0, 0, 'I(1, 0, \'\')', false, true)
				ProfileItem('Simulation Setup ', 3, 0, 3, 0, 417736, 'I(2, 2, \'Tetrahedra\', 73439, false, 1, \'Disk\', \'44.3 KB\')', true, true)
				ProfileItem('Matrix Assembly', 11, 0, 10, 0, 625384, 'I(6, 2, \'Tetrahedra\', 73439, false, 2, \'1 Triangles\', 98, false, 2, \'2 Triangles\', 100, false, 2, \'3 Triangles\', 103, false, 2, \'4 Triangles\', 100, false, 1, \'Disk\', \'0 Bytes\')', true, true)
				ProfileItem('Matrix Solve', 32, 0, 30, 0, 2560428, 'I(5, 1, \'Type\', \'DCS\', 2, \'Cores\', 1, false, 2, \'Matrix size\', 516518, false, 3, \'Matrix bandwidth\', 20.552, \'%5.1f\', 1, \'Disk\', \'1 Bytes\')', true, true)
				ProfileItem('Field Recovery', 10, 0, 10, 0, 2560428, 'I(2, 2, \'Excitations\', 4, false, 1, \'Disk\', \'2.11 MB\')', true, true)
				ProfileItem('Data Transfer', 0, 0, 0, 0, 77556, 'I(1, 0, \'Adaptive Pass 19\')', true, true)
				ProfileItem('', 0, 0, 0, 0, 0, 'I(1, 3, \'Max Mag. Delta S\', 0.0484394, \'%.5f\')', false, true)
			$end 'ProfileGroup'
			ProfileItem('', 0, 0, 0, 0, 0, 'I(1, 0, \'\')', false, true)
			$begin 'ProfileGroup'
				MajorVer=2024
				MinorVer=1
				Name='Adaptive Pass 20'
				$begin 'StartInfo'
					I(1, 'Frequency', '1.57542GHz')
				$end 'StartInfo'
				$begin 'TotalInfo'
					I(0, ' ')
				$end 'TotalInfo'
				GroupOptions=0
				TaskDataOptions('CPU Time'=8, Memory=8, 'Real Time'=8)
				ProfileItem('Adaptive Refine', 9, 0, 7, 0, 136632, 'I(2, 2, \'Tetrahedra\', 117459, false, 2, \'Cores\', 1, false)', true, true)
				ProfileItem(' ', 0, 0, 0, 0, 0, 'I(1, 0, \'\')', false, true)
				ProfileItem('Simulation Setup ', 5, 0, 4, 0, 441616, 'I(2, 2, \'Tetrahedra\', 80828, false, 1, \'Disk\', \'47.1 KB\')', true, true)
				ProfileItem('Matrix Assembly', 16, 0, 13, 0, 668652, 'I(6, 2, \'Tetrahedra\', 80828, false, 2, \'1 Triangles\', 98, false, 2, \'2 Triangles\', 100, false, 2, \'3 Triangles\', 103, false, 2, \'4 Triangles\', 100, false, 1, \'Disk\', \'0 Bytes\')', true, true)
				ProfileItem('Matrix Solve', 39, 0, 35, 0, 2799068, 'I(5, 1, \'Type\', \'DCS\', 2, \'Cores\', 1, false, 2, \'Matrix size\', 568806, false, 3, \'Matrix bandwidth\', 20.5616, \'%5.1f\', 1, \'Disk\', \'1 Bytes\')', true, true)
				ProfileItem('Field Recovery', 10, 0, 10, 0, 2799068, 'I(2, 2, \'Excitations\', 4, false, 1, \'Disk\', \'2.71 MB\')', true, true)
				ProfileItem('Data Transfer', 0, 0, 0, 0, 77576, 'I(1, 0, \'Adaptive Pass 20\')', true, true)
				ProfileItem('', 0, 0, 0, 0, 0, 'I(1, 3, \'Max Mag. Delta S\', 0.0359414, \'%.5f\')', false, true)
			$end 'ProfileGroup'
			ProfileFootnote('I(1, 0, \'Adaptive Passes did not converge\')', 1)
		$end 'ProfileGroup'
		$begin 'ProfileGroup'
			MajorVer=2024
			MinorVer=1
			Name='Frequency Sweep'
			$begin 'StartInfo'
				I(1, 'Time', '10/08/2025 20:20:30')
			$end 'StartInfo'
			$begin 'TotalInfo'
				I(1, 'Elapsed Time', '00:03:23')
			$end 'TotalInfo'
			GroupOptions=4
			TaskDataOptions('CPU Time'=8, Memory=8, 'Real Time'=8)
			ProfileItem('', 0, 0, 0, 0, 0, 'I(1, 1, \'HPC\', \'Disabled\')', false, true)
			ProfileItem('', 0, 0, 0, 0, 0, 'I(1, 0, \'\')', false, true)
			ProfileItem('Solution Sweep', 0, 0, 0, 0, 0, 'I(1, 0, \'Fast Sweep\')', false, true)
			ProfileItem('', 0, 0, 0, 0, 0, 'I(1, 0, \'From 1.55 GHz to 1.6 GHz, 10000 Steps\')', false, true)
			ProfileItem('Simulation Setup', 2, 0, 2, 0, 422208, 'I(1, 1, \'Disk\', \'0 Bytes\')', true, true)
			ProfileItem('Matrix Assembly', 15, 0, 15, 0, 1233572, 'I(6, 2, \'Tetrahedra\', 80828, false, 2, \'1 Triangles\', 98, false, 2, \'2 Triangles\', 100, false, 2, \'3 Triangles\', 103, false, 2, \'4 Triangles\', 100, false, 1, \'Disk\', \'0 Bytes\')', true, true)
			ProfileItem('Matrix Solve', 178, 0, 177, 0, 3369104, 'I(6, 1, \'Type\', \'DCS\', 2, \'Cores\', 1, false, 2, \'Matrix size\', 568806, false, 3, \'Matrix bandwidth\', 20.5616, \'%5.1f\', 2, \'Reduced matrix size\', 20, false, 1, \'Disk\', \'174 MB\')', true, true)
			ProfileItem('Field Recovery', 3, 0, 3, 0, 3369104, 'I(2, 2, \'Excitations\', 4, false, 1, \'Disk\', \'76.5 MB\')', true, true)
		$end 'ProfileGroup'
		ProfileItem('', 0, 0, 0, 0, 0, 'I(1, 0, \'\')', false, true)
		$begin 'ProfileGroup'
			MajorVer=2024
			MinorVer=1
			Name='Simulation Summary'
			$begin 'StartInfo'
			$end 'StartInfo'
			$begin 'TotalInfo'
				I(0, ' ')
			$end 'TotalInfo'
			GroupOptions=0
			TaskDataOptions('CPU Time'=8, Memory=8, 'Real Time'=8)
			ProfileItem('Design Validation', 0, 0, 0, 0, 0, 'I(2, 1, \'Elapsed Time\', \'00:00:00\', 1, \'Total Memory\', \'72.8 MB\')', false, true)
			ProfileItem('Initial Meshing', 0, 0, 0, 0, 0, 'I(2, 1, \'Elapsed Time\', \'00:00:45\', 1, \'Total Memory\', \'406 MB\')', false, true)
			ProfileItem('Adaptive Meshing', 0, 0, 0, 0, 0, 'I(5, 1, \'Elapsed Time\', \'00:14:01\', 1, \'Average memory/process\', \'2.67 GB\', 1, \'Max memory/process\', \'2.67 GB\', 2, \'Max number of processes/frequency\', 1, false, 2, \'Total number of cores\', 1, false)', false, true)
			ProfileItem('Frequency Sweep', 0, 0, 0, 0, 0, 'I(2, 1, \'Elapsed Time\', \'00:03:23\', 1, \'Total Memory\', \'3.21 GB\')', false, true)
			ProfileFootnote('I(3, 2, \'Max solved tets\', 80828, false, 2, \'Max matrix size\', 568806, false, 1, \'Matrix bandwidth\', \'20.6\')', 0)
		$end 'ProfileGroup'
		ProfileFootnote('I(2, 1, \'Stop Time\', \'10/08/2025 20:23:53\', 1, \'Status\', \'Normal Completion\')', 0)
	$end 'ProfileGroup'
$end 'Profile'

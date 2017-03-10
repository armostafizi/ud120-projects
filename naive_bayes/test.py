with open('features_train.txt', 'rb') as f:
	reader = f.readlines()
	for line in reader:
		nums = line.split()
		nums = [float(x) for x in nums]
		if max(nums) != 0:
			print max(nums)



import hashlib

test = "ecsc"
while test != "c89aa2ffb9edcc6604005196b5f0e0e4":
	hash = hashlib.md5()
	hash.update(test.encode("utf-8"))
	test = hash.hexdigest()
	print(test)

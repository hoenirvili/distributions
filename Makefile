install:
	sudo python -m pip install -r requirements.txt
	sudo python setup.py install --record files.txt

remove:
	# inspect files.txt to make sure it looks ok. Then:
	tr '\n' '\0' < files.txt | xargs -0 sudo rm -f --
	rm files.txt

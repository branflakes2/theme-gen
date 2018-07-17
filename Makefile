theme-gen: test.py
	pyinstaller --onefile test.py --name theme-gen

install: dist/theme-gen
	cp dist/theme-gen /usr/bin

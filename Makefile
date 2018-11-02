theme-gen: test.py
	pyinstaller --onefile test.py --name theme-gen

install: dist/theme-gen
	cp dist/theme-gen /usr/bin/.
	mkdir -p ~/.config/theme-gen/themes
	cp -r themes ~/.config/theme-gen/.
	cp config ~/.config/theme-gen/.

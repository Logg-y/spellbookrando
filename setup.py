import os
import shutil
import time
import zipfile

if __name__ == "__main__":

	if os.path.isdir("build"):
		shutil.rmtree("build")
	if os.path.isdir("dist"):
		shutil.rmtree("dist")
	if os.path.isdir("spellbookrando"):
		shutil.rmtree("spellbookrando")
	os.system("pyinstaller spellbookrando.py --onefile")
	# ugly for permissions
	time.sleep(4)
	os.rename("dist", "spellbookrando")
	shutil.copy("LICENSE", "spellbookrando/LICENSE")
	shutil.copy("readme.txt", "spellbookrando/readme.txt")
	shutil.copy("spells.csv", "spellbookrando/spells.csv")

	zipf = zipfile.ZipFile("spellbookrando.zip", "w", zipfile.ZIP_DEFLATED)
	for root, dirs, files in os.walk("spellbookrando"):
		for file in files:
			zipf.write(os.path.join(root, file))
			
	zipf.close()
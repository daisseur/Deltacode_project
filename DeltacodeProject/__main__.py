# __main__.py

import sys
from DeltacodeProject.DeltacodeProject import main
from DeltacodeProject import main as ui

def main():
	"""Encode & Decode"""
	
	if len(sys.argv) > 1 and ".ui" not in sys.argv:
		print("A venir...")
	elif ".ui" in sys.argv:
		ui().run()
	else:
		main().run()
if __name__ == "__main__":
	main()

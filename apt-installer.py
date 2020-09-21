import os
import yaml
from pathlib import Path

cwd = os.getcwd()
dir_path = os.path.dirname(os.path.realpath(__file__))

# - Apt

def install_apts(aptdir):
	print("Installing apt packages")
	apt = os.listdir(aptdir)
	for packyaml in apt:
		if (packyaml.startswith("_")):
			continue
		with open(aptdir / Path(packyaml), 'r') as stream:
			apt = yaml.safe_load(stream)
			label = apt['label'] if 'label' in apt else f"NO LABEL ({packyaml})"

			print(f"- Installing {label}")

			if 'ckey' in apt:
				print("- - Download and add Repo key")
				if isinstance(apt['ckey'], list):
					print(f"curl -fsSL {apt['ckey'][0]} | sudo tee {apt['ckey'][1]} > /dev/null")
					os.system(f"curl -fsSL {apt['ckey'][0]} | sudo tee {apt['ckey'][1]} > /dev/null")
				else:
					print(f"curl -fsSL {apt['ckey']} | sudo apt-key add - > /dev/null")
					os.system(f"curl -fsSL {apt['ckey']} | sudo apt-key add - > /dev/null")

			if 'key' in apt:
				print("- - Add Repo key")
				if ('keyserver' in apt):
					os.system(f"sudo apt-key adv --keyserver {apt['keyserver']}--recv-key {apt['key']}")
				else:
					os.system(f"sudo {apt['key']} | sudo apt-key add - > /dev/null")

			if 'repo' in apt:
				print("- - Add Repo")
				if 'ckey' in apt and isinstance(apt['ckey'], list):
					os.system(f"sudo add-apt-repository \"[signed-by={apt['ckey'][1]}] {apt['repo']}\" -y > /dev/null")
				else:
					os.system(f"sudo add-apt-repository \"{apt['repo']}\" -y > /dev/null")

			print("- - Apt update")
			os.system("sudo apt update > /dev/null")

			for package in apt['packages']:
				print(f"- - Installing {package}")
				os.system(f"sudo apt install {package} -y > /dev/null")

			print(f"- Done ({label})")


install(dir_path / "common")
install(Path(sys.argv[1]))


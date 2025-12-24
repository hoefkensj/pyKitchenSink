#!/usr/bin/env python

from pathlib import Path
import sys
import os
from subprocess import Popen,PIPE,STDOUT
from subprocess import getoutput
from shlex import split
from Clict import Clitct
def getPath():
	if len(sys.argv) >1:
		arg=sys.argv[1]
	else:
		arg='/home/hoefkens/Development/Code/Python/Projects'
	path=Path(arg).expanduser().resolve().absolute()
	return path


def exclude(p):
	result=False
	if len([part for part in  [*p.parts] if not part.startswith('.') ]) > 0:
		result= True
	elif p.name=='__init__.py':
		result= True
	elif '__pycache__' in  [*p.parts]:
		result = True
	return False



def getproj(root):
	return [p.parent for p in root.rglob('.venv')]


def main():
	p=getPath()
	projects=getproj(p)
	for project in projects:
		ENV=Clict
		os.chdir(project)
		venv=Path(project,'.venv')
		pyenvfile=Path(venv,'bin/activate_this.py')
		shenvfile=Path(venv,'bin/activate')
		exec(open(pyenvfile).read(), {'__file__': pyenvfile})
		pyscripts=[py.relative_to(p) for py in [*p.rglob('*.py')] if not exclude(p)]
		cmd='python {file}'
		for file in pyscripts:
			print(file)
			ex=Popen(split(cmd.format(file=file)),shell=True,stdout=PIPE,stdin=PIPE)

			print(ex.stdout)
			print('---\n\n')


if __name__ == '__main__':
	main()
import sys
import subprocess
import os

def run_script(script_path):

	exec(open(pyenvfile).read(), {'__file__': pyenvfile})

	# Get the Python interpreter path from the virtual environment
	python_interpreter = os.path.join(venv_path, "bin", "python")

	# Run the script using subprocess
	try:
		result = subprocess.run([python_interpreter, script_path], capture_output=True, text=True)
	except Exception as e:
		print(f"Error running script: {e}")
		return

	# Print output and exit status
	print("Output:")
	print(result.stdout)
	print("Error:")
	print(result.stderr)
	print("Exit Status:", result.returncode)

if __name__ == "__main__":
	if len(sys.argv) != 2:
		print("Usage: python runner.py <script_path>")
		sys.exit(1)

	script_path = sys.argv[1]
	run_script(script_path)

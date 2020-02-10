*******************************************************************************
*
*						            PC-AUDIT
*
*******************************************************************************

CREATED: 2020-02-09
LAST MODIFIED: 2019-11-30
AUTHOR: Brian Metzger (metzgerb@oregonstate.edu)



PROJECT DESCRIPTION: This program collects info about the system hardware, 
operating system, and installed software. The project is written in Python 3 
and was developed in Python 3.7 on Windows.



REQUIREMENTS:
	-Python 3 must be installed
	-virtualenv and psutil must be installed



SETUP INSTRUCTIONS:
	1. Install Python 3.
	
	2. Create Virtual Environment:
		a. [POSIX] python3 -m venv ./venv
		   [WINDOWS] python -m venv .\venv
						OR
		   [WINDOWS] python3 -m venv .\venv
	
	3. Activate virtual environment and install dependencies:
		a. [POSIX] source ./venv/bin/activate
		   [WINDOWS] .\venv\Scripts\activate.bat
		b. pip3 install -r requirements.txt
	
	4. [POSIX ONLY] add executable permissions to pcaudit.py:
		a. chmod +x ./pcaudit.py
	
	5. With active virtual environment, run pcaudit.py with the appropriate
		commands (see USAGE INSTRUCTIONS below)
		a. [POSIX] ./pcaudit.py
						OR
		   [WINDOWS] python3 .\pcaudit.py
		
		NOTE:[POSIX] The shebang at the top of pcaudit.py points to the created 
			  virtual environment. To override, specify the path/interpreter 
			  before pcaudit.py.



CLEANUP INSTRUCTIONS:
	1. Deactivate and delete virtual environment directory:
		a. deactivate
		b. [POSIX] rm -rf ./venv
		   [WINDOWS] del .\venv ('Y' to confirm)
	
	3. [POSIX ONLY] remove executable permissions from pcaudit.py
		a. chmod -x ./pcaudit.py
		
	4. Remove the source files if desired


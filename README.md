# pyshot-example
Example project for the plugin pyshot with an automation of the duck.com website

### Installation guide

```
# Close the repository
git clone https://github.com/anggelomos/pyshot-example.git

# Create and activate virtual environment (optional)
python -m venv pyshot-example

# Activate virtual environment (optional)
source pyshot-example/bin/activate   # MacOS
pyshot-example/Scripts/activate.bat  # Windows CMD
pyshot-example/Scripts/activate.ps1  # Windows Powershell

# Move to the folder and install requirements
cd pyshot-example
pip install -r requirements.txt
```

### Run test
Once the requirements are installed, you can run the test using the following command:
```
python -m pytest test_duckduck.py --pyshot_conf="pyshot.conf"
```
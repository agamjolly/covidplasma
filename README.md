# COVID-19 Plasma Dashboard

India's largest public COVID-19 plasma donors dashboard.

## Setup

To run the file on your local machine, you need to activate the virtual environment `venv` contained in the directory.

To activate the virtual environment, you need to ensure that you have the `virtualenv` package installed globally. To double check, try running 
```bash
pip3 install virtualenv
```

To activate the virtual, `cd` into the directory and run 
```bash
. venv/bin/activate
```

This would activate the virtual environment. You should see `(venv)` besides your directory in the terminal.

## Installation Requirements

The requirements for the app are contained in the `requirements.txt` file. You could install each package individually using `pip3 install <package-name>` or automatically install all dependencies using
```bash 
pip3 install -r requirements.txt
```

## Running

You can run the app using 
```bash
python3 app.py
```

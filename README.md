# COVID-19 Plasma Dashboard

India's first open dashboard that uses crowdsourced data to connect COVID-19 patients to recovered donors for plasma therapy. 

## API

The API only facilitates `POST` requests in the form of a JSON. {{content work needed here}}

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

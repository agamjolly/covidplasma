# COVID-19 Plasma Dashboard

World's first open dashboard that uses crowdsourced data to connect COVID-19 patients to recovered donors for plasma therapy. 

## API

The API only facilitates `POST` requests in the form of a JSON. If you want to have a look at the data being used by the backend in the form of JSON, you could simply make a `POST` request to the endpoint `https://www.covidplasma.in/api/v1/` using the standard public key issued to you. 

If you don't have a key yet and want to explore the API, please contact the administrator.

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

You could also run the file by mounting a Docker image using the `Dockerfile` included in the source. Then run 
```bash 
docker build -t covidplasma .
```

To deploy, run
```bash
docker run -p 80:80 covidplasma
```

## Contribution and Questions

Pull requests are welcome. For any further questions, feel free to reach out to me at me@agamjolly.com. Thank you!

<h6> Contributors &mdash; Agam Jolly, Agrim Gupta, Harsh Arora, Gunangad Pal Singh Narula, Maanav Khaitan, Siddhant Satapathy, Kushagra Wadhwa. 

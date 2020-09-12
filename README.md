## Overview

This repo provides the boiler plate required to setup the API for the takehome BONUS section. 

This repo assumes: 
- Familiarity with Python
- Understanding of basic HTTP request semantics
- Installed Conda as a package manager

## Getting Started

**1. Create your Conda Environment**
`conda create -n <env_name> python=3.8`

**2. Install the required dependencies**
`conda install -n <env_name> requirements.txt`

**3. Run the local flask Development Server**
```
export FLASK_APP=app.py
export FLASK_ENV=development
flask run
```

**4. Hit the endpoint from your local browser**
Enter `http://127.0.0.1:5000/address/exposure/direct` into your browser!

You should see the following response:
```
{
  "data": [
      {
        "address": "", 
        "inflows": "", 
        "outflows": "", 
        "total_flows": ""
      }
  ], 
  "success": true
}
```

## Additional Details

Depending on your data store, you may have to install one or more packages
to connect via Python. I have listed the most common packages below:
- RedShift/Postgres: [Psycopg2](https://pypi.org/project/psycopg2/)
- MySQL: [mysqlclient](https://pypi.python.org/pypi/mysqlclient)
- BigQuery: [google-cloud-bigquery](https://pypi.org/project/google-cloud-bigquery/)




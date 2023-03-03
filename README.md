# - Path to automation

**Current State -** 

Genoa is keeping track (manually) of bill reports that get sent out to patients and providers from every pharmacy. Every month we send a few files to a printing company for them to print/distribute our bills for us.  The process is highly complicated and contains many exceptions so what has happend is IT basically owns the process and micro manages it. Currently any update/change is sent via email to IT for manual data entry. 

**Future state -**

Create some sort of a CRUD interactive tool using python and Node JS.  This would allow the Venders/billing team can put their updates etc in and they can see the results live. This would also elimiate the need for manual email exchanges. 


## Installation

Install fastapi along with all other dependencies

```bash
  pip install -r requirements.txt
```

For React JS install (requires node.js)  
```bash
npx create-react-app my-app
cd my-app
npm start
```

## Environment Variables

To run this project, you will need to add the following environment variables to your .env file. These are realted to SQL Server. 

`SERVER`

`DATABASE`


## Run Locally

Clone the project

```bash
  git clone https://github.optum.com/drossano/fast_api-consumer_reports
```

Go to the project directory

```bash
  cd my-project
```

Install dependencies

```bash
  npm install
```

Start the front end server 

```bash
  npm run start
```

Start the backend server 

```bash
  uvicorn main:app --reload
```



## Tech Stack

**Client:** React

**Server:** Python (Fast API)


## Appendix

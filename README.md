
# Installation
- clone/download videobeat repository
### Frontend Part
- Navigate to videobeat directory in main directory with "cd videobeat" (...videdeobeat-main/videobeat>)
- "npm install" 
- "npm install axios"
- "npm run serve" to start the server
### Backend Part
- Navigate to videobeat-backend directory in main directory with "cd videobeat-backend"
- "python -m venv venv" to create virtual enviroment
- ". venv/Scripts/activate" on Windows to activate virtual enviroment(on other OS may differ)
- "pip install Flask"
- "pip install flask_cors"
- "python app.py" to run the server 

Flask Vue application which takes two files csv files on input and return the data as the JSON

Aplication can be usefull for any one who wants to quickly write an algorythm which computes and muteates data(in thi case CSV files, but the program can be adapted to other files), and dont want to waste time on searching information and writing IO logic themself. 

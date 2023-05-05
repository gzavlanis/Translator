# Translate data using ChatGPT

### This application takes data from CSV files, converts them in JSON strings and finally asks from chatGPT to translate these strings.
### After that, the program converts the translations to pandas Dataframes.

#### Please, have in mind that you have to install all the required packages, included inside the requirements.txt file. The most important is 'openai' because gives you the ability to use chatGPT API.

#### To do that, run in terminal, inside the project folder the following: 

Windows:

```
python -m venv venv
cd venv/Scripts
activate.bat
cd ../../
pip install requirements.txt
```

Linux:

```
python3 -m venv venv
cd venv/Scripts
source activate
cd ../../
pip install requirements.txt
```
#### That's it Enjoy!
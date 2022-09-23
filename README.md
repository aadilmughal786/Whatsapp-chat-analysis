# Do these step in order to run this app locally

### create folder
```
mkdir <folder_name>
```
```
cd <folder_name>
```

### create virtual environment
```
python<version> -m venv <virtual-environment-name>
```
```
python3.8 -m venv env
```


### activate environment
```
source env/bin/activate
```

### copy these file in to <folder_name>
* analysisAPI.py
* app.py
* chatToDataframe.py
* stop_words.txt
* requirements.txt

### install requirements
```
pip install -r requirements.txt
```

### Let run the App
```
streamlit run app.py
```
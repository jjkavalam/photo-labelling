# photo-labelling

- Open editor.html to label a photo
- When done, press cleanup button to make the html file ready for export
- Save the file from the browser and share with friends !

Note: 
- The shared file cannot be viewed offline; an internet connection is
required
- NO user data is saved anywhere outside the file; the internet connection is
used to download certain required code libraries only.

# How to run ?

```
python photo-labelling.py <...args>
```

# How it works ?

The svg is placed inline within the HTML template; and then
analyzed for `circle`, `ellipse` with `title` and `desc` (optional)

# How to build an executable ?

```
pip install -r requirements.txt
pyinstaller --add-data="lib/*;lib" --onefile photo-labelling.py

```
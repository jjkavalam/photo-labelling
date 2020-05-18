# photo-labelling

Using an svg editor like inkscape, make an svg file with the photo (embedded) and the parts to be labelled marked with `circle`, `ellipse`; put the label text within the `title` child tag of the cirlce or ellipse.

Next, use the python script provided here to make a shareable photo viewer from it.

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
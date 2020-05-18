import sys
import os

template="""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>%TITLE%</title>
    %LIB_STYLES%
</head>
<body>
<style>
    html, body {
        margin: 0;
        padding: 0;
        width: 100%;
        height: 100%;
        font-family: sans-serif;
    }
    svg {
        opacity: 0;
        transition-property: opacity;
        transition-duration: 100ms;
    }
    svg:focus {
        outline: none;
    }
    h1 {
        text-align: center;
    }
    .heading {
    }
    .container {
        margin-bottom: 4em;
        height: 80vh;
    }
</style>
<div class="heading">
    <h1>%TITLE%</h1>
</div>

<div class="container">
%SVG%

</div>
%LIB_SCRIPTS%
<script>
    function sizeImage() {
        var svg$ = document.querySelector('svg');
        var container$ = document.querySelector(".container");
        svg$.setAttribute("width", container$.clientWidth + 'px');
        svg$.setAttribute("height", container$.clientHeight + 'px');
    }

    window.onresize = sizeImage;
    sizeImage();

    // initialize panzoom
    var pz = panzoom(document.querySelector('svg > g'), {bounds: true, boundsPadding: 0.5, minZoom: 0.5, maxZoom: 10.0, onTouch: () => false});

    // svg
    var svg = SVG('svg');
    var annotations = svg.find('circle,ellipse');

    // reset stroke and fill
    annotations.css({stroke: 'none', fill: 'white', opacity: 0.1});

    annotations.forEach(function(el) {
        var titleEl = el.findOne('title');
        if (titleEl) {
            var title = titleEl.node.innerHTML;
            // remove title so that there is no default tootlip
            titleEl.remove();
            el.click(function() {
                Snackbar.show({
                    text: title,
                    pos: 'bottom-center'
                });
            });
        }
    });


    // now show the image
    document.querySelector('svg').style.opacity = 1.0;
</script>

</body>
</html>
"""

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def putWithinTags(fileList, tagName):
    out = ""
    for fileName in fileList:
        with open(resource_path(fileName), encoding="utf8") as f:
            contents = f.read()
            out += "<%s>"%(tagName) + contents + "</%s>"%(tagName)
    return out

def makeHtml(svgFile, title):
    with open(svgFile, encoding="utf8") as f:
        svgContents = f.read()
        r = template.replace("%TITLE%", title)
        r = r.replace("%SVG%", svgContents)
        r = r.replace("%LIB_STYLES%", putWithinTags(["lib/snackbar.min.css"], "style"))
        r = r.replace("%LIB_SCRIPTS%", putWithinTags(["lib/svg.min.js","lib/panzoom.min.js","lib/snackbar.min.js"], "script"))
        return r

if len(sys.argv) != 4:
    usage = """Usage:
    %s <path to svg file> <title> <path to html output>
    """%(sys.argv[0])
    print(usage)
else:
    svgFile = sys.argv[1]
    title = sys.argv[2]
    outFile = sys.argv[3]

    with open(outFile, "w", encoding="utf8") as f:
        f.write(makeHtml(svgFile, title))

    print("Done. Wrote html to file %s."%(outFile))


import sys
template="""<!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>%TITLE%</title>
                <link rel="stylesheet" href="https://unpkg.com/tippy.js@6/animations/scale.css" />
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
                svg *:focus {
                    outline: none;
                }
                h1 {
                    text-align: center;
                }
                .heading {
                    height: 15vh;
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

            <script src='https://unpkg.com/panzoom@8.7.3/dist/panzoom.min.js'></script>
            <script src="https://cdn.jsdelivr.net/npm/@svgdotjs/svg.js@latest/dist/svg.min.js"></script>
            <script src="https://unpkg.com/@popperjs/core@2"></script>
            <script src="https://unpkg.com/tippy.js@6"></script>
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
                var pz = panzoom(document.querySelector('svg > g'), {bounds: true});

                // svg
                var svg = SVG('svg');
                var annotations = svg.find('circle,ellipse');

                // reset stroke and fill
                annotations.css({stroke: 'none', fill: 'white', opacity: 0.1});

                // setup data- attribute so that tippy can pick them up
                annotations.forEach(function(el) {
                    var titleEl = el.findOne('title');
                    if (titleEl) {
                        var title = titleEl.node.innerHTML;
                        el.data('tippy-content', title);
                        // remove title so that there is no default tootlip
                        titleEl.remove();
                    }
                });

                // initialize tippy
                tippy('[data-tippy-content]', { animation: 'scale'});


                // now show the image
                document.querySelector('svg').style.opacity = 1.0;
            </script>
            </body>
            </html>
"""

def makeHtml(svgFile, title):
    with open(svgFile) as f:
        svgContents = f.read()
        r = template.replace("%TITLE%", title)
        r = r.replace("%SVG%", svgContents)
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

    with open(outFile, "w") as f:
        f.write(makeHtml(svgFile, title))

    print("Done. Wrote html to file %s."%(outFile))


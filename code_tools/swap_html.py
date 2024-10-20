"""
This file will serve as the last step in the make.bat file for 
a sphinx developed page.

Here I will detail a set of commands available to the system
and deploy replacements to quickly utilize CloudFlare Streams in
place of high storage media.

Commands Available:
    !!insert objectName:
        The tool will search the given HTML for <p>!!insert objectName</p> and 
        replace that portion of the HTML file with the pre-determined HTML product.
"""
commands = {
    "!!insert objectName!!" : "Replaces the HTML Line at that position with the object from the configuration file."
}
import argparse
import json

Parser = argparse.ArgumentParser(
    prog="SPHINX HTML Replacer",
    description="Uses the input files and a pre-configured set of html inserts to "
                "replace <p>!!myCommand</p> with the appropriate stream html"
)

Parser.add_argument('filepath',
                    help='The HTML file to be affected')
Parser.add_argument('-c','--config',
                    help="The JSON file containing the key-value pairs of replaceable objectNames",
                    default="html_config.json")
Parser.add_argument('-m','--mode',
                    default='display',
                    choices=('display','perform'))

args = Parser.parse_args()

print(args.config)

with open(args.config,'r') as fid:
    config = json.load(fid)
with open(args.filepath,'r') as fid:
    html = fid.readlines()

idx_to_replace = [i for i, line in enumerate(html) if "!!" in line]
for idx in idx_to_replace:
    command, objectName = html[idx].split("!!")[1].split(" ")
    print(command, objectName)
    replace = config.get(objectName,False)
    if replace:
        print(html[idx])
        html[idx] = replace
        print(html[idx])
if args.mode == "perform":
    html = "\n".join(html)
    with open(args.filepath,'w') as fid:
        fid.write(html)


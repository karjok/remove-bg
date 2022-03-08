# The CLI for remove-bg
# Rahman Hakim <rahmanhakim2435@protonmail.com>

import argparse
import json

from removebg import *

# Argument Parser
parser = argparse.ArgumentParser(description='Remove-Bg')
parser.add_argument('--input', '-i', type=str, action="store", help="Specify the input image file", required=True)
parser.add_argument('--dir', type=str, help='Specify the output directory')
parser.add_argument('--output', '-o', type=str, help='Specify the output filename')
parser.add_argument('--download', '-d', help="Download the processed file", action='store_true')

args = parser.parse_args()

filename = None
output_dir = None

# Using the backend
remove = removeBg(args.input)

# If download is specified
if args.download:
    # If output filename is specified
    if args.output:
        filename = args.output

    # If output directory is specified
    if args.dir:
        output_dir = args.dir
    
    try:
        # Getting the result URL
        response = remove.get("result")["url"]
        print("Downloading...")
        # Download
        download(response, output_dir, filename)
        print("Download successful")
    except Exception as e:
        print("There's a problem when downloading: ", e)

else:
    print(remove)




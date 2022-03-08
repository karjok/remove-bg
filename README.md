![remove.bg logo](https://static.remove.bg/remove-bg-web/726c8211ef4fdb5ce44accdf843f9bab4d2a356a/assets/logo-nav-9c62b7e3f4c43480bcd12867907e1fb4525f57535be412bbd59fd4c6466bfd40.svg)
# Remove-Bg
A simple python (scraper) tool for remove background on image

> This tool is scraper tool for https://www.remove.bg

### Required module
* requests
* bs4

> pip install requests
> pip install bs4

### Function
Remove-Bg has only one function named `'removeBg'`
with required paramenter `'file_source'`

and one optional paramenter `'delay'` with default value is 1

### Usage
In the remove-bg directory, you can import it as a module or use it directly and give you result as `json`
#### - As module
Example:
```
from removebg import removeBg

image_file = "https://i.redd.it/oxjnv3nybnx71.jpg"
result = removeBg(image_file)
print(result)
```
Output:
```
$ {'original': {'url': 'https://o.remove.bg/uploads/8fc6f083-ebd6-495a-b363-a629c0a5ab32/oxjnv3nybnx71.jpg'}, 'result': {'url': 'https://o.remove.bg/downloads/8fc6f083-ebd6-495a-b363-a629c0a5ab32/oxjnv3nybnx71-removebg-preview.png', 'width': 472, 'height': 529, 'rated': False, 'filename': 'oxjnv3nybnx71-removebg-preview.png', 'foreground_type': 'person'}, 'full': {'width': 680, 'height': 763, 'url': '/images/8fc6f083-ebd6-495a-b363-a629c0a5ab32/full_image'}}
```

#### - Use directly

`$ python removebg.py`

Output:
```
$ input image file source: https://i.redd.it/oxjnv3nybnx71.jpg
{'original': {'url': 'https://o.remove.bg/uploads/8fc6f083-ebd6-495a-b363-a629c0a5ab32/oxjnv3nybnx71.jpg'}, 'result': {'url': 'https://o.remove.bg/downloads/8fc6f083-ebd6-495a-b363-a629c0a5ab32/oxjnv3nybnx71-removebg-preview.png', 'width': 472, 'height': 529, 'rated': False, 'filename': 'oxjnv3nybnx71-removebg-preview.png', 'foreground_type': 'person'}, 'full': {'width': 680, 'height': 763, 'url': '/images/8fc6f083-ebd6-495a-b363-a629c0a5ab32/full_image'}}
```

#### - With CLI

`$ python cli.py -h`

The usage:

```
usage: cli.py [-h] --input INPUT [--dir DIR] [--output OUTPUT] [--download]

Remove-Bg

options:
  -h, --help            show this help message and exit
  --input INPUT, -i INPUT
                        Specify the input image file
  --dir DIR             Specify the output directory
  --output OUTPUT, -o OUTPUT
                        Specify the output filename
  --download, -d        Download the processed file
```

Example usage:

`python cli.py --input myfile.jpg --dir Pictures --output mytransparentfile.png --download`

The command above will send your input image and download the result to `Pictures` directory, with a new name `mytransparentfile.png`

### Image result
From this

<img alt="chad image" src="https://i.redd.it/oxjnv3nybnx71.jpg" width="250">

To this

<img alt="chad image" src="https://o.remove.bg/downloads/8fc6f083-ebd6-495a-b363-a629c0a5ab32/oxjnv3nybnx71-removebg-preview.png" width="250">


As a suggestion, use an online host like flask in heroku to avoid captcha blocking although that will still happen.


Please contribute so that this scraper can be better

I hope it's useful for you

Thanks

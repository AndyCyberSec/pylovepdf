# pylovepdf 1.3.3

ilovepdf.com python API library

## What it does

This library allow to manipulate pdf using the API of http://www.ilovepdf.com. See the Tools section to know what you can do.

### Prerequisites

* [developer account] (https://developer.ilovepdf.com) to get a public key to use the API.
* [Python 3.x.x]
* [Requests] (http://it.python-requests.org/it/latest/)

## Installation (older version)

```
pip install pylovepdf 
```

## Manual installation (up to date) 

Download the latest release.
```
python setup.py install
```

## Getting started

Example files are located inside samples/.
Change file paths and the public_key parameter with the one you found in your developer account (See prerequisites).
Run the files and enjoy.

## Tools
Currently the following tools are available:

* compress          (Reduce the size of pdf files)
* imagepdf          (Converts an image to pdf)
* merge             (Merge multiple pdf into single file)
* officepdf         (Office document to pdf conversion)
* pagenumber        (Place numbers on pages)
* pdfa              (Converts into PDF/A)
* pdfjpg            (Converts a pdf into jpeg image)
* protect           (Add password to a pdf)
* rotate            (Rotates the pages of a file)
* split             (Split a pdf)
* unlock            (Remove the password security from the pdf, the coolest feature ever!)
* validatepdfa      (Checks the conformity of PDF/A format)
* watermark         (Adds watermark to the file)

## Example Usage (compress tool)
```python
from pylovepdf.ilovepdf import ILovePdf

ilovepdf = ILovePdf('public_key', verify_ssl=True)
task = ilovepdf.new_task('compress')
task.add_file('pdf_file')
task.set_output_folder('output_directory')
task.execute()
task.download()
task.delete_current_task()
```

## Alternative Example Usage (compress tool)
A tool can be created directly:
```python
from pylovepdf.tools.compress import Compress

t = Compress('public_key', verify_ssl=True)
t.add_file('pdf_file')
t.set_output_folder('output_directory')
t.execute()
t.download()
t.delete_current_task()
```
## Documentation

Please see https://developer.ilovepdf.com/docs for up-to-date documentation.

## Built With

* [pyCharm](https://www.jetbrains.com/pycharm/) - python IDE

## Versioning

I use [SemVer](http://semver.org/) for versioning.

## Authors

* **Andrea Bruschi** - *Initial work* - [AndyCyberSec](https://github.com/AndyCyberSec)

from pylovepdf.tools.repair import Repair
import urllib

t = Repair('public_key', verify_ssl=True, proxies=urllib.request.getproxies())
# add file
t.add_file('pdf_file')
t.debug = False
t.set_output_folder('output_directory')

t.execute()
t.download()
t.delete_current_task()

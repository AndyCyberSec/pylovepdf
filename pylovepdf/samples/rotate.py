from pylovepdf.tools.rotate import Rotate

t = Rotate('public_key', verify_ssl=True)
t.add_file('pdf_file')
t.file.rotate = 90
t.debug = False
t.set_output_folder('output_directory')

t.execute()
t.download()
t.delete_current_task()

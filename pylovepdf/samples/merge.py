from pylovepdf.tools.merge import Merge

t = Merge('public_key', verify_ssl=True)
# two files needed
t.add_file('pdf_file')
t.add_file('pdf_file')
t.debug = False
t.set_output_folder('output_directory')

t.execute()
t.download()
t.delete_current_task()

from pylovepdf.tools.compress import Compress

t = Compress('public_key', verify_ssl=True)
t.add_file('pdf_file')
t.debug = False
t.compression_level = 'low'
t.set_output_folder('output_directory')

t.execute()
t.download()
t.delete_current_task()

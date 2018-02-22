from pylovepdf.tools.split import Split

t = Split('public_key', verify_ssl=True)
t.add_file('pdf_file')
t.debug = False
t.split_mode = 'fixed_range'
t.fixed_range = '4'
t.set_output_folder('output_directory')

t.execute()
t.download()
t.delete_current_task()

from pylovepdf.tools.protect import Protect

t = Protect('public_key', verify_ssl=True)
t.add_file('pdf_file')
t.debug = False

# file_encryption key to be tested
t.file_encryption_key = 'ciao'

t.file.password = 'test'
t.set_output_folder('output_directory')

t.execute()
t.download()
t.delete_current_task()

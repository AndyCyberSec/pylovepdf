from pylovepdf.tools.pdfa import ToPdfA

t = ToPdfA('public_key', verify_ssl=True)
t.add_file('pdf_file')
t.debug = False
t.set_output_folder('output_directory')

t.execute()
t.download()
t.delete_current_task()

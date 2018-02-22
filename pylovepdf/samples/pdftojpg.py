from pylovepdf.tools.pdftojpg import PdfToJpg

t = PdfToJpg('public_key', verify_ssl=True)
t.add_file('pdf_file')
t.debug = False
t.pdfjpg_mode = 'pages'
t.set_output_folder('output_directory')

t.execute()
t.download()
t.delete_current_task()

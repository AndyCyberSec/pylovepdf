from pylovepdf.tools.imagetopdf import ImageToPdf

t = ImageToPdf('public_key', verify_ssl=True)
t.add_file('pdf_file')
t.debug = False
t.orientation = 'portrait'
t.margin = 0
t.pagesize = 'fit'
t.set_output_folder('output_directory')

t.execute()
t.download()
t.delete_current_task()

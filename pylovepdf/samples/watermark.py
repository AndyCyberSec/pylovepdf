from pylovepdf.tools.watermark import Watermark

t = Watermark('public_key', verify_ssl=True)
t.add_file('pdf_file')
t.debug = False
t.mode = 'text'
t.text = 'hi'
t.file.set_metas('Title', 'Hi, I am a title')
t.set_output_folder('output_directory')

t.execute()
t.download()
t.delete_current_task()

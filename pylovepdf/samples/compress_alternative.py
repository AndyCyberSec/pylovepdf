from pylovepdf.ilovepdf import ILovePdf

ilovepdf = ILovePdf('public_key', verify_ssl=True)
task = ilovepdf.new_task('compress')
task.add_file('pdf_file')
task.debug = False
task.compression_level = 'low'
task.set_output_folder('output_directory')

task.execute()
task.download()
task.delete_current_task()

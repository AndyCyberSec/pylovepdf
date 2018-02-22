from pylovepdf.tools.validatepdfa import ValidatePdfA

t = ValidatePdfA('public_key', verify_ssl=True)
t.add_file('pdf_file')
t.debug = False
t.conformance = 'pdfa-2b'

t.execute()
t.delete_current_task()

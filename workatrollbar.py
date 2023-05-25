import rollbar
# access_token, environment, code_version
rollbar.init('PROD_SERVER_ITEM_TOKEN', 'production', code_version='COMMIT_SHA')  

try:
    #x=1/0 Division By Zero -x-
    #x=2+"2" Add a string and integer -x-
    print("I want to work at Rollbar!" #Syntax Error
except IOError:
    rollbar.report_message('Got an IOError in the main loop', 'warning')
except:
    # catch-all
    rollbar.report_exc_info()
    print("There was an error.")
    # equivalent to rollbar.report_exc_info(sys.exc_info())

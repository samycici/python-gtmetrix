python-gtmetrix
========================

**python-gtmetrix** is a Python client library for GTmetrix REST API created by https://github.com/aisayko/python-gtmetrix
This is a sample project and was updated in January 2016 to address some needs:
 - Read the test urls from a json
 - Write the results in a txt file
 
Run in Python 2.7.10 or higher


Make tests:
-----------

Change sites.json with the desired URLs:
    
    {
    "google": "http://google.com",
    "facebook": "http://facebook.com"
    }
   

Change settings.py with your User and API Key:

    GTMETRIX_REST_API_URL = 'https://gtmetrix.com/api/0.1/test'
    USER = your_user@email.com
    API_KEY= your_api_key

If you don't have a user, create in the site https://gtmetrix.com

Run analysis.py:
    
    python analysis.py
        

When test is completed you able to access the results in two files:

    results-date and resources-date
    
Which date refers to the current system date (dd-mm-yyyy).

Example
    
    results-8-1-2016:
    site:google pagespeed_score:96 yslow_score:98 page_load_time:3435 page_bytes:358863 page_elements:12 
    
    resources-8-1-2016
    site:google screenshot:https://gtmetrix.com/api/0.1/test/StLBexrb/screenshot har:https://gtmetrix.com/api/0.1/test/StLBexrb/har pagespeed_url:https://gtmetrix.com/api/0.1/test/StLBexrb/pagespeed pagespeed_files:https://gtmetrix.com/api/0.1/test/StLBexrb/pagespeed-files yslow_url:https://gtmetrix.com/api/0.1/test/StLBexrb/yslow  report_pdf:https://gtmetrix.com/api/0.1/test/StLBexrb/report-pdf report_pdf_full:https://gtmetrix.com/api/0.1/test/StLBexrb/report-pdf?full=1  


List of available params and response attributes you can find at http://gtmetrix.com/api/


Exceptions:
-----------

Invalid test request

    GTmetrixInvalidTestRequest


The requested test does not exist

    GTmetrixTestNotFound 
    
The maximum number of API calls reached 
    
    GTmetrixMaximumNumberOfApis 
    
Too many concurrent requests from your IP    
    
    GTmetrixManyConcurrentRequests
    

[![Bitdeli Badge](https://d2weczhvl823v0.cloudfront.net/aisayko/python-gtmetrix/trend.png)](https://bitdeli.com/free "Bitdeli Badge")


from django.http import HttpResponse
from django.views.generic.simple import direct_to_template
#uncomment the following two lines and the one below
#if you dont want to use a decorator instead of the middleware
#from django.utils.decorators import decorator_from_middleware
#from facebook.djangofb import FacebookMiddleware

# Import the Django helpers
import facebook.djangofb as facebook

# The User model defined in models.py
from models import User
import logging
# import pdb;

LOG_FILENAME = 'example.log'
logging.basicConfig(filename=LOG_FILENAME,level=logging.DEBUG)

# We'll require login for our canvas page. This
# isn't necessarily a good idea, as we might want
# to let users see the page without granting our app
# access to their info. See the wiki for details on how
# to do this.
#@decorator_from_middleware(FacebookMiddleware)
@facebook.require_oauth()
def canvas(request):
    html = render_to_string(
        'canvas.fbml', 
        { 'fbuser': 'test_user' }, 
        context_instance=RequestContext(request)
    )
    # import pdb; pdb.set_trace()
    logging.info(html)
    return HttpResponse(html)
    # print request
    # return render_to_response(request, 'canvas.fbml', extra_context={'fbuser': 'test_user'})
    # return direct_to_template(request, 'test.html', extra_context={})

@facebook.require_oauth()
def ajax(request):
    return HttpResponse('hello world')

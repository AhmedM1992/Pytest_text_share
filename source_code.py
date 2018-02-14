import requests

MAIN_API_URL = 'http://text-share.com/api/'

def get_paste(pasteid):
    """Get paste
    Args:
         pasteid (string): the id of the paste
    Returns:
         response (json): paste
    """
    get_paste_url = '{}paste/{}'.format(MAIN_API_URL, pasteid)
    response = requests.get(get_paste_url)
    return response.json()


def get_paste_raw_text(pasteid):
    """Get raw text paste
    Args:
         pasteid (string): the id of the paste
    Returns:
         response (string): paste string
    """
    paste = get_paste(pasteid)
    return paste['raw']


def get_random_paste():
    """Get random paste
    Returns:
         response (string): paste string
    """
    paste_url = '{}random/'.format(MAIN_API_URL)
    response = requests.get(paste_url)
    return response.json()


def get_paste_id(paste_url):
    """Get raw text paste
    Args:
         paste_url (string): the url of the paste
    Returns:
         response (string): paste string
    """
    return paste_url[27:]


def get_list_available_languages():
    """Get paste
    Returns:
         response (json): available languages
    """
    paste_url = '{}langs/'.format(MAIN_API_URL)
    response = requests.get(paste_url)
    return response.json()


def create_paste(text, **kwargs):
    """
    text='your paste text'
    The paste content. Required.
    title='title'
    Title for the paste.
    name='name'
    The author's name.
    private=1
    Make paste private.
    lang='language'
    Use get_list_available_languages() method
    expire='minutes'
    Set paste expiration.
    reply='pasteid'
    Reply to existing paste.
    """
    paste_url = '{}create'.format(MAIN_API_URL)
    kwargs['text'] = text
    response = requests.post(paste_url, data=kwargs)
    return response.text.replace('\n','')
    

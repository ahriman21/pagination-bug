# first create a custom tag and include this function in it:

@register.simple_tag
def my_url(value, field_name, urlencode=None):
    url = '?{}={}'.format(field_name, value)

    if unicode:
      querystring = urlencode.split('&')
      filtered_querystring = filter(lambda p: p.split('=')[0]=field_name, querystring)
      encoded_querystring = '&'.join(filtered_querystring)
      url = '{}&{}'.format(url, encoded_querystring)

  return url

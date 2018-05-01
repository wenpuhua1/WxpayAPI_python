# 替换 php 的同名函数,实现一样的功能
import ast
import hashlib
import math
import numbers
import json
import time
import sys
import random

try:
    from io import BytesIO as StringIO  # python3
except ImportError:  # python2
    try:
        from cStringIO import StringIO
    except ImportError:
        from StringIO import StringIO

    StringIO = StringIO.StringIO()

import pycurl

md5 = lambda var: hashlib.md5(var).hexdigest()
strtoupper = lambda var: var.upper()
is_array = lambda var: isinstance(var, (list, tuple))
is_string = lambda var: isinstance(var, str)
strlen = lambda var: len(var)


def array_key_exists(key, dict_arr):
    return key in dict_arr.keys()


def is_numeric(obj):
    if isinstance(obj, numbers.Number):
        return True
    elif is_string(obj):
        nodes = list(ast.walk(ast.parse(obj)))[1:]
        if not isinstance(nodes[0], ast.Expr):
            return False
        if not isinstance(nodes[-1], ast.Num):
            return False
        nodes = nodes[1:-1]
        for i in range(len(nodes)):
            if i % 2 == 0:
                if not isinstance(nodes[i], ast.UnaryOp):
                    return False
            else:
                if not isinstance(nodes[i], (ast.USub, ast.UAdd)):
                    return False
        return True
    else:
        return False


def json_decode(string, assoc, depth, options):
    # 这个php函数可接收多个参数 todo
    return json.loads(string)


def json_encode(string, assoc, depth, options):
    # 这个php函数可接收多个参数 todo
    return json.dumps(string)


def ksort(d):
    return [(k, d[k]) for k in sorted(d.keys())]


def microtime(get_as_float=False):
    if get_as_float:
        return time.time()
    else:
        return '%f %d' % math.modf(time.time())


def mt_rand(low=0, high=sys.maxint):
    """Generate a better random value
    """
    return random.randint(low, high)


def simplexml_load_string(string, classname, options, ns, is_prefix):
    # todo ,基本就是解析 xml
    # 转换形式良好的 XML 字符串为 SimpleXMLElement 对象
    pass


def substr(string, start, length):
    return string[start:start + length]

# todo 下面的实现
CURLOPT_HEADER = ""
CURLOPT_POST = ""
CURLOPT_POSTFIELDS = ""
CURLOPT_PROXY = ""
CURLOPT_PROXYPORT = ""
CURLOPT_RETURNTRANSFER = ""
CURLOPT_SSL_VERIFYPEER = ""
CURLOPT_SSL_VERIFYHOST = ""
CURLOPT_SSLCERTTYPE = ""
CURLOPT_SSLCERT = ""
CURLOPT_SSLKEYTYPE = ""
CURLOPT_SSLKEY = ""
CURLOPT_TIMEOUT = ""
CURLOPT_URL = ""
TRUE = ""


def curl_init(url):
    c = pycurl.Curl()

    # if $url was set
    return c.setopt(c.URL, url)


def curl_setopt(curl, option, value):
    curl.setopt(option, value)


def curl_exec(curl):
    b = StringIO()
    curl.setopt(pycurl.WRITEFUNCTION, b.write)
    curl.perform()
    response = b.getvalue()
    return response

def curl_close(curl):
    return curl.close()

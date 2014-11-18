#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import warnings

try:
    import unicodedata2 as unicodedata
except:
    warnings.warn("Couldn't import unicodedata2, using standard lib fallback")
    import unicodedata

try:
    import unidecode
except:
    warnings.warn("Couldn't import unidecode, ASCII fallbacks not generated")

'''
Because Unicode contains bullshit like this:

🗼🗾🗻🗽📈📆🔪💋📎⌨
📌ॐ☠🔈📱🔊🔬🔥🔦🔫🔭🔱
🔰🔏🔣🔞📡📢📠📟📯📺
📷📹📻📼🎦📋💅💆💃💁👾
👺👸👳👰👬👭⚧⛢⚸⛵⛩
'''

# Try generating code points up to this value, since enumerating the whole
# possible 32bit unicode space would be dumb.
MAX_UNICODE_CHAR = 0xE007F

def main():
    for i in xrange(0, MAX_UNICODE_CHAR):
        s = r'\U' + ('%08X' % i)
        t = eval('u"' + s + '"')
        name = unicodedata.name(t, None)
        fall = unidecode.unidecode(t)
        if name is None: continue
        name = name.encode('utf8')
        print '%08x\t%08d\t%s\t%s\t%s\t%s' % (i, i, s, t, fall, name)

if __name__ == '__main__':
    main()

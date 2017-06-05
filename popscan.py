#!/usr/bin/env python

#
# popscan.py
# https://github.com/vesche
#

import os
import urllib2
import ssl
import sys


BANNER = '''
88d888b. .d8888b. 88d888b. .d8888b. .d8888b. .d8888b. 88d888b.
88'  `88 88'  `88 88'  `88 Y8ooooo. 88'  `"" 88'  `88 88'  `88
88.  .88 88.  .88 88.  .88       88 88.  ... 88.  .88 88    88
88Y888P' `88888P' 88Y888P' `88888P' `88888P' `88888P8 dP    dP
88                88
dP                dP        https://github.com/vesche
'''
HELP_TEXT = '''
{}

Usage:   python popscan.py <url>
Example: python popscan.py http://example.com

Popscan is a web server enumeration utility that requests common web application
URI's in attempt to discover web pages and services. Anything that doesn't
return a 404 is worth looking into further.
'''.format(BANNER)
BAR = '-'*20

# list taken from - https://github.com/pwnwiki/webappurls
URI_LIST = [ '/apims/public/userRequest/initSubmitAccountRequest.pub', '/.bzr/README',
'/.git/config', '/.hg/requires', '/.htaccess', '/.htpasswd',
'/.svn/wc.db', '/?Workshop/valid_page_name_in_current_directory&login',
'/CFIDE/adminapi/administrator.cfc', '/CFIDE/administrator/enter.cfm',
'/CFIDE/administrator/index.cfm', '/CFIDE/scripts/ajax/FCKeditor/editor/filemanager/connectors/cfm/upload.cfm',
'/CHANGELOG.txt', '/INSTALL.txt', '/Providers/HtmlEditorProviders/Fck/fcklinkgallery.aspx', '/README.txt',
'/WorkArea/version.xml', '/_layouts/groups.aspx', '/_layouts/people.aspx', '/access.log', '/admin', '/admin.nsf',
'/administration/index.php', '/administrator/', '/apc.php', '/awstats/', '/axis2/axis2-web/HappyAxis.jsp',
'/backup.tar.gz', '/backup/', '/backups/', '/bb-admin', '/c99.php', '/cacti', '/cgi-bin/cvsweb',
'/cgi-bin/php', '/cgi-bin/php5', '/console/', '/crossdomain.xml', '/data', '/dev/', '/elmah.axd',
'/error.log', '/exchange/', '/files', '/ghost', '/include/', '/includes/', '/index.php?-s',
'/index.php?url=admin', '/info.php', '/install', '/install/upgrade.php', '/jmx-console/',
'/login', '/logon', '/logs/', '/manager', '/manager/html', '/manual/', '/na_admin/ataglance.html',
'/owa', '/pgmyadmin/', '/phpinfo.php', '/phpmyadmin/', '/plesk', '/pls/admin', '/private', '/robots.txt',
'/rockmongo/index.php', '/server-status', '/sitemap.xml', '/sites/default/files/backup_migrate/', '/temp',
'/test.php', '/test/', '/tmp', '/trace.axd', '/upload/', '/uploads/', '/user.php', '/webalizer/', '/webdav/',
'/webmin', '/wp-admin/', '/wsman', '/xampp/' ]


def main(url):
    if not url.startswith('http'):
        print('Error, must specify http:// or https:// in the url.\n')
        sys.exit(1)

    if url.endswith('/'):
        url = url[:-1]

    print(BANNER)

    for u in URI_LIST:
        print u + '\n' + BAR

        try:
            ctx = ssl.create_default_context()
            ctx.check_hostname = False
            ctx.verify_mode = ssl.CERT_NONE
            response = urllib2.urlopen('{}{}'.format(url, u), context=ctx)
            html = response.read()
        except:
            html = '404'

        print(html + '\n' + BAR + '\n')


if __name__ == '__main__':
    try:
        url = sys.argv[1]
    except IndexError:
        print HELP_TEXT
        sys.exit(1)

    main(url)

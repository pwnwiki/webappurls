Web App Defauls URL list
==========

A public list of URLs generally useful to webapp testers and pentesters.

This will start off as a single list but could certainly grow into a much more organized set of lists.

Started here: https://etherpad.mozilla.org/weburl-easywins

```

# meta discussion#suffix directories with a '/'
# '#' is a comment char. I don't know what you'll have to do if you want to use a # in a url (shouldn't need to anyway)

# the list
/.bzr/README
/.git/config
/.hg/requires
/.htaccess
/.htpasswd
/.svn/wc.db
/?Workshop/valid_page_name_in_current_directory&login #CMSimple login panel 
/CFIDE/adminapi/administrator.cfc
/CFIDE/administrator/enter.cfm
/CFIDE/administrator/index.cfm
/CFIDE/scripts/ajax/FCKeditor/editor/filemanager/connectors/cfm/upload.cfm
/CHANGELOG.txt
/INSTALL.txt
/Providers/HtmlEditorProviders/Fck/fcklinkgallery.aspx
/README.txt
/WorkArea/version.xml
/_layouts/groups.aspx
/_layouts/people.aspx
/access.log
/admin
/admin.nsf
/administration/index.php #  (php fusion?)
/administrator/ #  (joomla) (idk if peeps still even use joomla xD)
/apc.php
/awstats/
/axis2/axis2-web/HappyAxis.jsp
/backup.tar.gz
/backup/
/backups/
/bb-admin
/c99.php # and others(r57 pls)
/cacti
/cgi-bin/cvsweb # <- RANCID
/cgi-bin/php # http://www.exploit-db.com/exploits/29290/ CVE-2012-1823
/cgi-bin/php5 # http://www.exploit-db.com/exploits/29290/ CVE-2012-1823
/console/
/crossdomain.xml
/data
/dev/
/elmah.axd
/error.log
/exchange/
/files
/ghost
/include/
/includes/
/index.php?-s
/index.php?url=admin #Tango admin panel when SEF not supported/enabled
/info.php
/install
/install/upgrade.php
/jmx-console/
/login
/logon
/logs/
/manager
/manager/html
/manual/
/na_admin/ataglance.html
/owa
/pgmyadmin/
/phpinfo.php
/phpmyadmin/
/plesk
/pls/admin
/private
/robots.txt
/rockmongo/index.php
/server-status
/sitemap.xml
/sites/default/files/backup_migrate/
/temp
/test.php
/test/
/tmp
/trace.axd
/upload/
/uploads/
/user.php #   (Zikula)
/webalizer/
/webdav/
/webmin
/wp-admin/
/wsman
/xampp/


# other tricks
# Add a ~ to any .php you see.
# Also add # to any .php you see; example wp-config.php# (for all the emacs users that somehow are still alive)
# Add .bak or .old after any .php you see (Or replace .php with them) - may still get preprocessed though. e.g. index.php --> index.php.old, index.bak etc.
# Try .phps for php source, alternate naming convention
#Some places still use test.domain.tld for testing new configurations before deploying, may have different access controls that allow you to see directory listings, etc

```

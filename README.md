puppetboard-rpm
===============

Spec files to build all required packages to install pupeptboard form rpm

This is a first attemp to get all python-packages into an rpm.  Most specs are taken from the epel (6.5) or centos base (6.5) src.rpms, and updated to the 'requirements.txt' form the [puppetboard github page] (https://github.com/nedap/puppetboard).

Only the python-flacs is taken from the fc20 repos.  This spec file has support for both current versions of fedora and RHEL and deriviates.

Building the packaged is best done using a clean centos6.5 vagrant box.  There is a specific order and build requirements.  I still have some conflicting versions  ...

Nexts step are done on a vagrant box as the vagrant user (never build rpms as the root user)
The next steps will not work, because the sources are not available.  As soon as i have thos working properly, I will provide a repo for the rpms ans src.rpms.  In the meantime, you can find the links to the sources in the \*.spec file and put these files in ~/rpmbuild/SOURCES)

* wget http://fedora.cu.be/epel/6/i386/epel-release-6-8.noarch.rpm (or any other mirror)
* sudo yum localinstall epel-release-6-8.noarch.rpm

* yum install rpm-build
* cd rpmbuild/SPECS

copy all spec files in this directory

* rpmbuild -ba python-markupsafe.spec
* sudo yum localinstall ../RPMS/x86_64/python-markupsafe-0.18-1.el6.x86_64.rpm
* sudo yum install python-sphinx10
* rpmbuild -ba python-jinja2-27.spec
* sudo yum localinstall ../RPMS/noarch/python-jinja2-27-2.7-1.el6.noarch.rpm
* sudo yum install python-sphinx
* rpmbuild -ba python-werkzeug.spec
* sudo yum install python-itsdangerous (correct version is in base repo)
* rpmbuild -ba python-wtforms.spec
* sudo localinstall ../RPMS/noarch/python-wtforms-1.0.4-1.el6.noarch.rpm
* rpmbuild -ba python-flask-wtf.spec

the next rpm builds, but the tests fail, because of jini2 version conflict.

* rpmbuild -ba python-flaks.spec

* rpmbuild -ba python-pypuppetdb
* rpmbuild -ba python-puppetdb

In the puppetdb rpm, all dependenccies to other rpm and there specific version are hard Required:.  For a first attemp this can be OK.  This could change in the futere (I dont know if this is good practice)


Example installation session
============================

[root@book ~]# yum install python-puppetboard
Loaded plugins: fastestmirror, security
Loading mirror speeds from cached hostfile
 * base: be.mirror.eurid.eu
 * epel: fedora.cu.be
 * extras: be.mirror.eurid.eu
 * updates: be.mirror.eurid.eu
Setting up Install Process
Resolving Dependencies
--> Running transaction check
---> Package python-puppetboard.noarch 0:0.0.4-1.el6 will be installed
--> Processing Dependency: python-wtforms = 1.0.4 for package: python-puppetboard-0.0.4-1.el6.noarch
--> Processing Dependency: python-werkzeug = 0.9.3 for package: python-puppetboard-0.0.4-1.el6.noarch
--> Processing Dependency: python-requests = 1.2.3 for package: python-puppetboard-0.0.4-1.el6.noarch
--> Processing Dependency: python-pypuppetdb = 0.1.0 for package: python-puppetboard-0.0.4-1.el6.noarch
--> Processing Dependency: python-markupsafe = 0.18 for package: python-puppetboard-0.0.4-1.el6.noarch
--> Processing Dependency: python-jinja2-27 = 2.7 for package: python-puppetboard-0.0.4-1.el6.noarch
--> Processing Dependency: python-itsdangerous = 0.22 for package: python-puppetboard-0.0.4-1.el6.noarch
--> Processing Dependency: python-flask-wtf = 0.8.4 for package: python-puppetboard-0.0.4-1.el6.noarch
--> Processing Dependency: python-flask = 1:0.10.1 for package: python-puppetboard-0.0.4-1.el6.noarch
--> Running transaction check
---> Package python-flask.noarch 1:0.10.1-3.el6 will be installed
---> Package python-flask-wtf.noarch 0:0.8.4-1.el6 will be installed
---> Package python-itsdangerous.noarch 0:0.22-1.el6 will be installed
---> Package python-jinja2-27.noarch 0:2.7-1.el6 will be installed
--> Processing Dependency: python-babel >= 0.8 for package: python-jinja2-27-2.7-1.el6.noarch
---> Package python-markupsafe.x86_64 0:0.18-1.el6 will be installed
---> Package python-pypuppetdb.noarch 0:0.1.0-1.el6 will be installed
---> Package python-requests.noarch 0:1.2.3-4.el6 will be installed
--> Processing Dependency: python-urllib3 for package: python-requests-1.2.3-4.el6.noarch
--> Processing Dependency: python-ordereddict for package: python-requests-1.2.3-4.el6.noarch
--> Processing Dependency: python-chardet for package: python-requests-1.2.3-4.el6.noarch
---> Package python-werkzeug.noarch 0:0.9.3-2.el6 will be installed
---> Package python-wtforms.noarch 0:1.0.4-1.el6 will be installed
--> Running transaction check
---> Package python-babel.noarch 0:0.9.4-5.1.el6 will be installed
---> Package python-chardet.noarch 0:2.0.1-1.el6 will be installed
---> Package python-ordereddict.noarch 0:1.1-2.el6 will be installed
---> Package python-urllib3.noarch 0:1.5-7.el6 will be installed
--> Processing Dependency: python-six for package: python-urllib3-1.5-7.el6.noarch
--> Processing Dependency: python-backports-ssl_match_hostname for package: python-urllib3-1.5-7.el6.noarch
--> Running transaction check
---> Package python-backports-ssl_match_hostname.noarch 0:3.4.0.2-1.el6 will be installed
--> Processing Dependency: python-backports for package: python-backports-ssl_match_hostname-3.4.0.2-1.el6.noarch
---> Package python-six.noarch 0:1.4.1-1.el6 will be installed
--> Running transaction check
---> Package python-backports.x86_64 0:1.0-3.el6 will be installed
--> Finished Dependency Resolution

Dependencies Resolved

====================================================================================================================================================
 Package                                              Arch                    Version                            Repository                    Size
====================================================================================================================================================
Installing:
 python-puppetboard                                   noarch                  0.0.4-1.el6                        puppetboard                   63 k
Installing for dependencies:
 python-babel                                         noarch                  0.9.4-5.1.el6                      base                         1.4 M
 python-backports                                     x86_64                  1.0-3.el6                          epel                         5.3 k
 python-backports-ssl_match_hostname                  noarch                  3.4.0.2-1.el6                      epel                          12 k
 python-chardet                                       noarch                  2.0.1-1.el6                        epel                         225 k
 python-flask                                         noarch                  1:0.10.1-3.el6                     puppetboard                  279 k
 python-flask-wtf                                     noarch                  0.8.4-1.el6                        puppetboard                   47 k
 python-itsdangerous                                  noarch                  0.22-1.el6                         epel                          23 k
 python-jinja2-27                                     noarch                  2.7-1.el6                          puppetboard                  1.0 M
 python-markupsafe                                    x86_64                  0.18-1.el6                         puppetboard                   33 k
 python-ordereddict                                   noarch                  1.1-2.el6                          epel                         7.6 k
 python-pypuppetdb                                    noarch                  0.1.0-1.el6                        puppetboard                   44 k
 python-requests                                      noarch                  1.2.3-4.el6                        puppetboard                   85 k
 python-six                                           noarch                  1.4.1-1.el6                        epel                          22 k
 python-urllib3                                       noarch                  1.5-7.el6                          epel                          41 k
 python-werkzeug                                      noarch                  0.9.3-2.el6                        puppetboard                  797 k
 python-wtforms                                       noarch                  1.0.4-1.el6                        puppetboard                  329 k

Transaction Summary
====================================================================================================================================================
Install      17 Package(s)

Total download size: 4.4 M
Installed size: 17 M
Is this ok [y/N]: y
Downloading Packages:
(1/17): python-babel-0.9.4-5.1.el6.noarch.rpm                                                                                | 1.4 MB     00:00     
(2/17): python-backports-1.0-3.el6.x86_64.rpm                                                                                | 5.3 kB     00:00     
(3/17): python-backports-ssl_match_hostname-3.4.0.2-1.el6.noarch.rpm                                                         |  12 kB     00:00     
(4/17): python-chardet-2.0.1-1.el6.noarch.rpm                                                                                | 225 kB     00:00     
(5/17): python-flask-0.10.1-3.el6.noarch.rpm                                                                                 | 279 kB     00:00     
(6/17): python-flask-wtf-0.8.4-1.el6.noarch.rpm                                                                              |  47 kB     00:00     
(7/17): python-itsdangerous-0.22-1.el6.noarch.rpm                                                                            |  23 kB     00:00     
(8/17): python-jinja2-27-2.7-1.el6.noarch.rpm                                                                                | 1.0 MB     00:00     
(9/17): python-markupsafe-0.18-1.el6.x86_64.rpm                                                                              |  33 kB     00:00     
(10/17): python-ordereddict-1.1-2.el6.noarch.rpm                                                                             | 7.6 kB     00:00     
(11/17): python-puppetboard-0.0.4-1.el6.noarch.rpm                                                                           |  63 kB     00:00     
(12/17): python-pypuppetdb-0.1.0-1.el6.noarch.rpm                                                                            |  44 kB     00:00     
(13/17): python-requests-1.2.3-4.el6.noarch.rpm                                                                              |  85 kB     00:00     
(14/17): python-six-1.4.1-1.el6.noarch.rpm                                                                                   |  22 kB     00:00     
(15/17): python-urllib3-1.5-7.el6.noarch.rpm                                                                                 |  41 kB     00:00     
(16/17): python-werkzeug-0.9.3-2.el6.noarch.rpm                                                                              | 797 kB     00:00     
(17/17): python-wtforms-1.0.4-1.el6.noarch.rpm                                                                               | 329 kB     00:00     
----------------------------------------------------------------------------------------------------------------------------------------------------
Total                                                                                                               424 kB/s | 4.4 MB     00:10     
warning: rpmts_HdrFromFdno: Header V3 RSA/SHA256 Signature, key ID 0608b895: NOKEY
Retrieving key from file:///etc/pki/rpm-gpg/RPM-GPG-KEY-EPEL-6
Importing GPG key 0x0608B895:
 Userid : EPEL (6) <epel@fedoraproject.org>
 Package: epel-release-6-8.noarch (installed)
 From   : /etc/pki/rpm-gpg/RPM-GPG-KEY-EPEL-6
Is this ok [y/N]: y
Running rpm_check_debug
Running Transaction Test
Transaction Test Succeeded
Running Transaction
Warning: RPMDB altered outside of yum.
  Installing : python-ordereddict-1.1-2.el6.noarch                                                                                             1/17 
  Installing : python-werkzeug-0.9.3-2.el6.noarch                                                                                              2/17 
  Installing : python-itsdangerous-0.22-1.el6.noarch                                                                                           3/17 
  Installing : python-markupsafe-0.18-1.el6.x86_64                                                                                             4/17 
  Installing : python-wtforms-1.0.4-1.el6.noarch                                                                                               5/17 
  Installing : python-flask-wtf-0.8.4-1.el6.noarch                                                                                             6/17 
  Installing : python-chardet-2.0.1-1.el6.noarch                                                                                               7/17 
  Installing : python-backports-1.0-3.el6.x86_64                                                                                               8/17 
  Installing : python-backports-ssl_match_hostname-3.4.0.2-1.el6.noarch                                                                        9/17 
  Installing : python-pypuppetdb-0.1.0-1.el6.noarch                                                                                           10/17 
  Installing : python-six-1.4.1-1.el6.noarch                                                                                                  11/17 
  Installing : python-urllib3-1.5-7.el6.noarch                                                                                                12/17 
  Installing : python-requests-1.2.3-4.el6.noarch                                                                                             13/17 
  Installing : python-babel-0.9.4-5.1.el6.noarch                                                                                              14/17 
  Installing : python-jinja2-27-2.7-1.el6.noarch                                                                                              15/17 
  Installing : 1:python-flask-0.10.1-3.el6.noarch                                                                                             16/17 
  Installing : python-puppetboard-0.0.4-1.el6.noarch                                                                                          17/17 
  Verifying  : python-babel-0.9.4-5.1.el6.noarch                                                                                               1/17 
  Verifying  : python-six-1.4.1-1.el6.noarch                                                                                                   2/17 
  Verifying  : python-jinja2-27-2.7-1.el6.noarch                                                                                               3/17 
  Verifying  : python-puppetboard-0.0.4-1.el6.noarch                                                                                           4/17 
  Verifying  : python-requests-1.2.3-4.el6.noarch                                                                                              5/17 
  Verifying  : 1:python-flask-0.10.1-3.el6.noarch                                                                                              6/17 
  Verifying  : python-wtforms-1.0.4-1.el6.noarch                                                                                               7/17 
  Verifying  : python-markupsafe-0.18-1.el6.x86_64                                                                                             8/17 
  Verifying  : python-pypuppetdb-0.1.0-1.el6.noarch                                                                                            9/17 
  Verifying  : python-flask-wtf-0.8.4-1.el6.noarch                                                                                            10/17 
  Verifying  : python-backports-1.0-3.el6.x86_64                                                                                              11/17 
  Verifying  : python-itsdangerous-0.22-1.el6.noarch                                                                                          12/17 
  Verifying  : python-werkzeug-0.9.3-2.el6.noarch                                                                                             13/17 
  Verifying  : python-backports-ssl_match_hostname-3.4.0.2-1.el6.noarch                                                                       14/17 
  Verifying  : python-ordereddict-1.1-2.el6.noarch                                                                                            15/17 
  Verifying  : python-urllib3-1.5-7.el6.noarch                                                                                                16/17 
  Verifying  : python-chardet-2.0.1-1.el6.noarch                                                                                              17/17 

Installed:
  python-puppetboard.noarch 0:0.0.4-1.el6                                                                                                           

Dependency Installed:
  python-babel.noarch 0:0.9.4-5.1.el6        python-backports.x86_64 0:1.0-3.el6       python-backports-ssl_match_hostname.noarch 0:3.4.0.2-1.el6   
  python-chardet.noarch 0:2.0.1-1.el6        python-flask.noarch 1:0.10.1-3.el6        python-flask-wtf.noarch 0:0.8.4-1.el6                        
  python-itsdangerous.noarch 0:0.22-1.el6    python-jinja2-27.noarch 0:2.7-1.el6       python-markupsafe.x86_64 0:0.18-1.el6                        
  python-ordereddict.noarch 0:1.1-2.el6      python-pypuppetdb.noarch 0:0.1.0-1.el6    python-requests.noarch 0:1.2.3-4.el6                         
  python-six.noarch 0:1.4.1-1.el6            python-urllib3.noarch 0:1.5-7.el6         python-werkzeug.noarch 0:0.9.3-2.el6                         
  python-wtforms.noarch 0:1.0.4-1.el6       

Complete!
[root@book ~]# 


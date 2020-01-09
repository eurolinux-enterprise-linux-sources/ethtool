Name:		ethtool
Epoch:		2
Version:	4.8
Release:	7%{?dist}
Summary:	Settings tool for Ethernet NICs

License:	GPLv2
Group:		Applications/System
#Old URL:	http://sourceforge.net/projects/gkernel/
URL:		http://ftp.kernel.org/pub/software/network/%{name}/

# When using tarball from released upstream version:
# - http://ftp.kernel.org/pub/software/network/%{name}/%{name}-%{version}.tar.bz2
#
# When generating tarball package from upstream git:
# - git clone git://git.kernel.org/pub/scm/network/ethtool/ethtool.git ethtool-6
# - cd ethtool-6; git checkout 669ba5cadfb15842e90d8aa7ba5a575f7a457b3e
# - cp -f ChangeLog ChangeLog.old; git log > ChangeLog.git
# - rm -rf .git; cd ..; tar cvfz ethtool-6.tar.gz ethtool-6
# - Use the visible date of latest git log entry for %{release} in spec file
Source0:	http://ftp.kernel.org/pub/software/network/%{name}/%{name}-%{version}.tar.xz
BuildRequires:	automake, autoconf
Conflicts:      filesystem < 3
Patch0:		0001-ethtool-add-register-dump-support-for-fjes-driver.patch
Patch1:		0002-ethtool-sync-help-output-for-x-X-with-man-page.patch
Patch2:		0003-ethtool-Fix-the-advertise-parameter-logic.patch
Patch3:		0004-ethtool-Fix-SFF-8079-cable-technology-bit-parsing.patch
Patch4:		0005-ethtool-Support-for-configurable-RSS-hash-function.patch
Patch5:		0006-net_tstamp.h-sync-with-net-next.patch
Patch6:		0007-ethtool-add-support-for-HWTSTAMP_FILTER_NTP_ALL.patch
Patch7:		0008-ethtool-copy.h-sync-with-net-next.patch
Patch8:		0009-ethtool-Add-support-for-2500baseT-5000baseT-link-mod.patch
Patch9:		0010-ethtool.8-Fix-formatting-of-advertise-bitmask.patch
Patch10:	0011-ethtool.8-Document-56000-advertise-link-modes.patch
Patch11:	0012-ethtool-Remove-UDP-Fragmentation-Offload-error-print.patch
Patch12:	0013-ethtool-copy.h-sync-with-net-next.patch
Patch13:	0014-ethtool-Support-for-FEC-encoding-control.patch

%description
This utility allows querying and changing settings such as speed,
port, auto-negotiation, PCI locations and checksum offload on many
network devices, especially of Ethernet devices.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1

# Only needed when using upstream git
# aclocal
# autoheader
# automake --gnu --add-missing --copy
# autoconf

%build
aclocal
automake --gnu --add-missing --copy
%configure
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} INSTALL='install -p' install

%files
%doc AUTHORS ChangeLog* COPYING LICENSE NEWS README
%{_sbindir}/%{name}
%{_mandir}/man8/%{name}.8*

%changelog
* Wed Jan 10 2018 Ivan Vecera <ivecera@redhat.com> - 2:4.8-7
- Fixed synopsis in ethtool man page

* Tue Jan  9 2018 Ivan Vecera <ivecera@redhat.com> - 2:4.8-6
- Added support for setting FEC parameters

* Fri Jan  5 2018 Ivan Vecera <ivecera@redhat.com> - 2:4.8-5
- Fixed changelog

* Fri Jan  5 2018 Ivan Vecera <ivecera@redhat.com> - 2:4.8-4
- Fixed UDP fragmentation offloading error messages printed on kernel-alt >=4.14

* Tue Nov 14 2017 Ivan Vecera <ivecera@redhat.com> - 2:4.8-3
- Added support for 2500baseT/5000baseT link modes

* Fri Nov  3 2017 Ivan Vecera <ivecera@redhat.com> - 2:4.8-2
- Added support for configurable RSS hash function
- Fixed SFF 8079 cable technology bit parsing
- Added support for HWTSTAMP_FILTER_NTP_ALL

* Wed Mar 22 2017 Ivan Vecera <ivecera@redhat.com> - 2:4.8-1
- Rebased against upstream v4.8

* Fri Mar 17 2017 Ivan Vecera <ivecera@redhat.com> - 2:4.5-6
- Fixed the "advertise" parameter logic

* Tue Feb 21 2017 Ivan Vecera <ivecera@redhat.com> - 2:4.5-5
- Fixed help page for commands -x and -X

* Thu Feb  2 2017 Ivan Vecera <ivecera@redhat.com> - 2:4.5-4
- Add register dump support for fjes driver

* Tue Aug 16 2016 Ivan Vecera <ivecera@redhat.com> - 2:4.5-3
- Added support for new ETHTOOL_xLINKSETTINGS API
- Added support for diagnostics information for QSFP Plus/QSFP28 modules
- Added support for 25G/50G/100G supported and advertised speed modes

* Fri Mar 18 2016 Ivan Vecera <ivecera@redhat.com> - 2:4.5-2
- Fixed several memory leaks

* Wed Mar 16 2016 Ivan Vecera <ivecera@redhat.com> - 2:4.5-1
- Update to the upstream version v4.5

* Fri Oct 31 2014 Ivan Vecera <ivecera@redhat.com> - 2:3.15-2
- Support for configurable RSS hash key

* Mon Sep 15 2014 Ivan Vecera <ivecera@redhat.com> - 2:3.15-1
- Update to the latest upstream

* Fri Jan 24 2014 Daniel Mach <dmach@redhat.com> - 2:3.8-3
- Mass rebuild 2014-01-24

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 2:3.8-2
- Mass rebuild 2013-12-27

* Mon Mar 04 2013 Jaromir Capik <jcapik@redhat.com> - 2:3.8-1
- Update to 3.8 (#916922)

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2:3.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Dec 17 2012 Jaromir Capik <jcapik@redhat.com> - 2:3.7-1
- Update to 3.7 (#887463)

* Tue Oct 23 2012 Jaromir Capik <jcapik@redhat.com> 2:3.6-1
- Update to 3.6 (#863774)

* Tue Sep 25 2012 Jaromir Capik <jcapik@redhat.com> 2:3.5-1
- Update to 3.5 (#840741)

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2:3.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun 28 2012 Jaromir Capik <jcapik@redhat.com> 2:3.4.1-1
- Update to 3.4.1 (#830263)

* Wed Jan 25 2012 Harald Hoyer <harald@redhat.com> 2:3.2-2
- install everything in /usr
  https://fedoraproject.org/wiki/Features/UsrMove

* Fri Jan 13 2012 Jaromir Capik <jcapik@redhat.com> 2:3.2-1
- Update to 3.2 (#781357)
- Minor spec file changes according to the latest guidelines

* Fri Dec 23 2011 Robert Scheck <robert@fedoraproject.org> 2:3.1-1
- Upgrade to 3.1 (#728480)

* Sun Jul 17 2011 Robert Scheck <robert@fedoraproject.org> 2:2.6.39-1
- Upgrade to 2.6.39 (#710400)

* Mon Mar 21 2011 Robert Scheck <robert@fedoraproject.org> 2:2.6.38-1
- Upgrade to 2.6.38 (#667594)

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2:2.6.36-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Dec 31 2010 Robert Scheck <robert@fedoraproject.org> 2:2.6.36-1
- Upgrade to 2.6.36 (#623094)

* Wed Jul 14 2010 Jeff Garzik <jgarzik@redhat.com> 2:2.6.34-1
- Update to release 2.6.34.

* Thu Feb  4 2010 Jeff Garzik <jgarzik@redhat.com> 2.6.33-0.1
- update to version 2.6.33-pre1

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6-7.20090323git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Jul 18 2009 Robert Scheck <robert@fedoraproject.org> 6-6.20090323git
- Upgrade to GIT 20090323

* Thu Jul 16 2009 Jeff Garzik <jgarzik@redhat.com> 6-5.20090306git
- minor specfile cleanups

* Sat Mar 07 2009 Robert Scheck <robert@fedoraproject.org> 6-4.20090306git
- Upgrade to GIT 20090306

* Mon Feb 23 2009 Robert Scheck <robert@fedoraproject.org> 6-3.20090115git
- Rebuild for gcc 4.4 and rpm 4.6

* Sat Jan 17 2009 Robert Scheck <robert@fedoraproject.org> 6-2.20090115git
- Changes to match with Fedora Packaging Guidelines (#225735)
- Upgrade to GIT 20090115 (#225735, #477498)
- Removed bogus stated need of DEVNAME in -h/--help (#472038)
- Removed completely needless INSTALL file from %%doc (#472034)

* Wed Mar 12 2008 Tom "spot" Callaway <tcallawa@redhat.com> 6-1
- Upgrade to ethtool version 6

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 5-2
- Autorebuild for GCC 4.3

* Thu Dec 14 2006 Jay Fenlason <fenlason@redhat.com> 5-1
- Upgrade to ethtool version 5 to close
  bz#184985: RFE: 10gigE support
  bz#204840: "buffer overflow detected" when devname's length >=16 of ethtool
  Resolves: #184985, #204840

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 3-1.2.2
- rebuild

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 3-1.2.1
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 3-1.2
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Thu Mar  3 2005 Jeff Garzik <jgarzik@pobox.com>
- Update to version 3.
- Use %%buildroot macro, rather than RPM_BUILD_ROOT env var,
  as recommended by RPM packaging guidelines.

* Sun Feb 27 2005 Florian La Roche <laroche@redhat.com>
- Copyright: -> License

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Sep  5 2003 Bill Nottingham <notting@redhat.com> 1.8-2
- remove bogus check for devices starting with ethXX, this time applying
  the patch

* Thu Jul 24 2003 Bill Nottingham <notting@redhat.com> 1.8-1
- update to 1.8
- remove bogus check for devices starting with ethXX

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Sat Feb  8 2003 Bill Nottingham <notting@redhat.com> 1.6-5
- move to /sbin

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Thu Dec 12 2002 Tim Powers <timp@redhat.com> 1.6-3
- rebuild on all arches

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu Jun 20 2002 Florian La Roche <Florian.LaRoche@redhat.de>
- update to 1.6

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Mon Mar  4 2002 Bill Nottingham <notting@redhat.com> 1.5-1
- 1.5

* Thu Feb 21 2002 Bill Nottingham <notting@redhat.com>
- rebuild

* Wed Jan 09 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Tue Dec  4 2001 Bill Nottingham <notting@redhat.com>
- update to 1.4

* Fri Aug  3 2001 Bill Nottingham <notting@redhat.com>
- return of ethtool! (#50475)

* Wed Jul 12 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Sun Jun 18 2000 Matt Wilson <msw@redhat.com>
- rebuilt for next release
- use FHS man path

* Tue Feb 22 2000 Bill Nottingham <notting@redhat.com>
- handle compressed manpages

* Wed Apr 14 1999 Bill Nottingham <notting@redhat.com>
- run through with new s/d

* Tue Apr 13 1999 Jakub Jelinek <jj@ultra.linux.cz>
- initial package.

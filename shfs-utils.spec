%define	module	shfs
%define	name	%{module}-utils
%define	version	0.35
%define release	7

Summary:	Tools for (Secure) SHell File System module
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		System/Kernel and hardware
Url:		http://shfs.sourceforge.net/
Source0:	http://atrey.karlin.mff.cuni.cz/~qiq/src/shfs/%{module}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Mount shares from remote hosts using plain ssh/rsh connection.i
This package contains mount/umount utility for shfs kernel module.
   
%prep
%setup -q -n %{module}-%{version}

%build
%make CFLAGS="%{optflags} -iquote -I. -I../shfs/Linux-2.4/ -DSHFS_VERSION=\"%{version}\"" utils
make docs-install ROOT=. HTML_DOC_DIR=doc docs-install

%install
rm -rf %{buildroot}
make ROOT=%{buildroot} HTML_DOC_DIR=/doc MAN_PAGE_DIR=%{_mandir} utils-install docs-install
rm -rf doc
mv %{buildroot}/doc .

%clean
rm -rf %{buildroot}

%files
%defattr(644,root,root,755)
%doc TODO Changelog doc/*
%defattr(-,root,root)
%{_bindir}/shfsmount 
%{_bindir}/shfsumount 
/sbin/mount.shfs
%{_mandir}/man8/shfsmount.8*
%{_mandir}/man8/shfsumount.8*


%changelog
* Thu Oct 08 2009 Herton Ronaldo Krzesinski <herton@mandriva.com.br> 0.35-6mdv2010.0
+ Revision: 456209
- Rebuild for updated changelog.

* Thu Oct 08 2009 Herton Ronaldo Krzesinski <herton@mandriva.com.br> 0.35-5mdv2010.0
+ Revision: 456172
- Don't use deprecated -I- option while building (use -iquote).

  + Thierry Vignaud <tvignaud@mandriva.com>
    - rebuild

* Fri Aug 08 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.35-4mdv2009.0
+ Revision: 269248
- rebuild early 2009.0 package (before pixel changes)
- rebuild

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 0.35-2mdv2008.1
+ Revision: 140792
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request
    - fix summary-ended-with-dot

* Sat Jun 23 2007 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.35-2mdv2008.0
+ Revision: 43501
- rebuild (closes #31553)
- Import shfs-utils



* Mon Aug 02 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.35-1mdk
- inital mdk release

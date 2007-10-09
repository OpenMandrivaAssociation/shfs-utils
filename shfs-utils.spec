%define	module	shfs
%define	name	%{module}-utils
%define	version	0.35
%define	release	%mkrel 2

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
%make CFLAGS="%{optflags} -I- -I. -I../shfs/Linux-2.4/ -DSHFS_VERSION=\"%{version}\"" utils
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

#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	SGI
%define	pnam	FAM
Summary:	SGI::FAM - Perl interface to SGI/Irix File Access Monitor
#Summary(pl):	
Name:		perl-SGI-FAM
Version:	1.002
Release:	0.1
License:	UNKNOWN
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	e92451d3d8fbb9ea6e1995f80d5b086a
BuildRequires:	fam-devel
BuildRequires:	perl-File-PathConvert
BuildRequires:	perl-Getopt-Mixed
BuildRequires:	perl-Test-Helper
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Provides a somewhat higher-level and friendlier interface to the SGI/Irix File Access
Monitor API. This allows one to monitor both local and remote (NFS-mounted) files and
directories for common filesystem events. To do so, you must register "monitors" on
specified pathnames and wait for events to arrive pertaining to them. To get a full
description of the API, you should see fam(3x).

Since FAM only deals with absolute pathnames, all paths are canonicalized internally
and monitors are held on canonical paths. Whenever a path is returned from this module,
howvever, via which or monitored with no arguments, the originally specified path
is given for convenience.

# %description -l pl
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README TODO
%attr(755,root,root) %{_bindir}/*
%{perl_vendorarch}/SGI/*.pm
%dir %{perl_vendorarch}/auto/SGI/FAM
%{perl_vendorarch}/auto/SGI/FAM/*.bs
%attr(755,root,root) %{perl_vendorarch}/auto/SGI/FAM/*.so
%{_mandir}/man[13]/*

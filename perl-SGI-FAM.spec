#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	SGI
%define	pnam	FAM
Summary:	SGI::FAM - Perl interface to SGI/Irix File Access Monitor
Summary(pl.UTF-8):	SGI::FAM - perlowy interfejs do monitora dostępu do plików FAM
Name:		perl-SGI-FAM
Version:	1.002
Release:	4
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	e92451d3d8fbb9ea6e1995f80d5b086a
BuildRequires:	fam-devel
BuildRequires:	perl-File-PathConvert
BuildRequires:	perl-Getopt-Mixed
BuildRequires:	perl-Test-Helper
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Provides a somewhat higher-level and friendlier interface to the
SGI/Irix File Access Monitor API. This allows one to monitor both
local and remote (NFS-mounted) files and directories for common
filesystem events. To do so, you must register "monitors" on specified
pathnames and wait for events to arrive pertaining to them. To get a
full description of the API, you should see fam(3x).

%description -l pl.UTF-8
SGI::FAM udostępnia nieco bardziej wysokopoziomowy i przyjazny
interfejs do API monitora dostępu do plików FAM (File Access Monitor)
pochodzącego z SGI/Iriksa. Pozwala on monitorować zarówno lokalne jak
i zdalne (podmontowane przez NFS) pliki i katalogi pod kątem zwykłych
zdarzeń występujących w systemach plików. Aby to zrobić, należy
zarejestrować "monitory" na podanych ścieżkach plików i oczekiwać na
nadejście związanych z nimi zdarzeń. Pełny opis API znajduje się w
manualu fam(3x).

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%{__sed} -i -e '1s,#!.*/bin/perl5,#!%{__perl},' magicrcs monitor

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
# %{_bindir}/magicrcs seems to be broken
%attr(755,root,root) %{_bindir}/mo*
%dir %{perl_vendorarch}/SGI
%{perl_vendorarch}/SGI/*.pm
%dir %{perl_vendorarch}/auto/SGI
%dir %{perl_vendorarch}/auto/SGI/FAM
%{perl_vendorarch}/auto/SGI/FAM/*.bs
%attr(755,root,root) %{perl_vendorarch}/auto/SGI/FAM/*.so
%{perl_vendorarch}/auto/SGI/FAM/*.ix
%{perl_vendorarch}/auto/SGI/FAM/*.al
%{_mandir}/man1/mo*
%{_mandir}/man3/*

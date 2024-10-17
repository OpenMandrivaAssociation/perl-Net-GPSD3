%define upstream_name    Net-GPSD3
%define upstream_version 0.19

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Net::GPSD3 Return Satellite Object
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Net/Net-GPSD3-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(DateTime)
BuildRequires:	perl(DateTime::Format::W3CDTF)
BuildRequires:	perl(GPS::Point)
BuildRequires:	perl(IO::Socket::INET6)
BuildRequires:	perl(JSON::XS)
BuildRequires:	perl(Test::Simple)
BuildArch:	noarch

%description
Net::GPSD3 provides an object client interface to the gpsd server daemon
utilizing the version 3.1 protocol. gpsd is an open source GPS deamon from
http://gpsd.berlios.de/. Support for Version 3 of the protocol (JSON) was
adding to the daemon in version 2.90. If your daemon is before 2.90 then
please use the the Net::GPSD manpage package.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc README Changes LICENSE META.yml
%{_mandir}/man3/*
%{perl_vendorlib}/*
# %{_bindir}/perl-Net-GPSD3-Example.pl
# %{_bindir}/perl-Net-GPSD3-Handler.pl
# %{_bindir}/perl-Net-GPSD3-poll.pl
# %{_mandir}/man1/perl-Net-GPSD3-Example.pl.1*
# %{_mandir}/man1/perl-Net-GPSD3-Handler.pl.1*
# %{_mandir}/man1/perl-Net-GPSD3-poll.pl.1*

%changelog
* Mon Jul 18 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.170.0-1mdv2011
+ Revision: 690524
- new version

* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 0.110.0-2
+ Revision: 657801
- rebuild for updated spec-helper

* Sun Oct 31 2010 Olivier Thauvin <nanardon@mandriva.org> 0.110.0-1mdv2011.0
+ Revision: 590778
- import perl-Net-GPSD3



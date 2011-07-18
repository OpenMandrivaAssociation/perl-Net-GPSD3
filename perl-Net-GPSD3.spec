%define upstream_name    Net-GPSD3
%define upstream_version 0.17

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Net::GPSD3 Return Satellite Object
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Net/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(DateTime)
BuildRequires: perl(DateTime::Format::W3CDTF)
BuildRequires: perl(GPS::Point)
BuildRequires: perl(IO::Socket::INET6)
BuildRequires: perl(JSON::XS)
BuildRequires: perl(Test::Simple)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
Net::GPSD3 provides an object client interface to the gpsd server daemon
utilizing the version 3.1 protocol. gpsd is an open source GPS deamon from
http://gpsd.berlios.de/. Support for Version 3 of the protocol (JSON) was
adding to the daemon in version 2.90. If your daemon is before 2.90 then
please use the the Net::GPSD manpage package.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc README Changes LICENSE META.yml
%{_mandir}/man3/*
%perl_vendorlib/*
%{_bindir}/perl-Net-GPSD3-Example.pl
%{_bindir}/perl-Net-GPSD3-Handler.pl
%{_bindir}/perl-Net-GPSD3-poll.pl
%{_mandir}/man1/perl-Net-GPSD3-Example.pl.1*
%{_mandir}/man1/perl-Net-GPSD3-Handler.pl.1*
%{_mandir}/man1/perl-Net-GPSD3-poll.pl.1*




Name:		alsa-ucm-conf
Summary:	Use Case Manager configuration for ALSA
Version:	1.2.15.3
Release:	1
License:	BSD-3-Clause
Source0:	https://www.alsa-project.org/files/pub/lib/alsa-ucm-conf-%{version}.tar.bz2
BuildArch:	noarch

%description
Use Case Manager configuration for ALSA

%prep
%build

%install
mkdir -p %{buildroot}/%{_datadir}/alsa/ucm2
tar xvjf %{SOURCE0} -C %{buildroot}/%{_datadir}/alsa --strip-components=1 "*/ucm2"

%files
%{_datadir}/alsa/ucm2/*

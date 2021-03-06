Name:           nethserver-docker
Version: 0.0.0
Release: 1%{?dist}
Summary:        NethServer Docker configuration

License:        GPLv3+
URL: %{url_prefix}/%{name}
Source0:        %{name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  nethserver-devtools
Requires:       docker-ce

%description
NethServer configuration for Docker CE

%prep
%setup

%build
%{makedocs}
perl createlinks


%install
(cd root   ; find . -depth -print | cpio -dump %{buildroot})
%{genfilelist} %{buildroot} > %{name}-%{version}-filelist
mkdir -p %{buildroot}%{_nsstatedir}/portainer


%files -f %{name}-%{version}-filelist
%doc COPYING
%doc README.rst
%config(noreplace) %attr (0644,root,root) %{_sysconfdir}/docker/docker.conf
%dir %{_nseventsdir}/%{name}-update
%dir %{_nsstatedir}/portainer

%changelog
* Mon Sep 10 2018 Davide Principi <davide.principi@nethesis.it> - 0.0.0
- Initial version

%define pypi_name subprocess32
# we don't want to provide private python extension libs
%{?filter_setup:
%filter_provides_in %{python2_sitearch}/.*\.so$
%filter_setup
}

Name:           python2-subprocess32
Version:        3.2.6
Release:        1
Summary:        Backport of subprocess module from Python 3.2 to Python 2.*
Group:          Development/Python
License:        Python
URL:            http://pypi.python.org/pypi/subprocess32/
Source0:        https://pypi.io/packages/source/s/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildRequires:  pkgconfig(python2)
BuildRequires:	pythonegg(setuptools)

%description
Backport of the subprocess module from Python 3.2 for use on 2.x.


%prep
%setup -q -n subprocess32-%{version}


%build
%py2_build


%install
%py2_install


%files -n python2-subprocess32
%doc LICENSE README.txt
%{python2_sitearch}/_posixsubprocess.so
%{python2_sitearch}/subprocess32*.egg-info
%{python2_sitearch}/subprocess32.py*


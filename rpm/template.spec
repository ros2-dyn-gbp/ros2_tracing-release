%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/iron/.*$
%global __requires_exclude_from ^/opt/ros/iron/.*$

Name:           ros-iron-ros2trace
Version:        6.3.0
Release:        2%{?dist}%{?release_suffix}
Summary:        ROS ros2trace package

License:        Apache 2.0
URL:            https://index.ros.org/p/ros2trace/
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-iron-ros2cli
Requires:       ros-iron-tracetools-trace
Requires:       ros-iron-ros-workspace
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  ros-iron-ros-workspace
BuildRequires:  ros-iron-ros2cli
BuildRequires:  ros-iron-tracetools-trace
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%if 0%{?with_tests}
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  ros-iron-ament-copyright
BuildRequires:  ros-iron-ament-flake8
BuildRequires:  ros-iron-ament-mypy
BuildRequires:  ros-iron-ament-pep257
BuildRequires:  ros-iron-ament-xmllint
%endif

%description
The trace command for ROS 2 command line tools.

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/iron/setup.sh" ]; then . "/opt/ros/iron/setup.sh"; fi
%py3_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/iron/setup.sh" ]; then . "/opt/ros/iron/setup.sh"; fi
%py3_install -- --prefix "/opt/ros/iron"

%if 0%{?with_tests}
%check
# Look for a directory with a name indicating that it contains tests
TEST_TARGET=$(ls -d * | grep -m1 "\(test\|tests\)" ||:)
if [ -n "$TEST_TARGET" ] && %__python3 -m pytest --version; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/iron/setup.sh" ]; then . "/opt/ros/iron/setup.sh"; fi
%__python3 -m pytest $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/iron

%changelog
* Thu Apr 20 2023 Christophe Bedard <bedard.christophe@gmail.com> - 6.3.0-2
- Autogenerated by Bloom

* Tue Apr 18 2023 Christophe Bedard <bedard.christophe@gmail.com> - 6.3.0-1
- Autogenerated by Bloom

* Tue Apr 18 2023 Christophe Bedard <bedard.christophe@gmail.com> - 6.2.0-1
- Autogenerated by Bloom

* Thu Apr 13 2023 Christophe Bedard <bedard.christophe@gmail.com> - 6.1.0-1
- Autogenerated by Bloom

* Wed Apr 12 2023 Christophe Bedard <bedard.christophe@gmail.com> - 6.0.0-1
- Autogenerated by Bloom

* Tue Mar 21 2023 Christophe Bedard <bedard.christophe@gmail.com> - 5.1.0-2
- Autogenerated by Bloom


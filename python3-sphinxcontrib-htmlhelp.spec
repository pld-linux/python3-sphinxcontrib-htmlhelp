#
# Conditional build:
%bcond_with	tests	# unit tests (failing?)

Summary:	Sphinx extension which renders HMTL help files
Summary(pl.UTF-8):	Rozszerzenie Sphinksa tworzące pliki pomocy HTML
Name:		python3-sphinxcontrib-htmlhelp
Version:	2.0.0
Release:	4
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/sphinxcontrib-htmlhelp/
Source0:	https://files.pythonhosted.org/packages/source/s/sphinxcontrib-htmlhelp/sphinxcontrib-htmlhelp-%{version}.tar.gz
# Source0-md5:	70765b55395a3c20233631802902c840
URL:		https://pypi.org/project/sphinxcontrib-htmlhelp/
BuildRequires:	python3-modules >= 1:3.6
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-Sphinx
BuildRequires:	python3-html5lib
BuildRequires:	python3-pytest
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
sphinxcontrib-htmlhelp is a Sphinx extension which renders HTML help
files.

%description -l pl.UTF-8
sphinxcontrib-htmlhelp to rozszerzenie Sphinksa, tworzące pliki pomocy
HTML.

%prep
%setup -q -n sphinxcontrib-htmlhelp-%{version}

%build
%py3_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
%{__python3} -m pytest tests
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES LICENSE README.rst
%{py3_sitescriptdir}/sphinxcontrib/htmlhelp
%{py3_sitescriptdir}/sphinxcontrib_htmlhelp-%{version}-py*.egg-info
%{py3_sitescriptdir}/sphinxcontrib_htmlhelp-%{version}-py*-nspkg.pth

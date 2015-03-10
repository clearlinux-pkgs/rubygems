Name     : rubygems
Version  : 2.4.8
Release  : 9
URL      : http://production.cf.rubygems.org/rubygems/rubygems-2.4.8.tgz
Source0  : http://production.cf.rubygems.org/rubygems/rubygems-2.4.8.tgz
Summary  : The Ruby standard for publishing and managing third party libraries.
Group    : Development/Tools
License  : Ruby
BuildRequires: ruby
BuildRequires: ruby-dev 
BuildRequires: rubygem-psych
BuildRequires: rubygem-rdoc
Requires: ruby
Requires: rubygems-bin
Requires: rubygems-doc
Requires: rubygem-psych
Requires: rubygem-io-console

%description
The Ruby standard for publishing and managing third party libraries.

%package bin
Summary: bin components for the rubygems package.
Group: Binaries

%description bin
bin components for the rubygems package.

%package doc
Summary: doc components for the rubygems package.
Group: Documentation

%description doc
doc components for the rubygems package.

%prep
%setup -q 

%build

%install
rm -rf %{buildroot}
env \
    LANG=en_US.UTF-8 \
    ruby -Ilib setup.rb \
    --prefix=/ \
    --document \
    --backtrace \
    --destdir=%{buildroot}%{_datarootdir}/rubygems

mkdir -p %{buildroot}%{_bindir}
mv %{buildroot}%{_datarootdir}/rubygems/bin/gem %{buildroot}%{_bindir}/gem
rm -rf %{buildroot}%{_datarootdir}/rubygems/bin

mkdir -p %{buildroot}%{_libdir}/ruby/2.2.0
mv %{buildroot}%{_datarootdir}/rubygems/lib/* %{buildroot}%{_libdir}/ruby/2.2.0/.


%files
%defattr(-,root,root,-)
%{_libdir}/ruby/2.2.0/rubygems/*
%{_libdir}/ruby/2.2.0/rubygems.rb
%{_libdir}/ruby/2.2.0/ubygems.rb
%{_libdir}/ruby/2.2.0/gauntlet_rubygems.rb

%files bin
%defattr(-,root,root,-)
%{_bindir}/gem

%files doc 
%defattr(-,root,root,-)

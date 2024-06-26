# Generated by go2rpm 1.11.1
%bcond_without check

# https://github.com/elves/elvish
%global goipath         src.elv.sh
%global forgeurl        https://github.com/elves/elvish
Version:                0.20.1

%gometa -L -f

%global common_description %{expand:
Powerful scripting language & Versatile interactive shell.}

%global golicenses      LICENSE pkg-diff-LICENSE pkg-md-spec-LICENSE\\\
                        pkg-persistent-LICENSE pkg-rpc-LICENSE vscode-LICENSE
%global godocs          SECURITY.md CONTRIBUTING.md README.md\\\

Name:           elvish
Release:        %autorelease
Summary:        Powerful scripting language & Versatile interactive shell

License:        BSD-3-Clause AND BSD-2-Clause AND EPL-1.0
URL:            %{gourl}
Source:         %{gosource}

%description %{common_description}

%gopkg

%prep
%goprep -A
%autopatch -p1

mv pkg/diff/LICENSE pkg-diff-LICENSE
mv pkg/md/spec/LICENSE pkg-md-spec-LICENSE
mv pkg/persistent/LICENSE pkg-persistent-LICENSE
mv pkg/rpc/LICENSE pkg-rpc-LICENSE
mv vscode/LICENSE vscode-LICENSE

%generate_buildrequires
%go_generate_buildrequires

%build
%gobuild -o %{gobuilddir}/bin/elvish %{goipath}/cmd/elvish

%install
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%if %{with check}
%check
%gocheck
%endif

%files
%license LICENSE pkg-diff-LICENSE pkg-md-spec-LICENSE
%license pkg-persistent-LICENSE pkg-rpc-LICENSE vscode-LICENSE
%doc SECURITY.md CONTRIBUTING.md README.md
%{_bindir}/elvish

%changelog
%autochangelog

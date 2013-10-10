# revision 31686
# category Package
# catalog-ctan /macros/latex/contrib/pythontex
# catalog-date 2013-09-17 11:10:59 +0200
# catalog-license lppl1.3
# catalog-version 0.12
Name:		texlive-pythontex
Version:	0.12
Release:	1.1
Summary:	Run Python from within a document, typesetting the results
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/pythontex
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pythontex.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pythontex.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pythontex.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
# FIXME not really, only during update
Provides:	texlive-pythontex.bin
#Requires:	texlive-pythontex.bin

%description
The package allows you to enter Python code within a LaTeX
document, execute the code, and access its output in the
original document. Python code is only executed when it has
been modified, or when it meets user-specified criteria. Code
may be divided into user-defined sessions, which automatically
run in parallel. Errors and warnings are synchronized with the
LaTeX document, so that they refer to the document's line
numbers. External dependencies can be tracked, so that code is
re-executed when the data it depends on is modified. PythonTeX
also provides syntax highlighting for code in LaTeX documents
via the Pygments syntax highlighter. The package provides a
depythontex utility, that creates a copy of the document in
which all Python code has been replaced by its output. This is
useful for journal submissions, sharing documents, and
conversion to other formats.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/scripts/pythontex/depythontex.py
%{_texmfdistdir}/scripts/pythontex/depythontex2.py
%{_texmfdistdir}/scripts/pythontex/depythontex3.py
%{_texmfdistdir}/scripts/pythontex/pythontex.py
%{_texmfdistdir}/scripts/pythontex/pythontex2.py
%{_texmfdistdir}/scripts/pythontex/pythontex3.py
%{_texmfdistdir}/scripts/pythontex/pythontex_2to3.py
%{_texmfdistdir}/scripts/pythontex/pythontex_engines.py
%{_texmfdistdir}/scripts/pythontex/pythontex_install_texlive.py
%{_texmfdistdir}/scripts/pythontex/pythontex_utils.py
%{_texmfdistdir}/tex/latex/pythontex/pythontex.sty
%doc %{_texmfdistdir}/doc/latex/pythontex/README
%doc %{_texmfdistdir}/doc/latex/pythontex/pythontex.pdf
%doc %{_texmfdistdir}/doc/latex/pythontex/pythontex_gallery.pdf
%doc %{_texmfdistdir}/doc/latex/pythontex/pythontex_gallery.tex
%doc %{_texmfdistdir}/doc/latex/pythontex/pythontex_quickstart.pdf
%doc %{_texmfdistdir}/doc/latex/pythontex/pythontex_quickstart.tex
#- source
%doc %{_texmfdistdir}/source/latex/pythontex/pythontex.bat
%doc %{_texmfdistdir}/source/latex/pythontex/pythontex.dtx
%doc %{_texmfdistdir}/source/latex/pythontex/pythontex.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}

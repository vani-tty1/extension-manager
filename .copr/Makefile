srpm:
	dnf install -y rpmdevtools
	spectool -g -R *.spec
	rpmbuild -bs --define "_sourcedir ." --define "_srcrpmdir $(outdir)" *.spec

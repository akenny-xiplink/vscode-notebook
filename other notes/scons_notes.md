git submodule update from top level

sudo jexec -U root aljail /bin/sh -c "cd /usr/home/akenny/ui; JOB_NAME=6.0.0 BUILD_NUMBER=666 scons -U PRODUCT=xv6000 RELEASE=1 image"

# to get rid of image dir stuff
sudo jexec -U root aljail /bin/sh -c "cd /usr/home/akenny/ui; JOB_NAME=6.0.0 BUILD_NUMBER=666 scons -U PRODUCT=xv6000 RELEASE=1 --nuke-image"

# the nuclear option (keeps toolchain)
sudo jexec -U root aljail /bin/sh -c "cd /usr/home/akenny/ui; JOB_NAME=6.0.0 BUILD_NUMBER=666 scons -U PRODUCT=xv6000 RELEASE=1 --nuke-all"

as root
execute in the jail as the root user with sh
	cd into the worktree
	set the version and build numbers
	run scons, looking up for scons files
	to create a release image for this specific product


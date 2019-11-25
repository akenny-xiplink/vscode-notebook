git submodule update from top level
```
sudo jexec -U root build /bin/sh -c "cd /usr/home/akenny/UI; JOB_NAME=6.0.0 BUILD_NUMBER=666 scons -U PRODUCT=xv100000 RELEASE=1 image"
```
# to get rid of image dir stuff
```
sudo jexec -U root build /bin/sh -c "cd /usr/home/akenny/UI; scons PRODUCT=xv100000 --nuke-image"
```
# the nuclear option (keeps toolchain)
```
sudo jexec -U root build /bin/sh -c "cd /usr/home/akenny/UI; scons --nuke-all"
```
as root
execute in the jail as the root user with sh
	cd into the worktree
	set the version and build numbers
	run scons, looking up for scons files
	to create a release image for this specific product

# build a specific dir
```
sudo jexec -U root build /bin/sh -c "cd /usr/home/akenny/UI/path/to/dir; scons -U ."
```
note that this dir is in the main section, not compile or image
also note that you need to pay attention to where the output is going (i.e, `release` or `debug` in `compile`)

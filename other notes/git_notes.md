load and update all modules
git submodule update --init

get rid of unneeded modules
git submodule deinit

only init the submodules you actually need like those in external

cd /storage/git/public/u/akenny/
ls
git clone /storage/git/public/external/net-snmp.git/
ls
rm -rf net-snmp/
git clone --mirror /storage/git/public/external/net-snmp.git/
ls
cd net-snmp.git/
ls
ln -s ../../gitweb.category category

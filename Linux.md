<h3>This is the small cheat sheet for some of the popular linux commands I used daily.</h3>

<li><h2>1.Updating linux system</h2></li>
<li> i.sudo apt update</li>
<li> ii.sudo apt full-upgrade -y</li>
<li>iii.sudo apt dist-upgrade -y</li>
<li> iv.sudo apt autoremove</li>

<li><h2>2.Checking the user</h2></li>
  <li>i.whoami</li>

<li><h2>3.Creating bash scripting</h2></li>
  <li>i.#! /bin/bash</li>
<p>Note: After shebang then below it you add all your scripts you want to run then save the file.
      Then make sure you use chmod or just on the gui to give wxwcute permission to run the script.</p>

<li><h2>4.Change or grant permission</h2></li>
  <li>i.chmod +x or -X say for give execution power or take away execution</li>

<li><h2>5.Elevate yourself to root</h2></li>
 <li>i.sudo su</li>

<li><h2>6.Making Directory/navigation</h2></li>
  <li>i. mkdir name</li>
  <li>ii.pwd # display the current directory</li>
  <li>iii.cd # change directory</li>

<li><h2>7.Creating/readinf a file</h2></li>
  <li>i.touch name</li>
  <li>ii. nano name</li>
  <li>iii. cat name</li>

<li><h2>8.Managing Files</h2></li>
  <li>i.ls #list files and directories</li>
  <li>ii.cp #copies files</li>
  <li>iii.mv # move files and renaming them</li>
  <li>iv. rm # remove or delete file when using -r it forces remove</li>

<li><h2>9.System Info</h2></li>
  <li>i.uname -a</li>
  <li>ii.hostnamectl</li>
  <li>iii.lscpu</li>

<li><h2>10.system monitoring</h2></li>
  <li>i.top</li>
  <li>ii.kill -process id number-</li>

<li><h2>11.System Management</h2></li>
   <li>i.sudo systemctl start -name-</li>
   <li>ii.sudo systemctl stop -name-</li>
   <li>iii.sudo systemctl status -name-</li>
   <li>iv.sudo systemctl reload -name-</li>
   
<li><h2>12.Firewall Management</h2></li>
   <li>i.sudo ufw status</li>
   <li>ii. sudo ufw enable</li>
   <li>iii.sudo ufw disable</li>
   <li>iv.sudo ufw allow -name-</li>
   <li> v. sudo ufw deny -name-</li>


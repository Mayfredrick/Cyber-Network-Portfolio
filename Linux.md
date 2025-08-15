<h3>This is the small cheat sheet for some of the popular linux commands I used daily.</h3>

<h2>1.Updating linux system</h2>
<li> sudo apt update</li>
<li> sudo apt full-upgrade -y</li>
<li> sudo apt dist-upgrade -y</li>
<li> sudo apt autoremove</li>

<h2>2.Checking the user</h2>
  <li>whoami</li>

<h2>3.Creating bash scripting</h2>
  <li>#! /bin/bash</li>
  <p>Note: After shebang then below it you add all your scripts you want to run then save the file.
      Then make sure you use chmod or just on the gui to give wxwcute permission to run the script.</p>

<h2>4.Change or grant permission</h2>
  <li>chmod +x or -X say for give execution power or take away execution</li>

<h2>5.Elevate yourself to root</h2>
 <li>sudo su</li>

<h2>6.Making Directory/navigation</h2>
  <li> mkdir name</li>
  <li> pwd # display the current directory</li>
  <li> cd # change directory</li>

<h2>7.Creating/readinf a file</h2>
  <li>touch name</li>
  <li>nano name</li>
  <li>cat name</li>

<h2>8.Managing Files</h2>
  <li>ls #list files and directories</li>
  <li>cp #copies files</li>
  <li>mv # move files and renaming them</li>
  <li>rm # remove or delete file when using -r it forces remove</li>

<h2>9.System Info</h2>
  <li>uname -a</li>
  <li>hostnamectl</li>
  <li>lscpu</li>

<h2>10.system monitoring</h2>
  <li>top</li>
  <li>kill -process id number-</li>

<h2>11.System Management</h2>
   <li>sudo systemctl start -name-</li>
   <li>sudo systemctl stop -name-</li>
   <li>sudo systemctl status -name-</li>
   <li>sudo systemctl reload -name-</li>

<h2>12.Firewall Management</h2>
   <li>sudo ufw status</li>
   <li>sudo ufw enable</li>
   <li>sudo ufw disable</li>
   <li>sudo ufw allow -name-</li>
   <li>sudo ufw deny -name-</li>

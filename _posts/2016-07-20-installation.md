---
layout: page
title: "Installing the Plugin"
category: doc 
date: 2016-07-20 17:03:00
order: 1
---

### From QGIS Plugin Manager

To install the plugin, you can simply use QGIS Plugin Manager. In your QGIS, 
click ```Plugin``` menu and ```Manage and Install Plugins...```. After the 
Plugin Installer dialog shows up, search for ```QGIS Resources Sharing``` in 
the search box of the dialog in the ```All``` tab.

![Search Plugin]({{ site.baseurl }}/assets/search_plugin.png)


Select the ```QGIS Resources Sharing``` plugin and click ```Install```

### From the repository 
If you are adventurous and would like to get the latest code of the plugin, 
you can install it directly from the repository. The repository is in 
Github [here](https://github.com/akbargumbira/qgis_resources_sharing). There 
are 2 ways that you can do generally: 

* Download the zip from github here: [ZIP Master](https://github
.com/akbargumbira/qgis_resources_sharing/archive/master.zip), extract the 
zip, and copy the extracted files into QGIS local plugins directory (on linux
 it's ```~/.qgis2/python/plugins```, on Windows it's ```C:\Users\{username}\.qgis2\python\plugins```
  
* Use git, clone the repository in that directory (or using symbolic link). 
If you know git already, I don't think I need to explain more for this :)
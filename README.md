# Extract-ID3-info-from-mp3
#### Description:made for DAM coursiese homework1  
Given mp3 files，generate txt files（title,artist and album) and png files.

#### Note:
1.Only for mp3  
2.Only version ID3-V2 tested.(If the metadata of mp3 doesn't contain the cover picture, the png will be all black.)  

#### Environment:
python3 + eyed3(you may need to install python-magic first, see the dependencies here:https://github.com/ahupp/python-magic)  

#### Step:
1.Use powershell to modify the file name, ascending from 001.mp3.(the next step will fail to load the file if the file name contains some chinese characters).  

  cd PATH  
  $files=get-childitem  
  $a=1  
  foreach ($file in $files) {  
  if($a -lt 10)  
  {Rename-Item $file.name ("00$a.mp3")}    
  elseif($a -lt 100)  
  {Rename-Item $file.name ("0$a.mp3")}  
  else  
  {Rename-Item $file.name ("$a.mp3")}  
  $a+=1  
  }  

2.Execute the python script. The generated files will be in the same directory of the script. 

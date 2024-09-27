# SimplePortScanner 
This is a Simple port scanner that actively scans specified host of a network. This port scanner is not at all an industry standard and purpose of creating this port scanner is just to have fun and gaining knowledge about how port scanners actually work under the hood.
___
## Prerequisites
Before testing this code install following python modules :
- `python-nmap`
- `pyfiglet`

Install these by executing following commands on your terminal or powershell :
```
pip3 install python-nmap
pip3 install pyfiglet
```
___
## Usage
Running the port scanner :
```
python3 portscanner.py
```

Then you will be prompted to specify target and port/port range.
___
## Limitations and Considerations
- This port scanner is still open for improvements.
- User should not scan targets without permission because it might be considered unethical, instead use your own networks or `scanme.nmap.org` for testing purposes.
- Anybody can fork this project to their liking.
- User is not encouraged use this work for any unethical purposes.
__
from http.server import HTTPServer,BaseHTTPRequestHandler

content= '''
<!doctype html>
<html>
<head>
<title> My Web Server</title>
</head>
<body>
<h1>LAPTOP CONFIGURATION</h1>
<table BORDER="3" CELLSPACING="5" CELLPADDING="5">
    <TR>
        <TH>SYSTEM CONFIGURATION</TH>
        <TH>DESCRIPTION</TH>
    </TR>
    <TR>
        <TH>PROCESSOR</TH>
        <td><B>13th Gen Intel(R) Core(TM) i5-1335U   1.30 GHz</B></td>
    </TR>
    <TR>
        <TH>PRIMARY MEMORY</TH>
        <TD><B>16.0 GB (15.7 GB usable)</B></TD>
    </TR>
    <TR>
        <TH>SECONDARY MEMORY</TH>
        <TD><B>512 GB</B></TD>
    </TR>
    <TR>
        <TH>OPERATING SYSTEM</TH>
        <TD><B>Windows 11,64-bit operating system</B></TD>
    </TR>
    <TR>
        <TH>GRAPHICS CARD</TH>
        <TD><B>NVIDIA GeForce MX550</B></TD>
    </TR>
</table>
</body>
</html>
'''

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Get request received...")
        self.send_response(200) 
        self.send_header("content-type", "text/html")       
        self.end_headers()
        self.wfile.write(content.encode())

print("This is my webserver") 
server_address =('',8000)
httpd = HTTPServer(server_address,MyServer)
httpd.serve_forever()
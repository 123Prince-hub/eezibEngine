from django.shortcuts import render, redirect
from .models import Domain_Info
from django.http import HttpResponse
import subprocess
import os

# Create your views here.
def home(request):
    title = ['Sr.No', 'Mark', 'Action', 'Domain', 'Subdomain', 'Open_Ports', 'Comment', 'Directory', 'IP', 'Lookup', 'Status', 'Technology', 'Urls', 'Date']
    data = Domain_Info.objects.all().order_by('-id')
    context = {
        'datas':data,
        'titles': title
    }


    if request.method == 'POST':
        global domain
        domain = request.POST.get('domain')
        query = f'"sublist3r" -d {domain} -o subdomain1.txt | "subfinder" -d {domain} -o subdomain2.txt'
        subprocess.check_output(query, shell=True)
        readFiles = ['subdomain1.txt', 'subdomain2.txt'] 
        with open('outputFile.txt', 'w') as writeFile: 
            for file in readFiles: 
                with open(file) as inputFile:   
                    writeFile.write(inputFile.read())
                writeFile.write("\n")

        with open('outputFile.txt', 'r') as f:
            content = f.readlines()
            remove_duplicat_item = set(content)  
            content = list(remove_duplicat_item)
            content.sort()
            subdomainLst = []
            for i in content:
                subdomainLst.append(i)
        subdomainLists = []
        for ele in subdomainLst:
            subdomainLists.append(ele.strip())
        del subdomainLists[0]
        for i in range(len(subdomainLists)):
            datainsert = Domain_Info(domain=domain, subdomain=subdomainLists[i])        
            datainsert.save()
        
        # textfile = open("outputfile.txt", "w")
        # for element in subdomainLists:
        #     textfile.write(element)
        # textfile.close()



        # query2 = f'naabu -list outputfile.txt -o ports.txt'
        # Open_ports = subprocess.check_output(query2, shell=True)

        # with open('ports.txt', 'r') as f:
        #     content = f.readlines()

        # domains = []
        # for i in content:
        #     domains.append(i.strip())

        # port = []
        # for domainn in domains:
        #     if "www" not in domainn:
        #         p = domainn.split(":", 1)[1]
        #         port.append(p)
        # remove_duplicat_item = set(port)  
        # port = list(remove_duplicat_item)

        # with open("sample.txt", "a") as file_object:
        #     p = ", ".join(port)
        #     file_object.write(f'{domain} = {p}')
        
        # with open('sample.txt', 'r') as file:
        #     data = file.read().replace('\n', '')

        # with open('sample.txt','r') as firstfile, open(f'text_files/open_ports_files/{domain}.txt','w') as secondfile:
        #     for line in firstfile:
        #             secondfile.write(line)

        # with open('outputfile.txt', 'r') as firstfile, open(f'{domain}.txt','a') as secondfile:
        #     for line in firstfile:
        #             secondfile.write(line)
        
        # os.rename(f'{domain}.txt', f"text_files/subdomainFiles/{domain}.txt")

        os.remove('subdomain1.txt')
        os.remove('subdomain2.txt')
        os.remove('subd.txt')
        # os.remove('outputFile.txt')
        # os.remove('outputfile.txt')
        # os.remove('sample.txt')
        # os.remove('ports.txt')
        return redirect('home')
    return render(request, "index.html", context=context)

def open_ports(request, uid, subd):
    query = f'naabu -host {subd} -o ports.txt'    
    Open_ports = subprocess.check_output(query, shell=True)
    with open('ports.txt', 'r') as f:
        content = f.readlines()

    domains = []
    for i in content:
        domains.append(i.strip())

    port = []
    for domainn in domains:
        p = domainn.split(":", 1)[1]
        port.append(p)
    ports = ', '.join(port)

    Domain_Info.objects.filter(pk=uid).update(open_ports=ports)        
    return redirect('home')


def multi_open_ports(request):
    if request.method == 'GET':
        subdmn = request.GET.get('subdmn')
        subdmn = subdmn.split(",")
        with open('subd.txt', 'w') as f:
            for item in subdmn:
                f.write("%s\n" % item)
        query = f'naabu -list subd.txt -o pts.txt'    
        Open_ports = subprocess.check_output(query, shell=True)                
        return redirect('home')

from csv import DictReader, DictWriter
import csv
from posixpath import basename
from json import *
import xmltodict
import yaml
def checkFile():
    try:
        filePath = input("Veuillir saisire le chemain du fichier: ")
        ext = str(basename(filePath))
        ext = ext.split(".")
        ext = str(ext[-1])
        ext =ext.upper()
        if ext in["CSV","JSON","YAML","YML","XML"]:
            dictfile =[]
            fich = open(filePath,"r")
            if ext == "CSV":
                csvfile = DictReader(fich)
                for row in csvfile:
                    dictfile.append(row)
                return dictfile,ext
            elif ext =="JSON":
                with open(filePath,"r") as fich:
                    dictfile = load(fich)
                return dictfile,ext
            elif ext == "YML" or "YAML":
                with open(filePath,"r") as fich:
                    dictfile = load(fich)
                return dictfile,ext
            elif ext =="XML":
                xmlfile = open(filePath,'r')
                xmlfiledict = xmltodict.parse(xmlfile.read())
                dictfile = yaml.load(dump(xmlfiledict))
                return dictfile,ext
        else:
            print("Ce format de fichier n'est pas valide")
            return False
    except ValueError:
            print("Ce format de fichier n'est pas valide")
            return False


def dictTocsv(dictfile):
    for i in range(len(dictfile)):
        x = dictfile[i]
        key = list(x.keys())
    with open("csvfile.csv","w") as csv_file:
        writer_csv = DictWriter(csv_file,fieldnames= key)
        writer_csv.writeheader()
        for csvdata in dictfile:
            writer_csv.writerow(csvdata)
    msg = "Le fichier est converti sous format csv !!!"
    return msg


def dictTojson(dicfile):
    with open("jsonfile.csv","w") as json_file:
        dumps(dicfile,json_file)
    msg = "Le fichier est converti sous format json !!!"
    return msg


def dictToxml(dictfile):
    return True


# def dictToyml(dictfile):
#     with open("ymlfile.yml","w") as yml_file:
#         dump(dictfile,yml_file)
#     msg = "Le fichier est converti sous format json !!!"
#     return msg


def menu(ext,dictfile):
    if ext in "CSV":
        print("1 pour convertir le fichier en JSON")
        print("2 pour convertir le fichier en XML")
        print("3 pour convertir le fichier en YML")
        print("Appuiller sur un autre numéro pour changer de fichier")
        choice = input("Faites votre choix: ")
        if choice == "1":
            dictTojson(dictfile)
        elif choice == "2":
            dictToxml(dictfile)
        # elif choice == "3":
        #     dictToyml(dictfile)
        else:
            checkFile()
    elif ext in ["YML","YAML"]:
        print("1 pour convertir le fichier en JSON")
        print("2 pour convertir le fichier en XML")
        print("3 pour convertir le fichier en CSV")
        print("Appuiller sur un autre numéro pour changer de fichier")
        choice = input("Faites votre choix: ")
        if choice == "1":
            dictTojson(dictfile)
        elif choice == "2":
            dictToxml(dictfile)
        elif choice == "3":
            dictTocsv(dictfile)
        else:
            checkFile()
    elif ext in "JSON":
        print("1 pour convertir le fichier en CSV")
        print("2 pour convertir le fichier en XML")
        print("3 pour convertir le fichier en YML")
        print("Appuiller sur un autre numéro pour changer de fichier")
        choice = input("Faites votre choix: ")
        if choice == "1":
            dictTocsv(dictfile)
        elif choice == "2":
            dictToxml(dictfile)
        # elif choice == "3":
        #     dictToyml(dictfile)
        else:
            checkFile()
    elif ext in "XML":
        print("1 pour convertir le fichier en JSON")
        print("2 pour convertir le fichier en CSV")
        print("3 pour convertir le fichier en YML")
        print("Appuiller sur un autre numéro pour changer de fichier")
        choice = input("Faites votre choix: ")
        if choice == "1":
            dictTojson(dictfile)
        elif choice == "2":
            dictTocsv(dictfile)
        # elif choice == "3":
        #     dictToyml(dictfile)
        else:
            checkFile()

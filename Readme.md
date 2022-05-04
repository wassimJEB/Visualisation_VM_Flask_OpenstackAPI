## Architecture du Dashboard
• L’extraction de l’Etat du datacentre :
- La liste des servers , Liste des images et flavors et les informations de (Vcpu,vram,vmemoire)
- Liste des instances et des opérations crud delete,stop,refresh et start
- La liste des machines
- Visualisation du pourcentage de vcpu,vram et memoire disponible
• L’automatisation des taches de maintenance :
- Upgrade
- Panne HW : avoir une notification sur le dysfonctionnement de l’un des matérielles
- Extension : la necessité d’avoir des espaces libre dans les servers
=>Input modele de redondance afin de savoir combien de vm standby et combien active
=>Notification en cas de panne
=>Input nombre vcpu vmemoire et vram en cas d’extension
=>Input fichier csv contenant la liste de VNF et les caractéristiques de VM (par Example
MSS = 150 VM 75 active 75 standby )
=>Input modele de prediction
• CHATBOT :
- Réponse sur les questions fréquente


## Aspect technique 

### Execution de l'app 
##### python3 app.py 
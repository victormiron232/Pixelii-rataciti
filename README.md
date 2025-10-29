1. 
Autor(i): Abdelrahman Osman Elfaki, Wassim Messoudi, Anas Bushnag, Shakour Abuzneid, Tareq Alhmiedat
An: 2023
Titlu: A Smart Real-Time Parking Control and Monitoring System
Aplicație / Domeniu: Smart parking / real-time allocation and monitoring
Tehnologii utilizate: Cameras, mobile app, server-side logic, scheduling algorithms
Metodologie / Abordare: Sistem combinat: monitorizare ocupare + alocare dinamică a locurilor (ex. pentru angajați), interfață mobilă pentru rezervare și management.
Rezultate: Demonstrații pe pilot: sisteme funcționale în timp real, reducere a conflictele de parcare prin alocare; latențe acceptabile pentru aplicații enterprise.
Limitări: Probleme de scalare pentru parcări foarte mari, Dependență de calitatea camerelor / instalare
Comentarii suplimentare: Relevanță mare pentru gestionare / rezervare, nu doar detecție; potrivit pentru parcări private (companii, campusuri)

2.
Autor(i): Tuan T. Nguyen și Mina Sartipi
An: 2024
Titlu: Smart Camera Parking System With Auto Parking Spot Detection
Aplicație / Domeniu: Camera-based parking spot detection (computer vision)
Tehnologii utilizate: Camera (ceiling / overhead), transformer-based detector (deformable DETR), image processing pipeline
Metodologie / Abordare: Abordare bazată pe detectoare moderne (transformers) pentru a localiza corect locurile și estima ocuparea; auto-mapare ROI (nu e nevoie de grid manual etichetat).
Rezultate: Performanță superioară față de detectoare CNN clasice pe seturi cu variații mari (ocluzii, unghiuri), măsurată prin map / precizie.
Limitări: Necesită putere de calcul mai mare; latență ridicată; date de antrenare necesare
Comentarii suplimentare: Foarte eficient pentru soluție camera-only; reduce efortul de mapare manuală

3.
Autor(i): Yusufbek Yuldashev, Mukhriddin Mukhiddinov, Akmalbek B. Abdusalomov, Rashid Nasimov și Jinsoo Cho
An: 2024
Titlu: Parking Lot Occupancy Detection and Classification using fisheye cameras
Aplicație / Domeniu: Camera-based (fisheye / 360°) parking monitoring; clasificare tip loc (EV / handicap / normal)
Tehnologii utilizate: Fisheye cameras, image rectification, CNN classifiers, post-processing
Metodologie / Abordare:Camere fisheye pentru acoperire largă, Clasificare suplimentară a tipului locurilor, Pipeline de segmentare + clasificare
Rezultate: Bune rezultate în acoperire (mai puține camere necesare) și acuratețe bună la clasificare; metrici: precizie.
Limitări: Distorsiunile fisheye trebuie compensate; complexitate preprocesare; performanță afectată de iluminare extrema.
Comentarii suplimentare: Recomandat pentru parcări unde e necesara o acoperire mare cu puține camere. Identificarea tipului de loc (EV / dizabilitati) poate fi utilă pentru management.

4.

Autor(i): Hamid Reza Tohidypour, Yixiao Wang, Panos Nasiopoulos și Mahsa T. Pourazad
An: 2022
Titlu: A Deep Learning-Based Unoccupied Parking Space Detection Method for City Lots
Aplicație / Domeniu: Camera-based, detecție spații ocupate / libere
Tehnologii utilizate: YOLOv4 (detecție), preprocesare imagini, grid-based labeling
Metodologie / Abordare: Detectare cu YOLO pe imagini fixe / video; grid de locuri creat manual; clasificare occupied / unoccupied pe fiecare loc.
Rezultate: Acuratețe ~90.6% unoccupied; ~95.7% occupied
Limitări: Necesită mapare manuală grid; vulnerabil la umbre / iluminare slabă
Comentarii suplimentare: Bun ca referință practică (YOLOv4 e light/rapid) — potrivit pentru prototipuri pe edge device (Jetson, TPU) pentru camere fixe cu grid stabil.

5. 

Autor(i): Gustavo P. C. P. da Luz, Gabriel Massuyoshi Sato, Luis Fernando Gomez Gonzalez, Juliana Freitag Borin 
An: 2024
Titlu: Smart Parking with Pixel-Wise ROI Selection for Vehicle Detection Using YOLOv8, YOLOv9, YOLOv10, and YOLOv11
Aplicație / Domeniu: Monitorizare parcare (vehicle detection în parcări)
Tehnologii utilizate: Camere + IoT + Edge Computing + YOLOv8/9/10/11
Metodologie / Abordare: ROI pixel-wise pentru detecţie, comparaţie între versiuni YOLO pe edge/cloud
Rezultate: 99.68% balanced accuracy pe dataset propriu (3 484 imagini)
Limitări: Dataset relativ mic; teste pe mediu controlat, latenţă diferită în funcţie de hardware
Comentarii suplimentare: Foarte relevant pentru proiect: combină cameră + edge + DL, măsură de acuratețe foarte bună — poţi folosi ca referinţă de performanţă şi alegere tehnologie


Schema bloc a proiectului:
<img width="121" height="721" alt="Schema_bloc drawio" src="https://github.com/user-attachments/assets/5a8e4a64-846c-4f45-be7e-8c18cea2dc4a" />





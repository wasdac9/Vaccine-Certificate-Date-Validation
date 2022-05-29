# Vaccine-Certificate-Date-Validation

## Software Requirements
1) opencv-python 4.5.3.56 or above
2) pytesseract 0.3.8 or above
3) python 3
4) pillow 9.1.1 or above

## Hardware Requirements
1) Webcam

## **Downloading Tesseract OCR**
Along with above requirements you also need Tesseract OCR Engine.

**Download Tesseract OCR for windows**
1) 32-bit version:
   https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-w32-setup-v5.0.1.20220118.exe
2) 64-bit version:
   https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-w64-setup-v5.0.1.20220118.exe

More info at https://github.com/UB-Mannheim/tesseract/wiki
Note: Download the file and extract the contents of the file. Keep a note of the path of tesseract.exe(Eg: Desktop\Tesseract\tesseract.exe)

## **Goal of Project**
During COVID-19 Pandemic, in most establishments like Malls, Electronic Stores, Shopping Centers, etc, the security checked Vaccine Certificate manually at the entrance to permit entry, as per Government Regulations. The criteria for entry was that every individual has completed 2 Vaccine Doses and 14 days have passed since their 2nd Vaccine Dose. The people that passed this criteria were granted entry in the establishment as per Government Regulations. This is a proof of concept project with a goal of automating this manual process of dates validation from Vaccine Certificates using Opencv and Tesseract OCR

## **Project Information**
In this Project we place our Vaccine Certificate(since vaccine certificate generated at the time of 2nd vaccine dose consists of both vaccine dose dates, we use that certificate here) in front of the webcam and the code extracts dates from the certificate using OCR and checks if at least 14 days have passed since the 2nd Vaccine Dose date to permit entry.

If 14 days have passed, the code displays "ALLOWED" on the GUI when "Validate Dates" button is pressed,
If 14 days have not passed, the code displays "NOT ALLOWED" on the GUI when "Validate Dates" button is pressed,
and If the certificate is not clearly visible or if OCR cannot extract dates, the code displays "CHECK" on the GUI when "Validate Dates" button is pressed.

Eg: If a person takes their 1st Vaccine on 01 Jun 2021 and 2nd Vaccine on 10 Dec 2021, and now they want to enter a mall on 15 Dec 2021, then the code will display "NOT ALLOWED" on the GUI, as 14 days have not passed since their 2nd Vaccine Dose. But if the same person tries to enter the mall on 25 Dec 2021, the code will display "ALLOWED".

### **Code**

Setting up path to tesseract.exe(tesseract.exe can be found at download location of Tesseract OCR Engine Eg: Desktop\Tesseract\tesseract.exe)

```
class Page(tk.Frame):
    pytesseract.pytesseract.tesseract_cmd = r"<path\to\tesseract.exe>"   //set path to tesseract.exe
    tdy = datetime.today()
    allowed = tdy - timedelta(days=14)
```
Now you can run the python file "oop_vaccine_date_vaidator.py"

On Running the file you will see a GUI with live webcam feed on the left, place the vaccine certificate(2nd vaccine certificate) in front of the webcam and click on the "Validate Dates" button on the right. The code will extract dates using OCR and display if the person should be "ALLOWED" or "NOT ALLOWED", according to the vaccination dates. Every time a person is "ALLOWED" the count of allowed people is incremented by 1.

### **GUI**
The GUI is made using a python library called tkinter and it consists of:

1) Live Video (Blue rectangle in the images) : Live feed of the vaccine certificate when it is placed in front of the webcam is displayed in this section.
2) Validate Dates Button (Red rectangle in the images) : On press, this button calls validation function and the OCR extracts the dates and displays "ALLOWED", "NOT ALLOWED", or "CHECK" in Entry Status section.
3) Signal (Black Rectangle in the images) : If the Entry Status is "ALLOWED", the signal is Green, if it is "NOT ALLOWED" the signal is Red, and if it is "CHECK" the signal is Yellow.
4) Entry Status (Yellow Rectangle in the images) : This section displays "ALLOWED", "NOT ALLOWED", "CHECK".
5) Allowed Count (Orange Rectangle in the images) : Count of all the "ALLOWED" people.

### ALLOWED IMAGE

![alt text](https://github.com/wasdac9/Vaccine-Certificate-Date-Validation/blob/main/allowed_image.png?raw=true)

As can be seen in the example image, when a vaccine certificate with dates 21 Jul 2021 (1st vaccination date), 30 Oct 2021 (2nd vaccination date) are placed in the camera frame and "Validate Dates" button is pressed, the Signal is Green and Entry Status is "ALLOWED" and Allowed Count is incremented by 1.

Note: Personal info is blurred in the image

### NOT ALLOWED IMAGE

![alt text](https://github.com/wasdac9/Vaccine-Certificate-Date-Validation/blob/main/not_allowed_image.png?raw=true)

Note: Since I don't have any vaccine certificate for the "NOT ALLOWED" example, I have used fake dates here.

When the dates 16 Jan 2022(1st vaccination date), 16 May 2022(2nd vaccination date) are placed in the camera frame and "Validate Dates" button is pressed, the Signal is Red and Entry Status is "NOT ALLOWED" and Allowed Count is unchanged. 
(This is because the difference between 16 May 2022 and 28 May 2022(the date of this demo) is not more than that of 14 days)

### CHECK IMAGE

![alt text](https://github.com/wasdac9/Vaccine-Certificate-Date-Validation/blob/main/check_image.png?raw=true)

If the image is unclear or OCR cannot extract dates or if the frame is blank,and "Validate Dates" button is pressed, the Signal becomes Yellow and Entry Status is "CHECK" and Allowed Count is unchanged.
In this status, we can try pressing "Validate Dates" button again to see if the OCR picks up the dates or else manual intervention is required to check the dates.

## Summary
With this project we proved the concept that the manual task of Validating Vaccine dates can be automated using opencv and tesseract OCR. This is a simple computer vision solution for a real life problem during the COVID-19 pandemic. 

## Limitations
1) Tesseract OCR is an open source OCR engine but it is very slow and not very accurate, hence its results are unreliable.
2) The webcam quality should be good and the frame requires sufficient lighting for validation of dates.

## Future Work
In the mobile first world, this project can be deployed on a mobile device which has a camera (for video input),
a flash (for sufficient light) and enough computation power to carry out OCR on the mobile. This would reduce the cost of hardware like PC, webcam, etc at the entrance of establishments. 
But since the government is lifting the pandemic regulations now with COVID-19 cases dropping day by day, the need to check vaccine certificates is becoming unnecessary, hence any future work on this project seems unlikely.

# ESP32 PCB Assembly 

<p>
Using solder paste and a stencil, the PCB was fabricated using the following surface mounted components:
</p>

<p align="center">
  <img src="/bom-esp32s3mini.png" width="400">
</p>

<p> </p>

<p>
  To be able to program the ESP32 microcontroller, external circuitry was required. This included the USB-C port, ESD protection diodes, Voltage Regulator IC, etc. Fortunately, the ESP32-S3-MINI-1 has an on-chip USB Serial/JTAG Controller, so we can flash the microcontroller without too much external circuitry. 
</p>

<p align="center">
  <img src="/schm.png" width="750"><br>
  <img src="/pcb_layout.png" width="500">
</p>

---

<p>
  After placing all components on their respective pads, I heated my PCB in the reflow oven in UCSD's EnVision MakerSpace for 20 minutes. This was the outcome:
</p>

<p align="center">
  <img src="/esp32-s3-mini-1.png" width="300">
</p>

---

### **Programming the Microcontroller**

<p>
  By plugging the PCB into a laptop, with the power switch off, you can put the ESP32 in USB-Serial-JTAG Download Boot mode. By holding the BOOT button and flipping the power switch,
  the laptop will recognize the device:
</p>

<p align="center">
  <img src="/bootmode.png" width="400">
</p>

<p>
  For simplicity, CircuitPython was used to run programs on this device by going to their website and flashing CircuitPython 10.1.4 intended for the ESP32-S3-DevKitC-N8 to the MCU. The device
  is not an exact match, but it ultimately works because both my PCB and the ESP32 DevKit use an ESP32-S3 microcontroller, mine just happens to be an S3-mini.
</p>

---

### **Verifying Device Functionality**

In code.py, the correctness of the design is validated by executing a BLE program that receives analog data from a [BLE Central Device](https://github.com/bigbyrus/ble-project) using the Nordic UART Service. To visually verify that the analog signals are being received
correctly, I soldered female pin holders to the exposed pins on the PCB, and connected the "VU Shield" supplied by UCSD's EnVision Makerspace

<p>
  <em>VU Shield</em><br>
  <img src="/vumeter.png" width="400">
</p>

---


![Demo](IMG_1625gif.gif)

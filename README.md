# MagStrike

MagStrike is a custom hall effect keyboard that has a 60 percent layout.
It uses the Gateron Low Profile Magnetic Jade Switches. The brains of this keyboard is a Rpi Pico 2 that runs micropython that communicates with a python script running on the main PC/Laptop

## Why did i build this???
I built this keyboard because i have always wanted to make my own keyboard from scratch and when i stumbled across hall-effect one day i quickly fell in love with it. I also wanted to use low profile switches so my wrists wouldnt hurt all day. I Found the perfect switch for this which is the Gateron Low Profile Magnetic Jade switches.

## What did it take?
It took about 2 weeks to build this it is my first every PCB and unfortunately i couldn't find anywhere to place the rasberry pi pico so i had to put it outside the keyboard. I also designed the case without a top plate so it is easy to print and easy to see the insides

## If i did it again what would i do?
 I would probably make a custom devboard with the rp2040 and embed it inside the footprint of the keyboard.
 
## READ THIS:
the 3d file was to big to commit to github so this is the google drive link:
    https://drive.google.com/file/d/1xGtgr9WMyzFMHPNl8FSLAcrnGV7yFdcr/view
 
### My Bill of Materials

| Item | Description | Quantity | Unit Price (USD) | Total Price (USD) | Shipping(USD) | URL | Running Total(USD) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Switches | Gateron Low Profile Magnetic Jade | 1 x pack of 70 | 56 | 56 | 4.3 | [Link](https://www.gateron.com/products/gateron-low-profile-magnetic-jade-switch?VariantsId=10872) | 60.3 |
| Stabilizer | GATERON Low Profile Plate Mounted Stabilizer | 1 | 8 | 8 | 2.45(Processing Fee) | [Link](https://www.gateron.com/products/gateron-low-profile-plate-mounted-stabilizer?VariantsId=10540) | 70.75 |
| Capacitor | 50V 100nF X7R ±10% 0603 Ceramic Capacitors RoHS | 100 | 0.0025 | 0.25 | 8.87 | [Link](https://www.lcsc.com/product-detail/C14663.html?utm_source=chatgpt.com) | 79.87 |
| Hall Effect Sensor | Analog-Bipolar Hall Effect Sensor | 70 | 0.2345 | 16.42 | N/A | [Link](https://www.lcsc.com/product-detail/C962159.html) | 96.29 |
| Multiplexer | IC MUX 16:1 160OHM 24SOIC | 5 | 0.83 | 3.32 | N/A | [Link](https://www.lcsc.com/sea rch?q=%20CD74HC4067M96%20&s_z=n_%20CD74HC4067M96%20) | 99.61 |
| Rasberry Pi Pico | Rasberry Pi Pico | 1 | 4.32 | 4.32 | 2.42 | [Link](https://core-electronics.com.au/raspberry-pi-pico.html) | 106.35 |
| PCB | THE pcb | 5 | N/A | 26.35 | 18.43 | [Link](https://cart.jlcpcb.com/shopcart/cart/) | 151.13 |


### I didnt include all of the shopping carts so here it is(Note that on gateron website it says some cheaper that the bom but that is cause of a sale that is ending in 16 hours.):
![PCB](/Images/JLC.png)
![shop](/Images/cORE.png)
![shop](/Images/Gateron.png)
![shop](/Images/JLC.png)
![shop](/Images/lcsc.png)

# 3d render:
![Render](/Images/render.png)



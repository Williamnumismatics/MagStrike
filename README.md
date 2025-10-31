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

| Part | Description | Quantity | Unit Price (AUD) | Total Price (AUD) | Fee / Notes | Link | Cumulative Total (AUD) |
|------|-------------|----------|-----------------|-----------------|-------------|------|-----------------------|
| Switches | Gateron Low Profile Magnetic Jade (1 x pack of 70) | 56 | 4.3 | 56 | - | [Link](https://www.gateron.com/products/gateron-low-profile-magnetic-jade-switch?VariantsId=10872) | 60.3 |
| Stabilizer | GATERON Low Profile Plate Mounted Stabilizer | 1 | 8 | 8 | 3 (Processing Fee) | [Link](https://www.gateron.com/products/gateron-low-profile-plate-mounted-stabilizer?VariantsId=10540) | 68.3 |
| Capacitor | 50V 100nF X7R ±10% 0603 Ceramic Capacitors RoHS | 70 | 0.0025 | 0.25 | 8.78 | [Link](https://www.lcsc.com/product-detail/C14663.html?utm_source=chatgpt.com) | 77.3 |
| Hall Effect Sensor | Analog-Bipolar Hall Effect Sensor | 70 | 0.2345 | 16.42 | N/A | [Link](https://www.lcsc.com/product-detail/C962159.html) | 93.72 |
| Multiplexer | 160Ω 16:1 SOIC-24-300mil Analog Switches, Multiplexers, Demultiplexers RoHS | 5 | 0.6172 | 3.09 | N/A | [Link](https://www.lcsc.com/product-detail/C1545936.html?s_z=n_CD74HC4067M) | 96.81 |
| Raspberry Pi Pico | Raspberry Pi Pico | 1 | 4.32 | 4.32 | 5.85 | [Link](https://core-electronics.com.au/raspberry-pi-pico.html) | 102.66 |
| PCB | THE PCB | 5 | N/A | 26.35 | 18.43 | [Link](https://cart.jlcpcb.com/shopcart/cart/) | 147.44 |
| Keycap | Keycap | 1 | 24.3 | 24.3 | 0 | [Link](https://www.aliexpress.com/item/1005004840360158.html?spm=a2g0o.productlist.main.2.1f034deaqPZaon&aem_p4p_detail=202510310235431605446549089200000325829&algo_pvid=ba55caf8-806d-4b17-adf7-32431a53e844&algo_exp_id=ba55caf8-806d-4b17-adf7-32431a53e844-1&pdp_ext_f=%7B%22order%22%3A%22549%22%2C%22eval%22%3A%221%22%2C%22fromPage%22%3A%22search%22%7D&pdp_npi=6%40AUD%2137.15%2114.12%21%21%2123.98%219.11%21%402101e2b617619033438188470ed0b0%2112000033198291368%21sea%21AU%210%21ABX%211%210%21n_tag%3A-29910%3Bd%3Aabb7ff7c%3Bm03_new_user%3A-29895%3BpisId%3A5000000190291127&curPageLogUid=07EuITmEFWFK&utparam-url=scene%3Asearch%7Cquery_from%3A%7Cx_object_id%3A1005004840360158%7C_p_origin_prod%3A&search_p4p_id=202510310235431605446549089200000325829_1) | 171.74 |


### I didnt include all of the shopping carts so here it is(Note that on gateron website it says some cheaper that the bom but that is cause of a sale that is ending in 16 hours.):
